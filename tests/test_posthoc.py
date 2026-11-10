import importlib.util
import json
from pathlib import Path

from trafficslm.schema import Record


def _load(name):
    p = Path(__file__).resolve().parents[1] / "scripts" / f"{name}.py"
    spec = importlib.util.spec_from_file_location(name + "_mod", p)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


def rec(i, itype="road_accident", sev="low", road="Shaw Boulevard"):
    return Record.model_validate({
        "id": i, "split": "test", "text": "t", "language": "taglish", "incident_type": itype,
        "location": {"road": road, "landmark": None, "direction": None},
        "severity": sev, "road_obstruction": "none", "tags": []})


def raw(r, **over):
    d = json.loads(r.target().model_dump_json())
    for k, v in over.items():
        if k == "road":
            d["location"]["road"] = v
        else:
            d[k] = v
    return json.dumps(d)


def test_extended_aliases_change_location_score():
    m = _load("alias_sensitivity")
    recs = [rec("a"), rec("b")]
    raws = [raw(recs[0], road="Shaw"), raw(recs[1])]
    base = m.location_f1(recs, raws, extended=False)
    ext = m.location_f1(recs, raws, extended=True)
    assert ext == 1.0 and base < 1.0
    # restored afterwards: base again unchanged
    assert m.location_f1(recs, raws, extended=False) == base


def test_extra_aliases_are_the_seven_bare_names():
    m = _load("alias_sensitivity")
    bare = {a for v in m.EXTRA_ALIASES.values() for a in v}
    assert {"Commonwealth", "Shaw", "Recto", "Ortigas", "Marcos", "Kalayaan", "McArthur"} <= bare


def test_posthoc_metrics():
    m = _load("posthoc_metrics")
    recs = [rec("a", "road_accident", "low"), rec("b", "flooding", "high"), rec("c", "flooding", "high")]
    raws = [raw(recs[0]), raw(recs[1]), raw(recs[2], incident_type="road_accident", severity="low")]
    out = m.compute(recs, raws)
    assert out["severity_macro_f1"] > 0
    pc = out["per_class"]
    assert pc["road_accident"] == {"precision": 0.5, "recall": 1.0, "f1": 2 / 3, "support": 1}
    assert pc["flooding"]["support"] == 2 and pc["flooding"]["recall"] == 0.5 and pc["flooding"]["precision"] == 1.0
