"""LoRA / QLoRA training on the PC's CUDA GPU (RTX 3070, 8 GB). Started by tools/pc/run.sh, inside WSL2.

  python tools/pc/train.py --model MODEL_DIR --data data/build --out RUN_DIR [--load-4bit] [--rank 64] [--alpha R]
         [--layers 0] [--targets all] [--seq 4096] [--batch 2] [--accum 8] [--lr 1e-4] [--epochs 3] [--max-steps N]
         [--eval-every 200] [--resume] [--smoke N] [--engine unsloth|hf]

Reads the chat JSONL that tools/build_data.py writes (the same files mlx_lm.lora read on the Mac). The loss is on the
assistant answer only (as `mask_prompt` on the Mac): the prompt is the chat template up to the generation prompt, and
every token after it is learned, the end-of-turn token included. --layers N puts LoRA on the last N blocks (0 = all);
--targets all is every linear layer of a block (attention and MLP).

Writes RUN_DIR/{log.jsonl,checkpoint-*/,adapter-final/,adapter-best/,result.json}. Stops on a NaN loss and when
validation loss rises at two evaluations in a row (PLAN.md 6); the final adapter is saved either way (run 1 showed the
final weights scoring better than the best-validation ones), and adapter-best is a copy of the lowest-validation
checkpoint's adapter (the final one when there was no evaluation), which run.sh eval and export use by default. --resume continues from the newest checkpoint with its optimizer,
schedule and data order. --smoke N trains N steps on the longest items and writes RUN_DIR/smoke.json (peak VRAM, tok/s).
"""

import argparse
import inspect
import json
import math
import os
import shutil
import sys
import time

ATTN = ["q_proj", "k_proj", "v_proj", "o_proj"]
MLP = ["gate_proj", "up_proj", "down_proj"]


def load_rows(path):
    with open(path, encoding="utf-8") as f:
        return [json.loads(line)["messages"] for line in f if line.strip()]


def ids_of(x):
    if isinstance(x, dict) or hasattr(x, "keys"):
        x = x["input_ids"]
    return list(x)


def encode(tok, msgs, seq):
    """Token ids and labels for one chat; None when it is longer than seq."""
    kw = {"enable_thinking": False}  # templates that do not know the flag ignore it
    prompt = ids_of(tok.apply_chat_template(msgs[:-1], add_generation_prompt=True, tokenize=True, **kw))
    full = ids_of(tok.apply_chat_template(msgs, tokenize=True, **kw))
    if len(full) > seq:
        return None
    n = 0
    while n < min(len(prompt), len(full)) and prompt[n] == full[n]:
        n += 1
    if n == len(full):
        return None
    return {"input_ids": full, "attention_mask": [1] * len(full), "labels": [-100] * n + full[n:]}


