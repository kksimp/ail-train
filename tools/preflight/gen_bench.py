"""M1 preflight: inference speed and memory for one candidate base, untrained, with the core card as system prompt.

Usage: python gen_bench.py MODEL_DIR CARD OUT_JSON
Writes prompt and generation tokens per second, peak memory, and the untrained base's answer to one small task
(a first look at the arm A baseline; not an eval).
"""

import json
import sys

import mlx.core as mx
from mlx_lm import load, stream_generate
from mlx_lm.sample_utils import make_sampler

TASK = (
    "Write an AIL program whose main prints the sum of the squares of the integers 1 to 10, "
    "with one @test for the helper function."
)


def peak():
    f = getattr(mx, "get_peak_memory", None) or mx.metal.get_peak_memory
    return f()


def main():
    model_dir, card_path, out_path = sys.argv[1:4]
    with open(card_path, encoding="utf-8") as f:
        card = f.read()
    model, tok = load(model_dir)
    msgs = [{"role": "system", "content": card}, {"role": "user", "content": TASK}]
    prompt = tok.apply_chat_template(msgs, add_generation_prompt=True)
    text, last = "", None
    for r in stream_generate(model, tok, prompt, max_tokens=256, sampler=make_sampler(temp=0.0)):
        text += r.text
        last = r
    out = {
        "prompt_tokens": last.prompt_tokens,
        "prompt_tps": round(last.prompt_tps, 1),
        "generation_tokens": last.generation_tokens,
        "generation_tps": round(last.generation_tps, 1),
        "peak_memory_gb": round(last.peak_memory, 3),
        "mlx_peak_gb": round(peak() / 1e9, 3),
        "answer": text,
    }
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(out, f, indent=2)
    print(json.dumps({k: v for k, v in out.items() if k != "answer"}))


if __name__ == "__main__":
    main()
