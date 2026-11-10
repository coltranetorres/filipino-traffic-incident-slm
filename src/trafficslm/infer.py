"""Prediction runner and greedy MLX generator."""
from __future__ import annotations

import json
import statistics
import time
from collections.abc import Callable, Sequence
from pathlib import Path

from .prompts import build_messages
from .schema import Record

Generator = Callable[[list[dict]], str]


def mlx_generator(model_id: str, adapter_path: str | None = None, max_tokens: int = 200) -> Generator:
    """Load once; return a greedy generator bounded by max_tokens.

    The chat template is applied via the tokenizer. Gemma's template accepts a
    `system` role by folding it into the first user turn itself; for any
    template that rejects `system`, we fold it into the first user turn here.
    """
    from mlx_lm import generate, load  # lazy: keep model loading out of import time

    model, tokenizer = load(model_id, adapter_path=adapter_path)

    # Gemma's end-of-turn token is not its default EOS; without this the model
    # keeps generating past the turn until max_tokens. Register turn enders as EOS.
    for tok in ("<end_of_turn>", "<|im_end|>"):
        if tokenizer.convert_tokens_to_ids(tok) not in (None, tokenizer.unk_token_id):
            tokenizer.add_eos_token(tok)

    def _prompt(messages: list[dict]) -> str:
        try:
            return tokenizer.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)
        except Exception:
            if not messages or messages[0]["role"] != "system":
                raise
            rest = [dict(m) for m in messages[1:]]
            rest[0]["content"] = messages[0]["content"] + "\n\n" + rest[0]["content"]
            return tokenizer.apply_chat_template(rest, tokenize=False, add_generation_prompt=True)

    def gen(messages: list[dict]) -> str:
        # Template text already contains BOS; avoid adding a second one.
        ids = tokenizer.encode(_prompt(messages), add_special_tokens=False)
        # No sampler => greedy argmax. max_tokens bounds runaway generations.
        return generate(model, tokenizer, prompt=ids, max_tokens=max_tokens, verbose=False)

    return gen


def _peak_memory_gb() -> float | None:
    try:
        import mlx.core as mx
        fn = getattr(mx, "get_peak_memory", None) or getattr(mx.metal, "get_peak_memory", None)
        return round(fn() / 1e9, 3) if fn else None
    except Exception:
        return None


def run_predictions(
    records: list[Record],
    generator: Generator,
    out_dir: Path,
    shots: Sequence[Record] = (),
    meta: dict | None = None,
    pred_name: str = "predictions.jsonl",
    meta_name: str = "meta.json",
) -> Path:
    out_dir = Path(out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)
    pred_path = out_dir / pred_name
    latencies: list[float] = []
    with open(pred_path, "w", encoding="utf-8") as f:
        for r in records:
            row: dict = {"id": r.id}
            t0 = time.perf_counter()
            try:
                row["raw"] = generator(build_messages(r.text, shots))
            except Exception as e:  # one bad item must not abort the run
                row["raw"] = ""
                row["error"] = f"{type(e).__name__}: {e}"
            ms = max((time.perf_counter() - t0) * 1000, 1e-6)
            row["latency_ms"] = ms
            latencies.append(ms)
            f.write(json.dumps(row, ensure_ascii=False) + "\n")
            f.flush()
    meta = dict(meta or {})
    meta.setdefault("model", None)
    meta.setdefault("adapter", None)
    meta["mode"] = "few-shot" if shots else "zero-shot"
    meta["shot_ids"] = [s.id for s in shots]
    meta["n"] = len(records)
    meta["latency_ms_mean"] = statistics.fmean(latencies) if latencies else None
    meta["latency_ms_median"] = statistics.median(latencies) if latencies else None
    meta["peak_memory_gb"] = _peak_memory_gb()
    (out_dir / meta_name).write_text(json.dumps(meta, indent=2, ensure_ascii=False), encoding="utf-8")
    return pred_path
