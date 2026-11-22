"""M5 quick eval (PLAN.md section 7, stage 1): score one arm on data/build/quick-eval.jsonl.

Usage: python tools/eval_quick.py --ail AIL_ROOT --model MODEL_DIR [--adapter ADAPTER_DIR] [--system short|core|FILE]
                                  --out OUT_DIR [--samples 3] [--temp 0.2] [--max-tokens 1024] [--limit N]

Each quick-eval row holds a task and its reference answer, which passed the compiler when the data was built. An answer
passes when its program passes `ail check` and `ail run` prints what the reference program prints. For `complete` and
`cursor` the model's text is put back where the prompt marks it; `fixline` replaces the line it names; for `fix` the
answer is the whole fixed program. Writes
OUT/answers.jsonl (every sample with its verdict) and OUT/summary.json and prints a table: compile rate, pass@1 (mean
over samples) and pass@k (any sample) per family. Runs on the Mac only.
"""

import argparse
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
import time

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FENCE = re.compile(r"```[A-Za-z]*[^\n]*\n(.*?)```", re.S)
MARK = "\u27e8BODY\u27e9"
FILL = "\u27e8FILL\u27e9"
LINE = re.compile(r"Line (\d+):")


def read(path):
    with open(path, encoding="utf-8") as f:
        return f.read()


def code_of(text):
    """The first fenced block of an answer, or the whole answer when it has none."""
    m = FENCE.search(text)
    return (m.group(1) if m else text).rstrip("\n") + "\n"


def family(user):
    if user.startswith("Fill in the AIL code at"):
        return "cursor"
    if user.rstrip().endswith("Give the corrected line."):
        return "fixline"
    if user.startswith("Write the body of"):
        return "complete"
    if user.startswith("This AIL program fails"):
        return "fix"
    if user.startswith("Port this Python program"):
        return "port"
    return "write"


def program_for(fam, user, answer_code, answer_text=""):
    if fam == "cursor":
        prompt = user[user.index("```ail\n") + 7:user.rindex("\n```")]
        # A run of lines starts at a line start and ends with its own newline; the rest of a line has none.
        middle = answer_code if ("\n" + FILL) in prompt or prompt.startswith(FILL) else answer_code.rstrip("\n")
        return prompt.replace(FILL, middle, 1)
    if fam == "fixline":
        m = LINE.search(answer_text)
        if not m:
            return ""
        bad = code_of(user[user.index("```"):])
        lines = bad.rstrip("\n").split("\n")
        n = int(m.group(1))
        if not 1 <= n <= len(lines):
            return ""
        lines[n - 1] = answer_code.rstrip("\n").split("\n")[0]
        return "\n".join(lines) + "\n"
    if fam != "complete":
        return answer_code
    prompt = code_of(user[user.index("```"):])
    body = answer_code.rstrip("\n")
    lines = body.split("\n")
    if lines and not lines[0].startswith(" "):  # the model dropped the indent: put it back
        lines = ["    " + l if l.strip() else l for l in lines]
    return prompt.replace("    " + MARK, "\n".join(lines))


