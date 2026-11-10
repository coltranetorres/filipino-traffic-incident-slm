"""Smoke check: 3 validation items, few-shot optional. Usage: uv run python scripts/smoke_infer.py OUT_DIR [model_id]"""
import sys
from pathlib import Path

from trafficslm.data import load_split, pick_shots
from trafficslm.infer import mlx_generator, run_predictions

out = Path(sys.argv[1])
model = sys.argv[2] if len(sys.argv) > 2 else "mlx-community/gemma-3-1b-it-bf16"
recs = load_split("validation")[:3]
gen = mlx_generator(model, max_tokens=200)
shots = pick_shots(load_split("train"), k=5) if "--few" in sys.argv else ()
p = run_predictions(recs, gen, out, shots=shots, meta={"model": model, "adapter": None})
print(p.read_text()); print((out / "meta.json").read_text())
