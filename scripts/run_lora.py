"""LoRA data-size sweep, evaluated on VALIDATION. One subprocess per step.

Usage: uv run python scripts/run_lora.py train <run> | eval <run> | table
"""
from __future__ import annotations

import json
import re
import subprocess
import sys
import time
from pathlib import Path

from trafficslm.runs import MAX_TOKENS

OUT = Path("experiments")
MODELS = json.loads((OUT / "models.json").read_text())
RUNS = {
    "gemma3-1b-lora-n50": ("gemma3-1b", 50),
    "gemma3-1b-lora-n100": ("gemma3-1b", 100),
    "gemma3-1b-lora-n207": ("gemma3-1b", 207),
    "qwen2.5-1.5b-lora-n207": ("qwen2.5-1.5b", 207),
    "gemma3-1b-4bit-lora-n207": ("gemma3-1b-4bit", 207),
}
HP = dict(batch_size=4, learning_rate=1e-5, num_layers=16, seed=0)


def do_train(name: str) -> None:
    from trafficslm.data import load_split, stratified_subset
    from trafficslm.train import iters_for, run_training

    key, n = RUNS[name]
    run = OUT / name
    run.mkdir(parents=True, exist_ok=True)
    train = stratified_subset(load_split("train"), n, seed=0)
    valid = load_split("validation")
    iters = iters_for(len(train), HP["batch_size"])
    t0 = time.perf_counter()
    from trafficslm.train import build_command

    train_cmd = build_command(MODELS[key], run / "mlx_data", run / "adapters", iters, **HP)
    run_training(MODELS[key], train, valid, run, iters=iters, **HP)
    wall = time.perf_counter() - t0
    import resource

    log = re.sub(r"\x1b\[[0-9;]*m", "", (run / "train.log").read_text())
    trains = [(int(a), float(b)) for a, b in re.findall(r"^\s*(\d+)\s+(\d+\.\d+)\s*[▼▲=]?\s+\d+\s", log, re.M)]
    vals = [(int(a), float(b)) for a, b in re.findall(r"^\s*(\d+)\s+val\s+(\d+\.\d+)", log, re.M)]
    # max RSS of the training child process (one process per run); bytes on macOS
    peak = [resource.getrusage(resource.RUSAGE_CHILDREN).ru_maxrss / 1e9]
    meta = {
        "model": MODELS[key], "adapter": str(run / "adapters"), "mode": "lora",
        "n_train": len(train), "iters": iters, "epochs": 3, "train_cmd": train_cmd,
        "max_seq_length": 1024, "steps_per_eval": 25, **HP,
        "training_wall_s": round(wall, 1),
        "train_loss_curve": trains, "val_loss_curve": vals,
        "final_train_loss": trains[-1][1] if trains else None,
        "final_val_loss": vals[-1][1] if vals else None,
        "train_peak_rss_gb": round(peak[0], 2),
    }
    (run / "meta_train.json").write_text(json.dumps(meta, indent=2))


def do_eval(name: str) -> None:
    from trafficslm.data import load_split
    from trafficslm.evaluate import main as evaluate_main
    from trafficslm.infer import mlx_generator, run_predictions

    run = OUT / name
    tm = json.loads((run / "meta_train.json").read_text())
    records = load_split("validation")
    gen = mlx_generator(tm["model"], adapter_path=tm["adapter"], max_tokens=MAX_TOKENS)
    run_predictions(records, gen, run, shots=(),
                    meta={**tm, "max_tokens": MAX_TOKENS, "split": "validation", "decoding": "greedy"})
    from trafficslm.train import finalize_lora_meta

    meta_path = run / "meta.json"
    meta_path.write_text(json.dumps(
        finalize_lora_meta(json.loads(meta_path.read_text()), tm["adapter"], tm.get("train_cmd")),
        indent=2, ensure_ascii=False), encoding="utf-8")
    (run / "meta_train.json").unlink()
    evaluate_main(["--run", str(run), "--split", "validation"])


def do_table() -> None:
    from trafficslm.tables import build_table

    runs = {}
    for name in ["gemma3-1b-zeroshot", "gemma3-1b-fewshot", "qwen2.5-1.5b-zeroshot",
                 "qwen2.5-1.5b-fewshot", *RUNS]:
        r = OUT / name
        runs[name] = (json.loads((r / "results.json").read_text()), json.loads((r / "meta.json").read_text()))
    (OUT / "lora_validation.md").write_text(
        "# LoRA vs baselines on validation (n=40), value [95% CI]\n\n" + build_table(runs), encoding="utf-8")


def do_fixmeta() -> None:
    """Regenerate meta.json for existing runs (no retraining / inference)."""
    from trafficslm.train import build_command, finalize_lora_meta

    for name, (key, _) in RUNS.items():
        run = OUT / name
        m = json.loads((run / "meta.json").read_text())
        cmd = build_command(MODELS[key], run / "mlx_data", run / "adapters", m["iters"],
                            **{k: m[k] for k in HP})
        m.pop("mask_prompt", None)
        m = finalize_lora_meta(m, run / "adapters", cmd)
        (run / "meta.json").write_text(json.dumps(m, indent=2, ensure_ascii=False), encoding="utf-8")


if __name__ == "__main__":
    cmd = sys.argv[1]
    if cmd == "train":
        do_train(sys.argv[2])
    elif cmd == "eval":
        do_eval(sys.argv[2])
    elif cmd == "fixmeta":
        do_fixmeta()
    elif cmd == "table":
        do_table()
