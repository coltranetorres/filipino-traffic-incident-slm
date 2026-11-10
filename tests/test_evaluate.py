import json
import math

import pytest

from trafficslm.evaluate import guard_test_access, score, score_subsets
from trafficslm.prompts import target_json
from trafficslm.schema import Record


def rec(i, itype="road_accident", road="EDSA", lang="taglish", tags=(), sev="low"):
    return Record.model_validate({
        "id": i, "split": "test", "text": "x", "language": lang,
        "incident_type": itype,
        "location": {"road": road, "landmark": None, "direction": None},
        "severity": sev, "road_obstruction": "none", "tags": list(tags),
    })


def recs():
    return [rec("a"), rec("b", "flooding", None, sev="high"),
            rec("c", "heavy_traffic", "C5", "english"), rec("d", "road_closure", "Roxas Blvd", "filipino")]


def test_score_perfect_predictions():
    rs = recs()
    s = score(rs, [target_json(r) for r in rs])
    assert s["n"] == 4
    for k in ("json_validity", "incident_macro_f1", "severity_acc", "obstruction_acc",
              "language_acc", "abstention"):
        assert s[k]["value"] == 1.0, k
    assert s["location"]["f1"]["value"] == 1.0
    assert s["location"]["road_acc"]["value"] == 1.0
    assert len(s["json_validity"]["ci"]) == 2


def test_score_all_garbage():
    rs = recs()
    s = score(rs, ["nope", "", "{", "[]"])
    assert s["json_validity"]["value"] == 0.0
    assert s["severity_acc"]["value"] == 0.0
    assert s["language_acc"]["value"] == 0.0
    assert s["location"]["road_acc"]["value"] == 0.0


def test_score_fenced_and_truncated_mix():
    rs = recs()
    raws = ["```json\n" + target_json(rs[0]) + "\n```", target_json(rs[1]),
            target_json(rs[2])[:20], "text " + target_json(rs[3])]
    s = score(rs, raws)
    assert s["json_validity"]["value"] == 0.75
    assert s["severity_acc"]["value"] == pytest.approx(0.75)


def test_score_length_mismatch_raises():
    with pytest.raises(ValueError):
        score(recs(), ["x"])


def test_subset_with_zero_or_one_item_gives_nan_not_error():
    rs = [rec("a", lang="english", tags=["noisy"]), rec("b", lang="filipino")]
    sub = score_subsets(rs, [target_json(r) for r in rs])
    assert sub["lang:taglish"]["n"] == 0
    assert math.isnan(sub["lang:taglish"]["json_validity"]["value"])
    assert sub["tag:short"]["n"] == 0
    assert sub["tag:noisy"]["n"] == 1
    assert sub["tag:noisy"]["json_validity"]["value"] == 1.0
    assert "lang:english" in sub and "tag:contradictory" in sub


def test_guard_blocks_test_without_final(tmp_path):
    log = tmp_path / "t.log"
    with pytest.raises(PermissionError):
        guard_test_access("r1", "test", False, log)
    assert not log.exists()


def test_guard_allows_first_final_run(tmp_path):
    log = tmp_path / "sub" / "t.log"
    guard_test_access("r1", "test", True, log)
    assert log.read_text().split() == ["r1"]


def test_guard_blocks_second_test_run_same_run(tmp_path):
    log = tmp_path / "t.log"
    guard_test_access("r1", "test", True, log)
    with pytest.raises(PermissionError):
        guard_test_access("r1", "test", True, log)
    guard_test_access("r2", "test", True, log)


def test_guard_ignores_validation(tmp_path):
    log = tmp_path / "t.log"
    guard_test_access("r1", "validation", False, log)
    guard_test_access("r1", "validation", False, log)
    assert not log.exists()


# --- main() reservation handling ---
from trafficslm import evaluate as ev  # noqa: E402


@pytest.fixture
def env(tmp_path, monkeypatch):
    rs = recs()
    calls = []
    monkeypatch.setattr(ev, "load_split", lambda name: (calls.append(name), rs)[1])
    monkeypatch.setattr(ev, "verify_manifest", lambda: None)
    monkeypatch.setattr(ev, "TEST_LOG", tmp_path / "test_runs.log")
    return tmp_path, rs, calls


def write_preds(run, rs, extra_ids=()):
    run.mkdir(parents=True, exist_ok=True)
    rows = [{"id": r.id, "raw": target_json(r)} for r in rs]
    rows += [{"id": i, "raw": "x"} for i in extra_ids]
    (run / "predictions_test.jsonl").write_text("\n".join(json.dumps(r) for r in rows))


def run_main(run, *extra):
    ev.main(["--run", str(run), "--split", "test", *extra])


def test_failed_test_run_releases_reservation(env):
    tmp, rs, _ = env
    run = tmp / "r1"
    write_preds(run, rs, extra_ids=["zzz"])
    with pytest.raises(ValueError):
        run_main(run, "--final")
    assert "r1" not in (tmp / "test_runs.log").read_text().splitlines()
    write_preds(run, rs)
    run_main(run, "--final")
    assert (run / "results_test.json").exists()


def test_successful_test_run_keeps_reservation(env):
    tmp, rs, _ = env
    run = tmp / "r1"
    write_preds(run, rs)
    run_main(run, "--final")
    with pytest.raises(PermissionError):
        run_main(run, "--final")


def test_guard_fires_before_gold_labels_read(env):
    tmp, rs, calls = env
    run = tmp / "r1"
    write_preds(run, rs)
    with pytest.raises(PermissionError):
        run_main(run)
    assert calls == []


def test_log_matching_is_line_based(tmp_path):
    log = tmp_path / "t.log"
    guard_test_access("my run", "test", True, log)
    with pytest.raises(PermissionError):
        guard_test_access("my run", "test", True, log)
    guard_test_access("my", "test", True, log)


def test_read_raws_uses_split_specific_file(tmp_path):
    import json as _json
    from trafficslm.evaluate import read_raws
    rs = [rec("a"), rec("b")]
    (tmp_path / "predictions.jsonl").write_text(_json.dumps({"id": "a", "raw": "VAL"}) + "\n")
    (tmp_path / "predictions_test.jsonl").write_text(
        _json.dumps({"id": "a", "raw": "TEST-A"}) + "\n" + _json.dumps({"id": "b", "raw": "TEST-B"}) + "\n")
    assert read_raws(tmp_path, rs, "test") == ["TEST-A", "TEST-B"]
    assert read_raws(tmp_path, rs) == ["VAL", ""]
    assert read_raws(tmp_path, rs, "validation") == ["VAL", ""]
