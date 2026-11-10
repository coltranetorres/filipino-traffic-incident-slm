"""Regenerate results/summary*.md|png and results/errors_<run>.md from committed artifacts only.

No model is loaded and nothing is re-scored: reads experiments/<run>/results*.json, meta*.json,
predictions_test.jsonl and data/processed/test.jsonl.

Usage: uv run python scripts/make_reports.py [--experiments experiments] [--results results]
"""
from __future__ import annotations

import argparse
from pathlib import Path

from trafficslm.data import load_split
from trafficslm.errors import error_report
from trafficslm.evaluate import read_raws
from trafficslm.report import collect, write_summary
from trafficslm.runs import ERROR_REPORT_RUNS


def main(argv: list[str] | None = None) -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--experiments", default="experiments")
    ap.add_argument("--results", default="results")
    a = ap.parse_args(argv)
    exp, res = Path(a.experiments), Path(a.results)
    write_summary(collect(exp, "validation"), res / "summary.md", res / "summary.png")
    write_summary(collect(exp, "test"), res / "summary_test.md", res / "summary_test.png")
    records = load_split("test")
    for run in ERROR_REPORT_RUNS:
        error_report(records, read_raws(exp / run, records, "test"), res / f"errors_{run}.md")
    print(f"wrote reports to {res}")


if __name__ == "__main__":
    main()
