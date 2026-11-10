"""Generate TEST-split predictions for the nine configurations declared in research/selection.md.

Each run executes in its own subprocess (per-run peak memory). Only text/id of test items are used here;
scoring is a separate step: uv run python -m trafficslm.evaluate --run experiments/<run> --split test --final

Usage: uv run python scripts/run_test.py all | one <run>
"""
from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

from trafficslm.runs import MAX_TOKENS, TEST_RUNS

OUT = Path("experiments")
RUNS = TEST_RUNS


def do_one(name: str) -> None:
    from trafficslm.data import load_split, verify_manifest
    from trafficslm.infer import mlx_generator, run_predictions

    verify_manifest()
    run = OUT / name
    vm = json.loads((run / "meta.json").read_text(encoding="utf-8"))
    records = load_split("test")
    train = {r.id: r for r in load_split("train")}
    shots = tuple(train[i] for i in vm.get("shot_ids") or [])
    try:
        import mlx.core as mx
        mx.reset_peak_memory()
    except Exception:
        pass
    gen = mlx_generator(vm["model"], adapter_path=vm.get("adapter"), max_tokens=MAX_TOKENS)
    run_predictions(records, gen, run, shots=shots,
                    meta={"model": vm["model"], "adapter": vm.get("adapter"), "max_tokens": MAX_TOKENS,
                          "split": "test", "decoding": "greedy",
                          **({"n_train": vm["n_train"]} if "n_train" in vm else {})},
                    pred_name="predictions_test.jsonl", meta_name="meta_test.json")
    mt = json.loads((run / "meta_test.json").read_text(encoding="utf-8"))
    mt["mode"] = vm["mode"]  # keep the validation run's mode label (e.g. "lora")
    (run / "meta_test.json").write_text(json.dumps(mt, indent=2, ensure_ascii=False), encoding="utf-8")


def main() -> None:
    cmd = sys.argv[1]
    if cmd == "one":
        do_one(sys.argv[2])
    elif cmd == "all":
        for name in (sys.argv[2:] or RUNS):
            print(f"== {name}", flush=True)
            subprocess.run([sys.executable, __file__, "one", name], check=True)
    else:
        raise SystemExit(__doc__)


if __name__ == "__main__":
    main()
