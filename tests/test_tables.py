import math

from trafficslm.tables import build_table, fmt_entry, fmt_num


def test_fmt_entry_and_num():
    assert fmt_entry({"value": 0.62, "ci": [0.48, 0.75]}) == "0.62 [0.48, 0.75]"
    assert fmt_entry({"value": math.nan, "ci": [None, None]}) == "n/a"
    assert fmt_num(12.345, 1) == "12.3"


def test_build_table_shape():
    e = {"value": 0.5, "ci": [0.4, 0.6]}
    scores = {k: e for k in ("json_validity", "incident_macro_f1", "incident_macro_f1_no_unknown",
                             "severity_acc", "obstruction_acc", "language_acc", "abstention")}
    scores["location"] = {"f1": e}
    t = build_table({"r1": ({"scores": scores}, {"latency_ms_median": 600.4, "peak_memory_gb": 3.14159})})
    lines = t.strip().split("\n")
    assert len(lines) == 3 and lines[2].startswith("| r1 | 0.50 [0.40, 0.60]")
    assert lines[2].endswith("| 600 | 3.14 |")
