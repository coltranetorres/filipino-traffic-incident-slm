"""Markdown table formatting shared by the report and run scripts."""
from __future__ import annotations

import math

COLUMNS = [
    ("json_validity", ("json_validity",)),
    ("incident_macro_f1", ("incident_macro_f1",)),
    ("incident_macro_f1_no_unknown", ("incident_macro_f1_no_unknown",)),
    ("severity_acc", ("severity_acc",)),
    ("obstruction_acc", ("obstruction_acc",)),
    ("language_acc", ("language_acc",)),
    ("location_f1", ("location", "f1")),
    ("abstention", ("abstention",)),
]


def _ok(x) -> bool:
    return isinstance(x, (int, float)) and math.isfinite(x)


def fmt_num(x, nd: int = 2) -> str:
    return f"{x:.{nd}f}" if _ok(x) else "n/a"


def fmt_entry(e: dict | None) -> str:
    if not e or not _ok(e.get("value")):
        return "n/a"
    lo, hi = (e.get("ci") or [None, None])[:2]
    if _ok(lo) and _ok(hi):
        return f"{fmt_num(e['value'])} [{fmt_num(lo)}, {fmt_num(hi)}]"
    return fmt_num(e["value"])


def build_table(runs: dict[str, tuple[dict, dict]]) -> str:
    head = [c for c, _ in COLUMNS] + ["median_latency_ms", "peak_memory_gb"]
    lines = ["| run | " + " | ".join(head) + " |", "|" + "---|" * (len(head) + 1)]
    for name, (res, meta) in runs.items():
        cells = []
        for _, path in COLUMNS:
            e = res["scores"]
            for p in path:
                e = e[p]
            cells.append(fmt_entry(e))
        cells.append(fmt_num(meta.get("latency_ms_median"), 0))
        cells.append(fmt_num(meta.get("peak_memory_gb"), 2))
        lines.append(f"| {name} | " + " | ".join(cells) + " |")
    return "\n".join(lines) + "\n"
