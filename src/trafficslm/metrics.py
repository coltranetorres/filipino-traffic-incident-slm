"""Evaluation metrics (pure stdlib)."""
from __future__ import annotations

import json
import random
import re
import unicodedata
from collections.abc import Callable
from functools import lru_cache
from pathlib import Path

from trafficslm.schema import Location

ALIASES_PATH = Path(__file__).resolve().parents[2] / "data" / "aliases.json"
NAN = float("nan")
_ABBREV = {"ave": "avenue", "blvd": "boulevard", "hwy": "highway", "hway": "highway"}
FIELDS = ("road", "landmark", "direction")


def _base(s: str | None) -> str | None:
    if s is None:
        return None
    s = unicodedata.normalize("NFKD", s.strip().lower())
    s = "".join(c for c in s if not unicodedata.combining(c))
    if s in ("", "null"):
        return None
    s = s.replace(".", " ").replace(",", " ")
    toks = [_ABBREV.get(t, t) for t in s.split()]
    return " ".join(toks) or None


@lru_cache(maxsize=None)
def load_aliases(path: str | None = None) -> dict[str, str]:
    """Map normalized alias (and canonical) -> normalized canonical road."""
    p = Path(path) if path else ALIASES_PATH
    raw = json.loads(p.read_text(encoding="utf-8"))
    out: dict[str, str] = {}
    for canon, aliases in raw.items():
        c = _base(canon)
        out[c] = c
        for a in aliases:
            out[_base(a)] = c
    return out


def normalize(s: str | None, aliases_path: str | None = None) -> str | None:
    b = _base(s)
    if b is None:
        return None
    return load_aliases(aliases_path).get(b, b)


def accuracy(gold: list[str], pred: list[str | None]) -> float:
    if not gold:
        return NAN
    return sum(g == p for g, p in zip(gold, pred)) / len(gold)


def macro_f1(gold: list[str], pred: list[str | None],
             exclude: frozenset[str] = frozenset()) -> float:
    classes = set(gold) - set(exclude)
    if not classes:
        return NAN
    total = 0.0
    for c in classes:
        tp = sum(g == c and p == c for g, p in zip(gold, pred))
        fp = sum(g != c and p == c for g, p in zip(gold, pred))
        fn = sum(g == c and p != c for g, p in zip(gold, pred))
        d = 2 * tp + fp + fn
        total += 2 * tp / d if d else 0.0
    return total / len(classes)


def _field(loc: Location, f: str) -> str | None:
    return normalize(getattr(loc, f))


def location_scores(gold: list[Location], pred: list[Location | None]) -> dict[str, float]:
    if not gold:
        return {k: NAN for k in ("f1", "road_acc", "landmark_acc", "direction_acc")}
    tp = fp = fn = 0
    correct = {f: 0 for f in FIELDS}
    for g, p in zip(gold, pred):
        for f in FIELDS:
            gv = _field(g, f)
            if p is None:
                fn += gv is not None
                continue
            pv = _field(p, f)
            correct[f] += gv == pv
            if pv is None:
                fn += gv is not None
            elif pv == gv:
                tp += 1
            else:
                fp += 1
                fn += gv is not None
    d = 2 * tp + fp + fn
    out = {"f1": 2 * tp / d if d else 1.0}
    for f in FIELDS:
        out[f"{f}_acc"] = correct[f] / len(gold)
    return out


def abstention_rate(gold: list[Location], pred: list[Location | None]) -> float:
    """Share of gold-null location fields correctly left null (invalid = failure).

    nan if there are no gold-null fields.
    """
    total = ok = 0
    for g, p in zip(gold, pred):
        for f in FIELDS:
            if _field(g, f) is None:
                total += 1
                ok += p is not None and _field(p, f) is None
    return ok / total if total else NAN


def bootstrap_ci(metric_on_indices: Callable[[list[int]], float], n_items: int,
                 n_boot: int = 1000, seed: int = 0) -> tuple[float, float]:
    if n_items <= 0:
        return (NAN, NAN)
    rng = random.Random(seed)
    vals = []
    for _ in range(n_boot):
        v = metric_on_indices([rng.randrange(n_items) for _ in range(n_items)])
        if v == v:
            vals.append(v)
    if not vals:
        return (NAN, NAN)
    vals.sort()
    n = len(vals)
    return (vals[min(n - 1, int(0.025 * n))], vals[min(n - 1, int(0.975 * n))])
