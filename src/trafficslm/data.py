"""Dataset loading, integrity checks, sampling and MLX export."""
from __future__ import annotations

import hashlib
import json
import random
from collections import defaultdict
from pathlib import Path

from .prompts import SYSTEM_PROMPT, build_messages, target_json
from .schema import Record

__all__ = [
    "load_split", "verify_manifest", "stratified_subset", "pick_shots",
    "write_mlx_dataset", "target_json", "build_messages", "SYSTEM_PROMPT",
]

DEFAULT_ROOT = Path("data/processed")


def load_split(name: str, root: Path = DEFAULT_ROOT) -> list[Record]:
    with open(Path(root) / f"{name}.jsonl", encoding="utf-8") as f:
        return [Record.model_validate_json(line) for line in f if line.strip()]


def verify_manifest(root: Path = DEFAULT_ROOT) -> None:
    root = Path(root)
    manifest = json.loads((root / "MANIFEST.json").read_text(encoding="utf-8"))
    for split, meta in manifest.items():
        data = (root / f"{split}.jsonl").read_bytes()
        digest = hashlib.sha256(data).hexdigest()
        if digest != meta["sha256"]:
            raise ValueError(f"{split}: sha256 mismatch ({digest} != {meta['sha256']})")
        count = sum(1 for line in data.decode("utf-8").splitlines() if line.strip())
        if count != meta["count"]:
            raise ValueError(f"{split}: count mismatch ({count} != {meta['count']})")


def _by_class(records: list[Record]) -> dict[str, list[Record]]:
    groups: dict[str, list[Record]] = defaultdict(list)
    for r in records:
        groups[r.incident_type].append(r)
    return groups


def stratified_subset(records: list[Record], n: int, seed: int = 0) -> list[Record]:
    """Deterministic class-balanced subset (round-robin over incident types)."""
    rng = random.Random(seed)
    groups = _by_class(records)
    pools = {}
    for c in sorted(groups):
        pool = list(groups[c])
        rng.shuffle(pool)
        pools[c] = pool
    out: list[Record] = []
    while len(out) < min(n, len(records)):
        for c in sorted(pools):
            if pools[c] and len(out) < n:
                out.append(pools[c].pop())
    return out


def pick_shots(train: list[Record], k: int = 5, seed: int = 0) -> list[Record]:
    """k few-shot examples with distinct incident types, from train only."""
    rng = random.Random(seed)
    groups = _by_class(train)
    classes = sorted(groups)
    if k > len(classes):
        raise ValueError("k exceeds number of distinct incident types")
    chosen = rng.sample(classes, k)
    return [rng.choice(groups[c]) for c in chosen]


def write_mlx_dataset(train: list[Record], valid: list[Record], out_dir: Path) -> None:
    out_dir = Path(out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)
    for name, recs in (("train", train), ("valid", valid)):
        with open(out_dir / f"{name}.jsonl", "w", encoding="utf-8") as f:
            for r in recs:
                msgs = build_messages(r.text) + [{"role": "assistant", "content": target_json(r)}]
                f.write(json.dumps({"messages": msgs}, ensure_ascii=False) + "\n")
