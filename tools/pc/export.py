"""Merge a LoRA adapter into its base weights for deployment (tools/pc/run.sh export).

  python tools/pc/export.py --model MODEL_DIR --adapter RUN/adapter-best --out OUT/merged

The base is loaded in bf16 on the CPU (a 4-bit QLoRA adapter is merged into the full-precision base, not the 4-bit
one), so the big model needs about twice its parameter count in GB of WSL memory. The merged folder is a plain
safetensors model: tools/import_mlx.sh turns it into a 4-bit MLX model on the Mac, and run.sh export turns it into GGUF.
"""

import argparse
import os

import torch
from peft import PeftModel
from transformers import AutoModelForCausalLM, AutoTokenizer


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--model", required=True)
    ap.add_argument("--adapter", required=True)
    ap.add_argument("--out", required=True)
    args = ap.parse_args()
    base = AutoModelForCausalLM.from_pretrained(args.model, torch_dtype=torch.bfloat16, device_map={"": "cpu"},
                                                low_cpu_mem_usage=True)
    model = PeftModel.from_pretrained(base, args.adapter).merge_and_unload()
    model.save_pretrained(args.out, safe_serialization=True, max_shard_size="2GB")
    # Checkpoint folders of older runs may carry no tokenizer; the base model's is the same one.
    has_tok = os.path.isfile(os.path.join(args.adapter, "tokenizer_config.json"))
    AutoTokenizer.from_pretrained(args.adapter if has_tok else args.model).save_pretrained(args.out)
    print("merged:", args.out)


if __name__ == "__main__":
    main()
