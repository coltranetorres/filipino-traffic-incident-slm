from trafficslm.errors import error_report
from trafficslm.prompts import target_json
from trafficslm.schema import Record


def rec(i, itype="road_accident", road="EDSA", lang="taglish", tags=(), sev="low", text=None):
    return Record.model_validate({
        "id": i, "split": "test", "text": text or f"text-{i}", "language": lang,
        "incident_type": itype,
        "location": {"road": road, "landmark": None, "direction": None},
        "severity": sev, "road_obstruction": "none", "tags": list(tags),
    })


def fixture():
    rs = [rec("a", tags=("noisy",)), rec("b", "flooding", "C5", "english", ("short",)),
          rec("c", "flooding", "C5", "english", ("noisy", "ambiguous")),
          rec("d", "road_closure", None, "filipino", ("no_location",))]
    raws = [target_json(rs[0]),
            target_json(rs[1]),
            target_json(rec("c", "heavy_traffic", "C5", "english")),  # wrong incident
            target_json(rec("d", "road_closure", "Roxas", "filipino"))]  # wrong location
    return rs, raws


def test_error_report_lists_only_wrong_items(tmp_path):
    rs, raws = fixture()
    out = tmp_path / "e.md"
    error_report(rs, raws, out)
    t = out.read_text()
    assert "text-c" in t and "text-d" in t
    assert "text-a" not in t and "text-b" not in t
    assert "heavy_traffic" in t and "Roxas" in t


def test_error_report_groups_by_tag(tmp_path):
    rs, raws = fixture()
    out = tmp_path / "e.md"
    error_report(rs, raws, out)
    t = out.read_text()
    assert "| noisy | 1 / 2 |" in t
    assert "| ambiguous | 1 / 1 |" in t
    assert "| no_location | 1 / 1 |" in t
    assert "| short | 0 / 1 |" in t
    assert "| flooding | 1 / 2 |" in t
    assert "| english | 1 / 2 |" in t


def test_error_report_invalid_json(tmp_path):
    rs, raws = fixture()
    raws[0] = "not json at all"
    out = tmp_path / "e.md"
    error_report(rs, raws, out)
    t = out.read_text()
    assert "text-a" in t and "invalid JSON" in t
    assert "| noisy | 2 / 2 |" in t


def test_error_report_uses_alias_normalization(tmp_path):
    gold = rec("a", road="Commonwealth Avenue")
    pred = rec("a", road="commonwealth ave")
    out = tmp_path / "e.md"
    error_report([gold], [target_json(pred)], out)
    assert "text-a" not in out.read_text()
    assert "0 of 1 items" in out.read_text()
