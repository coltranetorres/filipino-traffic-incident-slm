"""LoRA training wrapper around `mlx_lm lora`."""
from __future__ import annotations

import math
import subprocess
from pathlib import Path

from .data import write_mlx_dataset
from .schema import Record


def iters_for(n_train: int, batch_size: int, epochs: int = 3) -> int:
    return math.ceil(n_train / batch_size) * epochs


def build_command(
    model: str,
    data_dir: Path,
    adapter_dir: Path,
    iters: int,
    batch_size: int = 4,
    learning_rate: float = 1e-5,
    num_layers: int = 16,
    seed: int = 0,
    steps_per_eval: int = 25,
    max_seq_length: int = 1024,
    grad_checkpoint: bool = False,
) -> list[str]:
    cmd = [
        "uv", "run", "python", "-m", "mlx_lm", "lora",
        "--model", model, "--train", "--fine-tune-type", "lora", "--mask-prompt",
        "--data", str(data_dir), "--adapter-path", str(adapter_dir),
        "--iters", str(iters), "--batch-size", str(batch_size),
        "--learning-rate", str(learning_rate), "--num-layers", str(num_layers),
        "--val-batches", "-1", "--steps-per-eval", str(steps_per_eval),
        "--steps-per-report", "5", "--save-every", str(iters),
        "--max-seq-length", str(max_seq_length), "--seed", str(seed),
    ]
    if grad_checkpoint:
        cmd.append("--grad-checkpoint")
    return cmd


def run_training(
    model: str,
    train_records: list[Record],
    valid_records: list[Record],
    run_dir: Path,
    **hparams,
) -> Path:
    """Write the MLX dataset, then train. Returns the adapter directory."""
    run_dir = Path(run_dir)
    data_dir = run_dir / "mlx_data"
    adapter_dir = run_dir / "adapters"
    overlap = {r.id for r in train_records} & {r.id for r in valid_records}
    if overlap:
        raise ValueError(f"train/validation overlap: {sorted(overlap)[:3]}")
    write_mlx_dataset(train_records, valid_records, data_dir)
    batch_size = hparams.get("batch_size", 4)
    iters = hparams.pop("iters", None) or iters_for(len(train_records), batch_size)
    cmd = build_command(model, data_dir, adapter_dir, iters, **hparams)
    with open(run_dir / "train.log", "w", encoding="utf-8") as log:
        proc = subprocess.run(cmd, stdout=log, stderr=subprocess.STDOUT, check=False)
    if proc.returncode != 0:
        raise RuntimeError(f"training failed (rc={proc.returncode}); see {run_dir / 'train.log'}")
    return adapter_dir


ADAPTER_CONFIG_KEYS = ("mask_prompt", "fine_tune_type", "num_layers", "batch_size", "iters",
                       "learning_rate", "seed")


def finalize_lora_meta(meta: dict, adapter_dir: Path, train_cmd: list[str] | None = None) -> dict:
    """Force mode='lora' and record what mlx_lm itself wrote to adapter_config.json."""
    import json

    cfg = json.loads((Path(adapter_dir) / "adapter_config.json").read_text(encoding="utf-8"))
    out = dict(meta)
    out["mode"] = "lora"
    out["adapter_config"] = {k: cfg.get(k) for k in ADAPTER_CONFIG_KEYS}
    out["mask_prompt"] = out["adapter_config"]["mask_prompt"]
    if train_cmd is not None:
        out["train_cmd"] = train_cmd
    return out
