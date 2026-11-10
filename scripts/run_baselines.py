"""Zero-shot and few-shot baselines on the VALIDATION split.

Usage: uv run python scripts/run_baselines.py [--out experiments]
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

from trafficslm.runs import MAX_TOKENS
from trafficslm.tables import build_table, fmt_entry, fmt_num  # noqa: F401  (re-exported)

MODELS = {
    "gemma3-1b": "mlx-community/gemma-3-1b-it-bf16",
    "qwen2.5-1.5b": "mlx-community/Qwen2.5-1.5B-Instruct-bf16",
}
SPLIT = "validation"
K_SHOTS = 5


def merge_models(path: Path, models: dict[str, str]) -> dict[str, str]:
    """Write `models` into the JSON file at `path`, keeping any other keys already there."""
    path = Path(path)
    cur = json.loads(path.read_text(encoding="utf-8")) if path.exists() else {}
    cur.update(models)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(cur, indent=2) + "\n", encoding="utf-8")
    return cur


def main(argv: list[str] | None = None) -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", default="experiments")
    a = ap.parse_args(argv)
    out = Path(a.out)
    out.mkdir(parents=True, exist_ok=True)
    merge_models(out / "models.json", MODELS)

    from trafficslm.data import load_split, pick_shots
    from trafficslm.evaluate import main as evaluate_main
    from trafficslm.infer import mlx_generator, run_predictions

    records = load_split(SPLIT)
    shots = pick_shots(load_split("train"), k=K_SHOTS, seed=0)
    runs = {}
    for key, repo in MODELS.items():
        gen = mlx_generator(repo, max_tokens=MAX_TOKENS)
        for mode, s in (("zeroshot", ()), ("fewshot", shots)):
            name = f"{key}-{mode}"
            run = out / name
            try:
                import mlx.core as mx
                mx.reset_peak_memory()
            except Exception:
                pass
            run_predictions(records, gen, run, shots=s,
                            meta={"model": repo, "adapter": None, "max_tokens": MAX_TOKENS,
                                  "split": SPLIT, "decoding": "greedy"})
            evaluate_main(["--run", str(run), "--split", SPLIT])
            runs[name] = (json.loads((run / "results.json").read_text()),
                          json.loads((run / "meta.json").read_text()))
        del gen
    (out / "baselines_validation.md").write_text(
        f"# Baselines on validation (n={len(records)}), value [95% CI]\n\n" + build_table(runs),
        encoding="utf-8")


if __name__ == "__main__":
    main()
