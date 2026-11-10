"""Post-hoc alias-coverage sensitivity of test location F1.

Post-hoc, computed after scoring; not used for any selection. data/aliases.json is NOT modified and no
run is re-scored on disk: the seven bare-name aliases below are written to a separate file
(results/aliases_extended_posthoc.json = data/aliases.json + extras) and metrics.ALIASES_PATH is pointed at it
temporarily, in memory, while location F1 (with the same bootstrap CI as the main tables) is recomputed from
the stored predictions.

Usage: uv run python scripts/alias_sensitivity.py [--out results/alias_sensitivity_test.md]
"""
from __future__ import annotations

import argparse
import contextlib
import json
import tempfile
from pathlib import Path

from trafficslm import metrics as M
from trafficslm.runs import TEST_RUNS
from trafficslm.tables import fmt_entry

EXTRA_ALIASES = {
    "Commonwealth Avenue": ["Commonwealth"],
    "Shaw Boulevard": ["Shaw"],
    "Recto Avenue": ["Recto"],
    "Ortigas Avenue": ["Ortigas"],
    "Marcos Highway": ["Marcos"],
    "Kalayaan Avenue": ["Kalayaan"],
    "McArthur Highway": ["McArthur"],
}


def extended_alias_map() -> dict[str, list[str]]:
    base = json.loads(M.ALIASES_PATH.read_text(encoding="utf-8"))
    out = {k: list(v) for k, v in base.items()}
    for canon, aliases in EXTRA_ALIASES.items():
        out.setdefault(canon, [])
        out[canon] += [a for a in aliases if a not in out[canon]]
    return out


@contextlib.contextmanager
def alias_file(path: Path | None = None):
    """Temporarily point metrics at the extended alias file; restore on exit."""
    path = Path(path) if path else Path(tempfile.mkdtemp()) / "aliases_extended_posthoc.json"
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(extended_alias_map(), indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    orig = M.ALIASES_PATH
    M.ALIASES_PATH = path
    M.load_aliases.cache_clear()
    try:
        yield path
    finally:
        M.ALIASES_PATH = orig
        M.load_aliases.cache_clear()


def location_entry(records, raws, extended: bool, path: Path | None = None) -> dict:
    from trafficslm.evaluate import score
    if extended:
        with alias_file(path):
            return score(records, raws)["location"]["f1"]
    return score(records, raws)["location"]["f1"]


def location_f1(records, raws, extended: bool) -> float:
    return location_entry(records, raws, extended)["value"]


def main(argv: list[str] | None = None) -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", default="results/alias_sensitivity_test.md")
    ap.add_argument("--alias-out", default="results/aliases_extended_posthoc.json")
    ap.add_argument("--experiments", default="experiments")
    a = ap.parse_args(argv)
    from trafficslm.data import load_split
    from trafficslm.evaluate import read_raws

    records = load_split("test")
    rows, ent = [], {}
    for run in TEST_RUNS:
        d = Path(a.experiments) / run
        raws = read_raws(d, records, "test")
        stored = json.loads((d / "results_test.json").read_text(encoding="utf-8"))["scores"]["location"]["f1"]
        base = location_entry(records, raws, False)
        assert abs(base["value"] - stored["value"]) < 1e-9, f"{run}: base location F1 does not reproduce"
        ext = location_entry(records, raws, True, Path(a.alias_out))
        ent[run] = (base, ext)
        rows.append(f"| {run} | {fmt_entry(base)} | {fmt_entry(ext)} | {ext['value'] - base['value']:+.3f} |")

    def sep(a_, b_, k):
        (ba, ea), (bb, eb) = ent[a_], ent[b_]
        x, y = (ba, bb) if k == 0 else (ea, eb)
        return "separated (CIs do not overlap)" if x["ci"][0] > y["ci"][1] or y["ci"][0] > x["ci"][1] \
            else "not separated (CIs overlap)"

    lines = ["# Alias-coverage sensitivity of test location F1", "",
             "Post-hoc, computed after scoring; not used for any selection. The pre-registered numbers "
             "(`data/aliases.json`) remain the ones in the main tables. Here the same stored predictions are "
             "re-scored in memory with seven extra bare-name road aliases (listed below); the 95% CI is the "
             "same bootstrap (1000 resamples, seed 0) as in the main tables. The `pre-registered` column "
             "reproduces `results_test.json` exactly (checked by the script).", "",
             "Extra aliases (canonical road <- alias): "
             + "; ".join(f"{c} <- {', '.join(v)}" for c, v in EXTRA_ALIASES.items())
             + ". Extended alias file: `results/aliases_extended_posthoc.json`.", "",
             "| run | location F1, pre-registered aliases | location F1, extended aliases | change |",
             "|---|---|---|---|"] + rows + ["", "## Interval separation, LoRA n207 vs few-shot (same model)", "",
             "| comparison | pre-registered aliases | extended aliases |", "|---|---|---|"]
    for fam in ("gemma3-1b", "qwen2.5-1.5b"):
        lines.append(f"| {fam} LoRA n207 vs few-shot | {sep(fam + '-lora-n207', fam + '-fewshot', 0)} "
                     f"| {sep(fam + '-lora-n207', fam + '-fewshot', 1)} |")
    out = Path(a.out)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"wrote {out}")


if __name__ == "__main__":
    main()
