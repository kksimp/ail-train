"""Arm B of the quick eval: the same items, model and sampling as tools/eval_quick.py (arm A, one shot), plus up to
--rounds compiler-assisted correction rounds.

Usage: python tools/eval_loop.py --ail AIL_ROOT --model MODEL_DIR [--adapter ADAPTER_DIR] --out OUT_DIR
                                 [--rounds 3] [--samples 3] [--temp 0.2] [--max-tokens 1536] [--limit N] [--load-4bit]

For every item, --samples first answers are drawn exactly as in arm A (same prompt, seed and sampler). Each answer is
then handled on its own: its program goes through `ail check`; while the check fails and rounds are left, the model
gets one new message holding the task, its current complete program, the exact `ail check` output and the number of
rounds left, and answers with a whole revised program. The model never sees the expected output, the reference, a test
or any documentation, and it gets no tool but this compiler check. A program that passes the check ends the loop
(runtime failures are not fed back). The last program then goes through `ail check` and `ail run` and passes when it
prints exactly what the reference program prints, as in arm A.

Writes OUT/revisions.jsonl (one line per sample: every revision's text, program, check output, tokens and seconds),
OUT/summary.json and a table per family. Round 0 alone is arm A rerun in the same process, so the two arms are paired.
CUDA only (transformers + peft), like `tools/pc/run.sh eval`.
"""

import argparse
import json
import os
import re
import sys
import time

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from eval_quick import ROOT, code_of, compile_and_run, family, program_for, read  # noqa: E402

CODE = re.compile(r"\b(?:error|warning)\[([A-Za-z0-9_.\-]+)\]")
FAMILIES = ["fixline", "fix", "cursor", "complete", "function", "port", "write"]
MAX_DIAG = 6000  # characters of `ail check` output passed back; longer output keeps its head (the first errors)


def codes(check_output):
    """The diagnostic rule IDs in a check output, or its first line when it names none."""
    found = sorted(set(CODE.findall(check_output)))
    if found:
        return found
    first = check_output.strip().split("\n")[0][:120]
    return [first] if first else []


def correction_prompt(task, source, diag, rounds_left_after):
    if len(diag) > MAX_DIAG:
        diag = diag[:MAX_DIAG] + "\n[... compiler output cut ...]"
    left = ("This is your last correction round." if rounds_left_after == 0 else
            "After this one you have {} correction round{} left.".format(rounds_left_after,
                                                                         "" if rounds_left_after == 1 else "s"))
    return ("Your earlier answer to this task does not pass `ail check`.\n\n"
            "The task:\n\n" + task.rstrip() + "\n\n"
            "Your current complete program:\n\n```ail\n" + source.rstrip("\n") + "\n```\n\n"
            "`ail check` output:\n\n```\n" + diag.rstrip("\n") + "\n```\n\n"
            "Fix these errors while keeping the program's intended behaviour. " + left + "\n"
            "Answer with the whole corrected program in one ```ail block.")


def check_only(ail, src):
    """`ail check` alone: (ok, output). Uses compile_and_run's check, so the flags and environment match arm A."""
    import shutil
    import subprocess
    import tempfile
    tmp = tempfile.mkdtemp(prefix="ailb-")
    try:
        with open(os.path.join(tmp, "main.ail"), "w", encoding="utf-8") as f:
            f.write(src)
        env = dict(os.environ, AIL_FIX="0")
        try:
            c = subprocess.run([ail, "check", "--no-fix", "main.ail"], cwd=tmp, capture_output=True, text=True,
                               env=env, timeout=120)
        except subprocess.TimeoutExpired:
            return False, "ail check timed out after 120 s"
        return c.returncode == 0, (c.stdout + c.stderr)
    finally:
        shutil.rmtree(tmp, ignore_errors=True)


