import json

from trafficslm.infer import run_predictions
from trafficslm.schema import Record


def rec(i, text="may banggaan sa EDSA"):
    return Record.model_validate({
        "id": i, "split": "valid", "text": text, "language": "taglish",
        "incident_type": "road_accident",
        "location": {"road": "EDSA", "landmark": None, "direction": None},
        "severity": "low", "road_obstruction": "none",
    })


def lines(p):
    return [json.loads(x) for x in p.read_text().splitlines()]


def test_run_predictions_writes_one_line_per_record(tmp_path):
    out = run_predictions([rec("a"), rec("b")], lambda m: "{}", tmp_path)
    assert out == tmp_path / "predictions.jsonl"
    rows = lines(out)
    assert [r["id"] for r in rows] == ["a", "b"]
    assert all(r["raw"] == "{}" for r in rows)
    meta = json.loads((tmp_path / "meta.json").read_text())
    assert meta["mode"] == "zero-shot" and meta["shot_ids"] == []


def test_latency_recorded_and_positive(tmp_path):
    out = run_predictions([rec("a")], lambda m: "x", tmp_path)
    assert lines(out)[0]["latency_ms"] > 0
    meta = json.loads((tmp_path / "meta.json").read_text())
    assert meta["latency_ms_mean"] > 0 and meta["latency_ms_median"] > 0


def test_generator_exception_recorded_not_fatal(tmp_path):
    def gen(msgs):
        if msgs[-1]["content"] == "boom":
            raise RuntimeError("bad")
        return "ok"
    rows = lines(run_predictions([rec("a", "boom"), rec("b")], gen, tmp_path))
    assert rows[0]["raw"] == "" and "bad" in rows[0]["error"]
    assert rows[1]["raw"] == "ok" and "error" not in rows[1]


def test_few_shot_messages_passed(tmp_path):
    seen = []
    shot = rec("s1", "shot text")
    run_predictions([rec("a")], lambda m: seen.append(m) or "x", tmp_path, shots=[shot],
                    meta={"model": "m", "adapter": None})
    assert seen[0][1] == {"role": "user", "content": "shot text"}
    meta = json.loads((tmp_path / "meta.json").read_text())
    assert meta["mode"] == "few-shot" and meta["shot_ids"] == ["s1"] and meta["model"] == "m"
