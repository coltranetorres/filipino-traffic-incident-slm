"""Score predictions against gold, per subset, with a test-split guard."""
from __future__ import annotations

import argparse
import json
import math
import os
from pathlib import Path

from . import metrics as M
from .data import load_split, verify_manifest
from .schema import LANGUAGES, Record, parse_report

TAGS = ("noisy", "no_location", "short", "ambiguous", "contradictory")
TEST_LOG = Path("experiments/test_runs.log")
NAN = float("nan")


def _cv(fn, n):
    lo, hi = M.bootstrap_ci(fn, n)
    return lo, hi


def score(records: list[Record], raws: list[str]) -> dict:
    if len(records) != len(raws):
        raise ValueError(f"{len(records)} records but {len(raws)} predictions")
    n = len(records)
    preds = [parse_report(r) for r in raws]
    g_inc = [r.incident_type for r in records]
    p_inc = [p.incident_type if p else None for p in preds]
    g_sev = [r.severity for r in records]
    p_sev = [p.severity if p else None for p in preds]
    g_obs = [r.road_obstruction for r in records]
    p_obs = [p.road_obstruction if p else None for p in preds]
    g_lang = [r.language for r in records]
    p_lang = [p.language if p else None for p in preds]
    g_loc = [r.location for r in records]
    p_loc = [p.location if p else None for p in preds]
    valid = [1.0 if p else 0.0 for p in preds]

    def sel(xs, idx):
        return [xs[i] for i in idx]

    def entry(fn):
        value = fn(list(range(n))) if n else NAN
        return {"value": value, "ci": list(_cv(fn, n))}

    loc_cache: dict[tuple, dict] = {}

    def loc(idx):
        key = tuple(idx)
        if key not in loc_cache:
            loc_cache.clear() if len(loc_cache) > 4 else None
            loc_cache[key] = M.location_scores(sel(g_loc, idx), sel(p_loc, idx))
        return loc_cache[key]

    def mean_valid(idx):
        return sum(sel(valid, idx)) / len(idx) if idx else NAN

    return {
        "n": n,
        "json_validity": entry(mean_valid),
        "incident_macro_f1": entry(lambda i: M.macro_f1(sel(g_inc, i), sel(p_inc, i))),
        "incident_macro_f1_no_unknown": entry(
            lambda i: M.macro_f1(sel(g_inc, i), sel(p_inc, i), frozenset({"unknown"}))),
        "severity_acc": entry(lambda i: M.accuracy(sel(g_sev, i), sel(p_sev, i))),
        "obstruction_acc": entry(lambda i: M.accuracy(sel(g_obs, i), sel(p_obs, i))),
        "language_acc": entry(lambda i: M.accuracy(sel(g_lang, i), sel(p_lang, i))),
        "location": {
            k: entry(lambda i, k=k: loc(i)[k])
            for k in ("f1", "road_acc", "landmark_acc", "direction_acc")
        },
        "abstention": entry(lambda i: M.abstention_rate(sel(g_loc, i), sel(p_loc, i))),
    }


def score_subsets(records: list[Record], raws: list[str]) -> dict[str, dict]:
    if len(records) != len(raws):
        raise ValueError(f"{len(records)} records but {len(raws)} predictions")
    out = {}
    groups = [(f"lang:{lang}", lambda r, lang=lang: r.language == lang) for lang in LANGUAGES]
    groups += [(f"tag:{t}", lambda r, t=t: t in r.tags) for t in TAGS]
    for name, pred in groups:
        idx = [i for i, r in enumerate(records) if pred(r)]
        out[name] = score([records[i] for i in idx], [raws[i] for i in idx])
    return out


def guard_test_access(run_name: str, split: str, final: bool, log_path: Path = TEST_LOG) -> None:
    if split != "test":
        return
    log_path = Path(log_path)
    if not final:
        raise PermissionError("test split requires --final")
    seen = log_path.read_text(encoding="utf-8").splitlines() if log_path.exists() else []
    if run_name in seen:
        raise PermissionError(f"run {run_name!r} has already been evaluated on the test split")
    log_path.parent.mkdir(parents=True, exist_ok=True)
    with open(log_path, "a", encoding="utf-8") as f:
        f.write(run_name + "\n")


def release_test_run(run_name: str, log_path: Path = TEST_LOG) -> None:
    log_path = Path(log_path)
    if not log_path.exists():
        return
    lines = log_path.read_text(encoding="utf-8").splitlines()
    kept = [x for x in lines if x != run_name]
    if len(kept) != len(lines):
        log_path.write_text("".join(x + "\n" for x in kept), encoding="utf-8")


def _clean(o):
    if isinstance(o, float) and not math.isfinite(o):
        return None
    if isinstance(o, dict):
        return {k: _clean(v) for k, v in o.items()}
    if isinstance(o, (list, tuple)):
        return [_clean(v) for v in o]
    return o


def read_raws(run: Path, records: list[Record], split: str = "validation") -> list[str]:
    by_id: dict[str, str] = {}
    pred_name = "predictions_test.jsonl" if split == "test" else "predictions.jsonl"
    with open(Path(run) / pred_name, encoding="utf-8") as f:
        for line in f:
            if line.strip():
                row = json.loads(line)
                by_id[row["id"]] = row.get("raw") or ""
    unknown = set(by_id) - {r.id for r in records}
    if unknown:
        raise ValueError(f"predictions contain ids not in split: {sorted(unknown)[:5]}")
    return [by_id.get(r.id, "") for r in records]


def main(argv: list[str] | None = None) -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--run", required=True)
    ap.add_argument("--split", required=True, choices=["validation", "test"])
    ap.add_argument("--final", action="store_true")
    a = ap.parse_args(argv)
    run = Path(a.run)
    if a.split == "test":
        verify_manifest()
    guard_test_access(run.name, a.split, a.final, TEST_LOG)
    try:
        records = load_split(a.split)
        raws = read_raws(run, records, a.split)
        result = {"split": a.split, "scores": score(records, raws),
                  "subsets": score_subsets(records, raws)}
        name = "results_test.json" if a.split == "test" else "results.json"
        tmp = run / (name + ".tmp")
        tmp.write_text(json.dumps(_clean(result), indent=2, ensure_ascii=False),
                       encoding="utf-8")
        os.replace(tmp, run / name)
    except BaseException:
        if a.split == "test":
            release_test_run(run.name, TEST_LOG)
        raise
    print(f"wrote {run / name}")


if __name__ == "__main__":
    main()