def hf_model(args):
    import torch
    from transformers import AutoModelForCausalLM, AutoTokenizer

    q = None
    if args.load_4bit:
        from transformers import BitsAndBytesConfig
        q = BitsAndBytesConfig(load_in_4bit=True, bnb_4bit_quant_type="nf4", bnb_4bit_use_double_quant=True,
                               bnb_4bit_compute_dtype=torch.bfloat16)
    tok = AutoTokenizer.from_pretrained(args.model)
    model = AutoModelForCausalLM.from_pretrained(args.model, torch_dtype=torch.bfloat16, quantization_config=q,
                                                 device_map={"": 0})
    if args.adapter:
        from peft import PeftModel
        model = PeftModel.from_pretrained(model, args.adapter)
    model.eval()

    def gen(msgs, seed, n):
        """n samples of one prompt: (texts, prompt tokens, generated tokens per sample, seconds)."""
        t = time.time()
        ids = tok.apply_chat_template(msgs, add_generation_prompt=True, return_tensors="pt", enable_thinking=False)
        if not torch.is_tensor(ids):
            ids = ids["input_ids"]
        ids = ids.to(model.device)
        torch.manual_seed(seed)
        with torch.no_grad():
            out = model.generate(ids, attention_mask=torch.ones_like(ids), do_sample=args.temp > 0,
                                 temperature=args.temp or None, top_p=1.0, max_new_tokens=args.max_tokens,
                                 num_return_sequences=n, pad_token_id=tok.pad_token_id or tok.eos_token_id)
        stop = model.generation_config.eos_token_id
        stop = set(stop if isinstance(stop, list) else [stop]) | {tok.eos_token_id, tok.pad_token_id}
        texts, lens = [], []
        for o in out:
            new = o[ids.shape[1]:].tolist()
            ends = [k for k, t in enumerate(new) if t in stop]
            lens.append(ends[0] + 1 if ends else len(new))  # generated tokens, the end token included
            texts.append(tok.decode(o[ids.shape[1]:], skip_special_tokens=True))
        return texts, ids.shape[1], lens, time.time() - t
    return gen


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--ail", required=True)
    ap.add_argument("--model", required=True)
    ap.add_argument("--adapter", default="")
    ap.add_argument("--data", default=os.path.join(ROOT, "data", "build", "quick-eval.jsonl"))
    ap.add_argument("--out", required=True)
    ap.add_argument("--rounds", type=int, default=3)
    ap.add_argument("--samples", type=int, default=3)
    ap.add_argument("--temp", type=float, default=0.2)
    ap.add_argument("--max-tokens", type=int, default=1536)
    ap.add_argument("--limit", type=int, default=0)
    ap.add_argument("--families", default="", help="comma list; default every family")
    ap.add_argument("--load-4bit", action="store_true")
    ap.add_argument("--resume", action="store_true",
                    help="keep the items OUT/revisions.jsonl already holds in full and continue after them")
    args = ap.parse_args()

    ail = os.path.join(os.path.abspath(args.ail), "ail")
    system = read(os.path.join(ROOT, "tools", "preflight", "short-system.txt")).strip()
    rows = [json.loads(l) for l in open(args.data, encoding="utf-8")]
    if args.limit:
        rows = rows[:args.limit]
    only = set(f for f in args.families.split(",") if f)
    gen = hf_model(args)
    os.makedirs(args.out, exist_ok=True)

    samples = []
    t_all = time.time()
    rpath = os.path.join(args.out, "revisions.jsonl")
    done = {}  # --resume: item -> its records, for items with every sample written
    if args.resume and os.path.isfile(rpath):
        for line in open(rpath, encoding="utf-8"):
            try:
                rec = json.loads(line)
            except ValueError:
                break
            done.setdefault(rec["i"], []).append(rec)
        done = {i: v for i, v in done.items() if len(v) == args.samples}
    with open(rpath, "w", encoding="utf-8") as out:
        for i, row in enumerate(rows):
            user = row["messages"][1]["content"]
            fam = family(user)
            if only and fam not in only:
                continue
            if i in done:
                for rec in done[i]:
                    out.write(json.dumps(rec, ensure_ascii=False) + "\n")
                    samples.append(rec)
                continue
            ref_src = program_for(fam, user, code_of(row["messages"][2]["content"]), row["messages"][2]["content"])
            ok, want, err = compile_and_run(ail, ref_src)
            if not ok or want is None:
                print("{}/{} {} skip: reference fails".format(i + 1, len(rows), fam), file=sys.stderr)
                continue
            # Round 0: arm A's call, unchanged (same messages, seed and batch of samples).
            texts, p_tok, g_toks, secs = gen([{"role": "system", "content": system},
                                              {"role": "user", "content": user}], 1000 * i, args.samples)
            marks = []
            for s, text in enumerate(texts):
                src = program_for(fam, user, code_of(text), text)
                c_ok, c_out = check_only(ail, src)
                revs = [{"round": 0, "prompt_tokens": p_tok, "gen_tokens": g_toks[s],
                         "seconds": round(secs / len(texts), 2), "text": text, "source": src,
                         "check_ok": c_ok, "check_output": c_out, "codes": [] if c_ok else codes(c_out)}]
                for r in range(1, args.rounds + 1):
                    if c_ok or not src.strip():
                        break
                    msg = correction_prompt(user, src, c_out, args.rounds - r)
                    t2, p2, g2, sec2 = gen([{"role": "system", "content": system},
                                            {"role": "user", "content": msg}], 1000 * i + 100 * r + s, 1)
                    src = code_of(t2[0])  # a revision is always a whole program
                    c_ok, c_out = check_only(ail, src)
                    revs.append({"round": r, "prompt_tokens": p2, "gen_tokens": g2[0], "seconds": round(sec2, 2),
                                 "text": t2[0], "source": src, "check_ok": c_ok, "check_output": c_out,
                                 "codes": [] if c_ok else codes(c_out)})
                compiled, got, run_err = compile_and_run(ail, src)
                passed = compiled and got == want
                a_compiled, a_got, _ = (compiled, got, None) if len(revs) == 1 else \
                    compile_and_run(ail, revs[0]["source"])
                rec = {"i": i, "family": fam, "sample": s, "rounds_used": len(revs) - 1,
                       "initial_compiled": revs[0]["check_ok"],
                       "initial_passed": bool(a_compiled and a_got == want),
                       "final_compiled": compiled, "passed": passed, "run_error": (run_err or "")[:1000],
                       "revisions": revs}
                out.write(json.dumps(rec, ensure_ascii=False) + "\n")
                out.flush()
                samples.append(rec)
                marks.append(("P" if passed else ("c" if compiled else ".")) + str(len(revs) - 1))
            print("{}/{} {} {}  ({:.0f} min)".format(i + 1, len(rows), fam, " ".join(marks),
                                                     (time.time() - t_all) / 60), file=sys.stderr)

    summary = {"model": os.path.basename(args.model.rstrip("/")), "adapter": args.adapter, "rounds": args.rounds,
               "samples": args.samples, "temp": args.temp, "max_tokens": args.max_tokens,
               "minutes": round((time.time() - t_all) / 60, 1), "table": metrics(samples, args.rounds)}
    with open(os.path.join(args.out, "summary.json"), "w", encoding="utf-8") as f:
        json.dump(summary, f, indent=1, sort_keys=True)
    print_table(summary["table"], args.samples)


