"""Post-hoc metrics from stored test predictions: severity macro-F1 and per-class incident precision/recall/F1.

Post-hoc, computed after scoring; not used for any selection. Reads data/processed/test.jsonl and
experiments/<run>/predictions_test.jsonl only; scoring logic in src/trafficslm/metrics.py is reused unchanged.

Usage: uv run python scripts/posthoc_metrics.py [--out results/posthoc_metrics_test.md]
"""
from __future__ import annotations

import argparse
import math
from pathlib import Path

from trafficslm import metrics as M
from trafficslm.runs import TEST_RUNS
from trafficslm.schema import INCIDENT_TYPES, parse_report


def compute(records, raws) -> dict:
    preds = [parse_report(r) for r in raws]
    g_inc = [r.incident_type for r in records]
    p_inc = [p.incident_type if p else None for p in preds]
    g_sev = [r.severity for r in records]
    p_sev = [p.severity if p else None for p in preds]
    per_class = {}
    for c in INCIDENT_TYPES:
        tp = sum(g == c and p == c for g, p in zip(g_inc, p_inc))
        fp = sum(g != c and p == c for g, p in zip(g_inc, p_inc))
        fn = sum(g == c and p != c for g, p in zip(g_inc, p_inc))
        support = tp + fn
        per_class[c] = {
            "precision": tp / (tp + fp) if tp + fp else math.nan,
            "recall": tp / support if support else math.nan,
            "f1": 2 * tp / (2 * tp + fp + fn) if 2 * tp + fp + fn else math.nan,
            "support": support,
        }
    present = [c for c in INCIDENT_TYPES if per_class[c]["support"]]
    mean_f1 = sum(per_class[c]["f1"] for c in present) / len(present)
    assert abs(mean_f1 - M.macro_f1(g_inc, p_inc)) < 1e-9  # agrees with the pre-registered metric
    return {"severity_macro_f1": M.macro_f1(g_sev, p_sev), "per_class": per_class,
            "valid": sum(p is not None for p in preds)}


def _f(x) -> str:
    return "n/a" if isinstance(x, float) and math.isnan(x) else f"{x:.2f}"


def main(argv: list[str] | None = None) -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", default="results/posthoc_metrics_test.md")
    ap.add_argument("--experiments", default="experiments")
    a = ap.parse_args(argv)
    from trafficslm.data import load_split
    from trafficslm.evaluate import read_raws

    records = load_split("test")
    res = {run: compute(records, read_raws(Path(a.experiments) / run, records, "test")) for run in TEST_RUNS}
    support = {c: res[TEST_RUNS[0]]["per_class"][c]["support"] for c in INCIDENT_TYPES}
    lines = ["# Post-hoc metrics on the test split (n=%d)" % len(records), "",
             "Post-hoc, computed after scoring; not used for any selection. Not part of the pre-registered "
             "metric list. Point estimates only (no confidence intervals). Computed from the stored "
             "`predictions_test.jsonl` of each run; invalid outputs count as a wrong prediction (no class "
             "predicted). Severity macro-F1 averages over the severity classes present in the gold labels "
             "(low, medium, high, unknown).", "",
             "## Severity macro-F1", "", "| run | severity macro-F1 |", "|---|---|"]
    lines += [f"| {r} | {_f(res[r]['severity_macro_f1'])} |" for r in TEST_RUNS]
    lines += ["", "## Per-class incident-type precision / recall / F1", "",
              "Cells are `precision / recall / F1`. `n/a` means the quantity is undefined (no predictions of "
              "that class for precision). Gold support per class (test): "
              + ", ".join(f"{c} {support[c]}" for c in INCIDENT_TYPES) + ".", "",
              "| run | " + " | ".join(INCIDENT_TYPES) + " |", "|" + "---|" * (len(INCIDENT_TYPES) + 1)]
    for r in TEST_RUNS:
        cells = [" / ".join(_f(res[r]["per_class"][c][k]) for k in ("precision", "recall", "f1"))
                 for c in INCIDENT_TYPES]
        lines.append(f"| {r} | " + " | ".join(cells) + " |")
    out = Path(a.out)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"wrote {out}")


if __name__ == "__main__":
    main()
