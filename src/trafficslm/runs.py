"""Run configuration shared by the scripts."""

MAX_TOKENS = 200
# The nine configurations declared in research/selection.md, in the order used by the findings tables.
TEST_RUNS = [
    "gemma3-1b-zeroshot", "gemma3-1b-fewshot", "gemma3-1b-lora-n50", "gemma3-1b-lora-n100",
    "gemma3-1b-lora-n207", "gemma3-1b-4bit-lora-n207",
    "qwen2.5-1.5b-zeroshot", "qwen2.5-1.5b-fewshot", "qwen2.5-1.5b-lora-n207",
]
# Runs for which results/errors_<run>.md is generated.
ERROR_REPORT_RUNS = [
    "gemma3-1b-lora-n207", "gemma3-1b-4bit-lora-n207",
    "qwen2.5-1.5b-fewshot", "qwen2.5-1.5b-lora-n207",
]
