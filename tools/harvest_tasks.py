"""Run 3 harvest: pick whole-program tasks from the TRAIN split for the current model to attempt (tools/eval_loop.py).

Usage: python tools/harvest_tasks.py [--train data/build/train.jsonl] --out FILE [--spec 120] [--port 120]
                                     [--max-ref-tokens 900] [--seed 20261124]

Reads only train.jsonl, so no quick-eval or valid program can be picked. Picks by a hash of the task text (stable
across runs), keeps items whose reference answer is at most --max-ref-tokens (chars / 3.35), and writes the rows
unchanged (same message format as quick-eval.jsonl). The model's failing drafts on these items, with the compiler
output or the wrong program output, become repair and behave training items (run 3, phase 3).
"""

import argparse
import hashlib
import json
import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def kind(user):
    if user.startswith("Port this Python program"):
        return "port"
    if "\n\nIt must print exactly:\n\n```\n" in user:
        return "spec"
    return None


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--train", default=os.path.join(ROOT, "data", "build", "train.jsonl"))
    ap.add_argument("--out", required=True)
    ap.add_argument("--spec", type=int, default=120)
    ap.add_argument("--port", type=int, default=120)
    ap.add_argument("--max-ref-tokens", type=int, default=900)
    ap.add_argument("--seed", type=int, default=20261124)
    args = ap.parse_args()

    want = {"spec": args.spec, "port": args.port}
    cands = {"spec": [], "port": []}
    for line in open(args.train, encoding="utf-8"):
        row = json.loads(line)
        user, ref = row["messages"][1]["content"], row["messages"][2]["content"]
        k = kind(user)
        if k is None or len(ref) / 3.35 > args.max_ref_tokens:
            continue
        h = hashlib.sha256("{}\0{}".format(args.seed, user).encode("utf-8")).hexdigest()
        cands[k].append((h, line))
    rows = []
    for k in ("spec", "port"):
        rows += [line for _, line in sorted(cands[k])[:want[k]]]
        print("{}: {} picked of {} candidates".format(k, min(want[k], len(cands[k])), len(cands[k])))
    os.makedirs(os.path.dirname(os.path.abspath(args.out)), exist_ok=True)
    with open(args.out, "w", encoding="utf-8") as f:
        f.writelines(rows)
    print("wrote {} rows to {}".format(len(rows), args.out))


if __name__ == "__main__":
    main()