def metrics(samples, rounds):
    """Kaleb's arm B metrics per family and for all. Rates are percent of samples unless named otherwise."""
    groups = {}
    for s in samples:
        for k in (s["family"], "all"):
            groups.setdefault(k, []).append(s)
    table = {}
    for fam, ss in groups.items():
        n = len(ss)
        items = {}
        for s in ss:
            items.setdefault(s["i"], []).append(s)
        failed0 = [s for s in ss if not s["initial_compiled"]]
        wins = [s for s in ss if s["passed"]]
        corr = [r for s in ss for r in s["revisions"][1:]]
        # Error recurrence: a correction round whose check still fails with a rule ID the round before also had.
        rec_n = rec_hit = same_src = 0
        for s in ss:
            rv = s["revisions"]
            for a, b in zip(rv, rv[1:]):
                if a["check_ok"]:
                    continue
                rec_n += 1
                if not b["check_ok"] and set(a["codes"]) & set(b["codes"]):
                    rec_hit += 1
                if b["source"].strip() == a["source"].strip():
                    same_src += 1
        tok = [sum(r["prompt_tokens"] + r["gen_tokens"] for r in s["revisions"]) for s in ss]
        tok0 = [s["revisions"][0]["prompt_tokens"] + s["revisions"][0]["gen_tokens"] for s in ss]
        sec = [sum(r["seconds"] for r in s["revisions"]) for s in ss]
        sec0 = [s["revisions"][0]["seconds"] for s in ss]
        by_round_c, by_round_p = [], []
        for r in range(rounds + 1):  # compile rate if the loop had stopped after round r
            by_round_c.append(pct(sum(any(v["check_ok"] for v in s["revisions"][:r + 1]) for s in ss), n))
        e = {
            "items": len(items), "samples": n,
            "initial_compile": pct(sum(s["initial_compiled"] for s in ss), n),
            "final_compile": pct(sum(s["final_compiled"] for s in ss), n),
            "armA_pass@1": pct(sum(s["initial_passed"] for s in ss), n),
            "pass@1": pct(len(wins), n),
            "armA_pass@k": pct(sum(any(x["initial_passed"] for x in v) for v in items.values()), len(items)),
            "pass@k": pct(sum(any(x["passed"] for x in v) for v in items.values()), len(items)),
            "initial_compile_failures": len(failed0),
            "recovered_compile": pct(sum(s["final_compiled"] for s in failed0), len(failed0)),
            "recovered_pass": pct(sum(s["passed"] for s in failed0), len(failed0)),
            "compiled_but_wrong_output": pct(sum(s["final_compiled"] and not s["passed"] for s in ss), n),
            "attempts_per_success": round(sum(1 + s["rounds_used"] for s in wins) / len(wins), 2) if wins else None,
            "generations_per_success": round(sum(1 + s["rounds_used"] for s in ss) / len(wins), 2) if wins else None,
            "correction_rounds": len(corr),
            "error_recurrence": pct(rec_hit, rec_n),
            "unchanged_revision": pct(same_src, rec_n),
            "tokens_per_sample_armA": round(sum(tok0) / n),
            "tokens_per_sample": round(sum(tok) / n),
            "tokens_per_success": round(sum(tok) / len(wins)) if wins else None,
            "seconds_per_sample_armA": round(sum(sec0) / n, 1),
            "seconds_per_sample": round(sum(sec) / n, 1),
            "compile_by_round": by_round_c,
            "passes_by_round": [sum(s["passed"] and s["rounds_used"] == r for s in ss) for r in range(rounds + 1)],
        }
        table[fam] = e
    return table


def pct(a, b):
    return round(100.0 * a / b, 1) if b else None


def print_table(table, k):
    cols = [("initial_compile", "comp0%"), ("final_compile", "compB%"), ("armA_pass@1", "A@1%"), ("pass@1", "B@1%"),
            ("armA_pass@k", "A@{}%".format(k)), ("pass@k", "B@{}%".format(k)), ("recovered_compile", "recC%"),
            ("recovered_pass", "recP%"), ("attempts_per_success", "att/win"), ("error_recurrence", "recur%"),
            ("tokens_per_sample", "tok/smp"), ("seconds_per_sample", "s/smp")]
    print("family    items " + " ".join("{:>8}".format(h) for _, h in cols))
    order = [f for f in FAMILIES if f in table] + ["all"]
    for fam in order:
        e = table[fam]
        print("{:<9} {:>5} ".format(fam, e["items"]) + " ".join("{:>8}".format("-" if e[c] is None else e[c])
                                                               for c, _ in cols))


if __name__ == "__main__":
    main()
