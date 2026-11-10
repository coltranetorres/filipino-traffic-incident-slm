"""Similarity check between the test split and train/validation (no model, no scoring).

Reports exact duplicates, the maximum difflib SequenceMatcher ratio, pair counts above 0.7 and 0.8,
and the maximum token Jaccard. Texts are compared lower-cased. This is a surface-similarity check,
not proof that test scenarios are independent of training scenarios.

Usage: uv run python scripts/check_leakage.py [--out results/leakage_check.md]
"""
from __future__ import annotations

import argparse
import re
from difflib import SequenceMatcher
from pathlib import Path


def _tokens(s: str) -> set[str]:
    return set(re.findall(r"\w+", s.lower()))


def leakage_stats(test: list[tuple[str, str]], ref: list[tuple[str, str]]) -> dict:
    exact, n_pairs = [], 0
    best_ratio = (0.0, None, None)
    best_jac = (0.0, None, None)
    gt07 = gt08 = 0
    ref_tok = [(rid, rt.lower(), _tokens(rt)) for rid, rt in ref]
    for tid, tt in test:
        tl, tk = tt.lower(), _tokens(tt)
        for rid, rl, rk in ref_tok:
            n_pairs += 1
            if tl.strip() == rl.strip():
                exact.append((tid, rid))
            r = SequenceMatcher(None, tl, rl).ratio()
            gt07 += r > 0.7
            gt08 += r > 0.8
            if r > best_ratio[0]:
                best_ratio = (r, tid, rid)
            u = tk | rk
            j = len(tk & rk) / len(u) if u else 0.0
            if j > best_jac[0]:
                best_jac = (j, tid, rid)
    return {"pairs": n_pairs, "exact_duplicates": exact, "max_ratio": best_ratio,
            "pairs_gt_07": gt07, "pairs_gt_08": gt08, "max_jaccard": best_jac}


def _load(split: str) -> list[tuple[str, str]]:
    from trafficslm.data import load_split
    return [(r.id, r.text) for r in load_split(split)]


def main(argv: list[str] | None = None) -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", default="results/leakage_check.md")
    a = ap.parse_args(argv)
    test = _load("test")
    lines = ["# Test-vs-train/validation similarity check", "",
             "Descriptive check computed after scoring, not used for any selection. "
             f"Test n={len(test)}; texts compared lower-cased. Token Jaccard uses word tokens (`\\w+`). "
             "This measures surface similarity only; it is not proof that test scenarios are independent "
             "of training scenarios.", "",
             "| reference split | n | pairs compared | exact duplicates | max SequenceMatcher ratio (test id, ref id) "
             "| pairs > 0.7 | pairs > 0.8 | max token Jaccard (test id, ref id) |",
             "|---|---|---|---|---|---|---|---|"]
    refs = {"train": _load("train"), "validation": _load("validation")}
    refs["train + validation"] = refs["train"] + refs["validation"]
    for name, ref in refs.items():
        s = leakage_stats(test, ref)
        ex = ", ".join(f"{t}/{r}" for t, r in s["exact_duplicates"]) or "none"
        mr, jc = s["max_ratio"], s["max_jaccard"]
        lines.append(f"| {name} | {len(ref)} | {s['pairs']} | {ex} | {mr[0]:.2f} ({mr[1]} vs {mr[2]}) "
                     f"| {s['pairs_gt_07']} | {s['pairs_gt_08']} | {jc[0]:.2f} ({jc[1]} vs {jc[2]}) |")
    out = Path(a.out)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"wrote {out}")


if __name__ == "__main__":
    main()