def filtered(cls, **kw):
    """Keyword arguments the installed version of cls accepts (names move between transformers releases)."""
    ok = set(inspect.signature(cls.__init__).parameters)
    if "eval_strategy" in kw and "eval_strategy" not in ok:
        kw["evaluation_strategy"] = kw.pop("eval_strategy")
    return {k: v for k, v in kw.items() if k in ok}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--model", required=True)
    ap.add_argument("--data", required=True)
    ap.add_argument("--out", required=True)
    ap.add_argument("--load-4bit", action="store_true")
    ap.add_argument("--rank", type=int, default=64)
    ap.add_argument("--alpha", type=int, default=0, help="default: equal to the rank")
    ap.add_argument("--dropout", type=float, default=0.0)
    ap.add_argument("--layers", type=int, default=0)
    ap.add_argument("--targets", default="all")
    ap.add_argument("--seq", type=int, default=4096)
    ap.add_argument("--batch", type=int, default=2)
    ap.add_argument("--accum", type=int, default=8)
    ap.add_argument("--lr", type=float, default=1e-4)
    ap.add_argument("--epochs", type=float, default=3)
    ap.add_argument("--max-steps", type=int, default=-1)
    ap.add_argument("--warmup", type=int, default=100, help="warm-up optimizer steps (run 2 on the Mac: 19 was too few)")
    ap.add_argument("--eval-every", type=int, default=200)
    ap.add_argument("--val-items", type=int, default=400)
    ap.add_argument("--seed", type=int, default=0)
    ap.add_argument("--resume", action="store_true")
    ap.add_argument("--smoke", type=int, default=0)
    ap.add_argument("--engine", default="unsloth", choices=["unsloth", "hf"])
    args = ap.parse_args()
    os.makedirs(args.out, exist_ok=True)

    if args.engine == "unsloth":
        import unsloth  # noqa: F401  (must come before transformers to patch it)
        from unsloth import FastLanguageModel
    import torch
    from datasets import Dataset
    from transformers import (AutoModelForCausalLM, AutoTokenizer, DataCollatorForSeq2Seq, Trainer, TrainerCallback,
                              TrainingArguments)

    assert torch.cuda.is_available(), "no CUDA GPU"
    torch.manual_seed(args.seed)
    targets = {"all": ATTN + MLP, "attn": ATTN}.get(args.targets, args.targets.split(","))
    alpha = args.alpha or args.rank

    if args.engine == "unsloth":
        model, tok = FastLanguageModel.from_pretrained(model_name=args.model, max_seq_length=args.seq, dtype=torch.bfloat16,
                                                       load_in_4bit=args.load_4bit)
        n_layers = model.config.num_hidden_layers
        layers = list(range(n_layers - args.layers, n_layers)) if args.layers else None
        model = FastLanguageModel.get_peft_model(model, r=args.rank, lora_alpha=alpha, lora_dropout=args.dropout,
                                                 target_modules=targets, layers_to_transform=layers, bias="none",
                                                 use_gradient_checkpointing="unsloth", random_state=args.seed)
    else:
        from peft import LoraConfig, get_peft_model, prepare_model_for_kbit_training
        q = None
        if args.load_4bit:
            from transformers import BitsAndBytesConfig
            q = BitsAndBytesConfig(load_in_4bit=True, bnb_4bit_quant_type="nf4", bnb_4bit_use_double_quant=True,
                                   bnb_4bit_compute_dtype=torch.bfloat16)
        tok = AutoTokenizer.from_pretrained(args.model)
        model = AutoModelForCausalLM.from_pretrained(args.model, torch_dtype=torch.bfloat16, quantization_config=q,
                                                     device_map={"": 0}, attn_implementation="sdpa")
        if q:
            model = prepare_model_for_kbit_training(model, use_gradient_checkpointing=True)
        else:
            model.gradient_checkpointing_enable(gradient_checkpointing_kwargs={"use_reentrant": False})
            model.enable_input_require_grads()
        n_layers = model.config.num_hidden_layers
        layers = list(range(n_layers - args.layers, n_layers)) if args.layers else None
        model = get_peft_model(model, LoraConfig(r=args.rank, lora_alpha=alpha, lora_dropout=args.dropout,
                                                 target_modules=targets, layers_to_transform=layers,
                                                 task_type="CAUSAL_LM"))
    if tok.pad_token is None:
        tok.pad_token = tok.eos_token
    trainable = sum(p.numel() for p in model.parameters() if p.requires_grad)
    print("trainable parameters: {:,}; LoRA on {} of {} blocks".format(trainable, args.layers or n_layers, n_layers),
          flush=True)

    def build(rows):
        out, skipped = [], 0
        for m in rows:
            e = encode(tok, m, args.seq)
            if e is None:
                skipped += 1
            else:
                out.append(e)
        return out, skipped

    train_rows = load_rows(os.path.join(args.data, "train.jsonl"))
    if args.smoke:
        # The longest items that fit: the worst case for memory.
        enc, _ = build(train_rows)
        enc.sort(key=lambda e: -len(e["input_ids"]))
        train, skipped = enc[:args.smoke * args.batch * args.accum], 0
        valid = []
    else:
        train, skipped = build(train_rows)
        valid, _ = build(load_rows(os.path.join(args.data, "valid.jsonl"))[:args.val_items])
    tokens = sum(len(e["input_ids"]) for e in train)
    print("train items {} ({} longer than {} skipped), {:,} tokens; valid items {}".format(
        len(train), skipped, args.seq, tokens, len(valid)), flush=True)
    train_ds = Dataset.from_list(train)
    valid_ds = Dataset.from_list(valid) if valid else None

    log_path = os.path.join(args.out, "log.jsonl")

    class Guard(TrainerCallback):
        def __init__(self):
            self.vals = []
            self.why = ""

        def on_log(self, a, state, control, logs=None, **kw):
            logs = dict(logs or {})
            logs["step"] = state.global_step
            logs["peak_gb"] = round(torch.cuda.max_memory_reserved() / 2**30, 2)
            with open(log_path, "a") as f:
                f.write(json.dumps(logs) + "\n")
            loss = logs.get("loss")
            if loss is not None and (math.isnan(loss) or math.isinf(loss)):
                self.why = "train loss is NaN"
                control.should_training_stop = True
            if "eval_loss" in logs:
                self.vals.append(logs["eval_loss"])
                v = self.vals
                if len(v) >= 3 and v[-1] > v[-2] > v[-3]:
                    self.why = "validation loss rose at two evaluations in a row"
                    control.should_training_stop = True
            return control

    guard = Guard()
    targs = TrainingArguments(**filtered(
        TrainingArguments,
        output_dir=args.out,
        per_device_train_batch_size=args.batch,
        per_device_eval_batch_size=args.batch,
        gradient_accumulation_steps=args.accum,
        learning_rate=args.lr,
        lr_scheduler_type="cosine",
        warmup_steps=0 if args.smoke else args.warmup,
        num_train_epochs=1 if args.smoke else args.epochs,
        max_steps=args.smoke or args.max_steps,
        weight_decay=0.0,
        max_grad_norm=1.0,
        optim="adamw_8bit",
        bf16=True,
        logging_steps=1 if args.smoke else 10,
        eval_strategy="no" if args.smoke else "steps",
        eval_steps=args.eval_every,
        save_strategy="no" if args.smoke else "steps",
        save_steps=args.eval_every,
        save_total_limit=4,
        metric_for_best_model="eval_loss",
        greater_is_better=False,
        group_by_length=not args.smoke,  # batches of similar length: little padding
        dataloader_num_workers=2,
        seed=args.seed,
        data_seed=args.seed,
        report_to="none",
        remove_unused_columns=False,
        gradient_checkpointing=args.engine == "hf",
        gradient_checkpointing_kwargs={"use_reentrant": False},
    ))
    collator = DataCollatorForSeq2Seq(tok, padding=True, pad_to_multiple_of=8, label_pad_token_id=-100)
    trainer = Trainer(**filtered(Trainer, model=model, args=targs, train_dataset=train_ds, eval_dataset=valid_ds,
                                 data_collator=collator, callbacks=[guard], processing_class=tok, tokenizer=tok))

    torch.cuda.reset_peak_memory_stats()
    t0 = time.time()
    resume = args.resume and any(d.startswith("checkpoint-") for d in os.listdir(args.out))
    trainer.train(resume_from_checkpoint=True if resume else None)
    secs = time.time() - t0
    peak = torch.cuda.max_memory_reserved() / 2**30

    if args.smoke:
        s = {"peak_gb": round(peak, 2), "tok_per_s": round(tokens / secs, 1), "steps": args.smoke,
             "batch": args.batch, "seq": args.seq, "rank": args.rank, "items": len(train), "tokens": tokens}
        json.dump(s, open(os.path.join(args.out, "smoke.json"), "w"), indent=1)
        print("smoke: peak {:.2f} GB, {:.0f} tok/s".format(peak, tokens / secs))
        return

    final = os.path.join(args.out, "adapter-final")
    model.save_pretrained(final)
    tok.save_pretrained(final)
    # adapter-best: the lowest-validation checkpoint's adapter (checkpoints rotate away; this copy stays).
    best_dir = os.path.join(args.out, "adapter-best")
    src = trainer.state.best_model_checkpoint
    src = src if src and os.path.isdir(src) else final
    shutil.rmtree(best_dir, ignore_errors=True)
    os.makedirs(best_dir)
    for name in os.listdir(src):
        if name.startswith("adapter_"):
            shutil.copy2(os.path.join(src, name), best_dir)
    tok.save_pretrained(best_dir)
    vals = [round(v, 4) for v in guard.vals]
    result = {"stopped": guard.why or "finished", "steps": trainer.state.global_step, "hours": round(secs / 3600, 2),
              "peak_gb": round(peak, 2), "val": vals, "best_val": min(vals) if vals else None,
              "best_checkpoint": trainer.state.best_model_checkpoint, "adapter_best_from": src, "train_items": len(train),
              "train_tokens": tokens, "epochs_done": round(trainer.state.epoch or 0, 3)}
    json.dump(result, open(os.path.join(args.out, "result.json"), "w"), indent=1)
    with open(os.path.join(args.out, "summary.txt"), "a") as f:
        f.write("result: " + json.dumps(result) + "\n")
    print(json.dumps(result, indent=1))


if __name__ == "__main__":
    sys.exit(main())
