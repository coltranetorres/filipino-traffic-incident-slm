import importlib.util
from pathlib import Path


def _load():
    p = Path(__file__).resolve().parents[1] / "scripts" / "check_leakage.py"
    spec = importlib.util.spec_from_file_location("check_leakage_mod", p)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


def test_leakage_stats():
    m = _load()
    test = [("te-1", "Stalled truck on EDSA near Cubao"), ("te-2", "Totally different words here")]
    ref = [("tr-1", "Stalled truck on EDSA near Cubao"), ("tr-2", "stalled truck on edsa near guadalupe")]
    s = m.leakage_stats(test, ref)
    assert s["exact_duplicates"] == [("te-1", "tr-1")]
    assert s["max_ratio"][0] == 1.0 and s["max_ratio"][1:] == ("te-1", "tr-1")
    assert s["pairs_gt_07"] >= 1 and s["pairs_gt_08"] >= 1
    assert s["max_jaccard"][0] == 1.0


def test_leakage_no_overlap():
    m = _load()
    s = m.leakage_stats([("te-1", "aaa bbb")], [("tr-1", "ccc ddd")])
    assert s["exact_duplicates"] == [] and s["pairs_gt_07"] == 0 and s["max_jaccard"][0] == 0.0