def compile_and_run(ail, src):
    tmp = tempfile.mkdtemp(prefix="ailq-")
    try:
        with open(os.path.join(tmp, "main.ail"), "w", encoding="utf-8") as f:
            f.write(src)
        env = dict(os.environ, AIL_FIX="0")
        try:
            c = subprocess.run([ail, "check", "--no-fix", "main.ail"], cwd=tmp, capture_output=True, text=True,
                               env=env, timeout=120)
        except subprocess.TimeoutExpired:
            return False, None, "check timeout"
        if c.returncode != 0:
            return False, None, (c.stdout + c.stderr)[-2000:]
        try:
            r = subprocess.run([ail, "run", "main.ail"], cwd=tmp, capture_output=True, text=True, env=env,
                               timeout=60)
        except subprocess.TimeoutExpired:
            return True, None, "run timeout"
        return True, r.stdout, "" if r.returncode == 0 else (r.stderr or "")[-2000:]
    finally:
        shutil.rmtree(tmp, ignore_errors=True)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--ail", required=True)
    ap.add_argument("--model", required=True)
    ap.add_argument("--adapter", default="")
    ap.add_argument("--system", default="short")
    ap.add_argument("--data", default=os.path.join(ROOT, "data", "build", "quick-eval.jsonl"))
    ap.add_argument("--out", required=True)
    ap.add_argument("--samples", type=int, default=3)
    ap.add_argument("--temp", type=float, default=0.2)
    ap.add_argument("--max-tokens", type=int, default=1024)
    ap.add_argument("--limit", type=int, default=0)
    args = ap.parse_args()

    import mlx.core as mx
    from mlx_lm import generate, load
    from mlx_lm.sample_utils import make_sampler

    ail = os.path.join(os.path.abspath(args.ail), "ail")
    if args.system == "short":
        system = read(os.path.join(ROOT, "tools", "preflight", "short-system.txt")).strip()
    elif args.system == "core":
        system = read(os.path.join(args.ail, "docs", "language-card-core.md"))
    else:
        system = read(args.system)
    rows = [json.loads(l) for l in open(args.data, encoding="utf-8")]
    if args.limit:
        rows = rows[:args.limit]
    model, tok = load(args.model, adapter_path=args.adapter or None)
    sampler = make_sampler(temp=args.temp)
    os.makedirs(args.out, exist_ok=True)

    results = []
    t0 = time.time()
    with open(os.path.join(args.out, "answers.jsonl"), "w", encoding="utf-8") as out:
        for i, row in enumerate(rows):
            user = row["messages"][1]["content"]
            ref_answer = row["messages"][2]["content"]
            fam = family(user)
            ref_src = program_for(fam, user, code_of(ref_answer), ref_answer)
            ok, want, err = compile_and_run(ail, ref_src)
            if not ok or want is None:
                results.append({"i": i, "family": fam, "skip": "reference fails: " + err[:200]})
                continue
            prompt = tok.apply_chat_template([{"role": "system", "content": system},
                                              {"role": "user", "content": user}], add_generation_prompt=True)
            verdicts = []
            for s in range(args.samples):
                mx.random.seed(1000 * i + s)
                text = generate(model, tok, prompt, max_tokens=args.max_tokens, sampler=sampler, verbose=False)
                src = program_for(fam, user, code_of(text), text)
                compiled, got, err = compile_and_run(ail, src)
                passed = compiled and got == want
                verdicts.append({"compiled": compiled, "passed": passed})
                out.write(json.dumps({"i": i, "family": fam, "sample": s, "compiled": compiled, "passed": passed,
                                      "answer": text, "error": err[:1000]}, ensure_ascii=False) + "\n")
                out.flush()
            results.append({"i": i, "family": fam, "verdicts": verdicts})
            print("{}/{} {} {}  ({:.0f} min)".format(i + 1, len(rows), fam,
                                                     "".join("P" if v["passed"] else ("c" if v["compiled"] else ".")
                                                             for v in verdicts), (time.time() - t0) / 60),
                  file=sys.stderr)

    table = {}
    for r in results:
        if "skip" in r:
            continue
        for fam in (r["family"], "all"):
            e = table.setdefault(fam, {"items": 0, "compile": 0.0, "pass@1": 0.0, "pass@k": 0})
            n = len(r["verdicts"])
            e["items"] += 1
            e["compile"] += sum(v["compiled"] for v in r["verdicts"]) / n
            e["pass@1"] += sum(v["passed"] for v in r["verdicts"]) / n
            e["pass@k"] += any(v["passed"] for v in r["verdicts"])
    for e in table.values():
        for k in ("compile", "pass@1", "pass@k"):
            e[k] = round(100.0 * e[k] / e["items"], 1)
    summary = {"model": os.path.basename(args.model.rstrip("/")), "adapter": args.adapter, "system": args.system,
               "samples": args.samples, "temp": args.temp, "skipped": sum(1 for r in results if "skip" in r),
               "minutes": round((time.time() - t0) / 60, 1), "table": table}
    with open(os.path.join(args.out, "summary.json"), "w", encoding="utf-8") as f:
        json.dump(summary, f, indent=1, sort_keys=True)
    print("family    items  compile%  pass@1%  pass@{}%".format(args.samples))
    for fam in sorted(table, key=lambda f: (f == "all", f)):
        e = table[fam]
        print("{:<9} {:>5}  {:>8}  {:>7}  {:>7}".format(fam, e["items"], e["compile"], e["pass@1"], e["pass@k"]))


if __name__ == "__main__":
    main()
