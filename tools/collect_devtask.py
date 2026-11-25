"""Collect held-out dev-task items into data/eval/dev-task/ (eval only, never training).

python3 tools/collect_devtask.py --src STAGING_DIR --train data/build/train.jsonl [--out data/eval/dev-task]

For every staged task with a VERIFIED marker (the verifier wrote the size class into it): the AIL program and the
spec are compared, by token 8-grams (the builder's near-duplicate rule, more than 30% shared drops), against every
train program and user message, every data/extra/tasks* program and spec, and the quick-eval and dev-spec programs.
Kept tasks are copied as NAME/{spec.md, NAME.ail, NAME.py, SIZE, cases/N.in, N.out}; then MANIFEST.sha256 lists the
sha256 of every file. Prints what it kept and dropped.
"""

import argparse
import hashlib
import json
import os
import re
import shutil
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from build_data import ROOT, grams  # noqa: E402

FENCE = re.compile(r"```ail\n(.*?)```", re.S)


def index_of(texts):
    idx = {}
    for k, t in enumerate(texts):
        for g in grams(t):
            idx.setdefault(g, set()).add(k)
    return idx


def worst(text, idx):
    gs = grams(text)
    if not gs:
        return 0.0
    c = {}
    for g in gs:
        for k in idx.get(g, ()):
            c[k] = c.get(k, 0) + 1
    return max(c.values()) / len(gs) if c else 0.0


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--src", required=True)
    ap.add_argument("--train", default=os.path.join(ROOT, "data", "build", "train.jsonl"))
    ap.add_argument("--out", default=os.path.join(ROOT, "data", "eval", "dev-task"))
    args = ap.parse_args()

    progs, texts = [], []
    build = os.path.dirname(args.train)
    for f in ("train.jsonl", "quick-eval.jsonl", "dev-spec.jsonl", "valid.jsonl"):
        p = os.path.join(build, f)
        if not os.path.isfile(p):
            continue
        for line in open(p, encoding="utf-8"):
            m = json.loads(line)["messages"]
            texts.append(m[1]["content"])
            progs.extend(FENCE.findall(m[2]["content"]) or [m[2]["content"]])
            progs.extend(FENCE.findall(m[1]["content"]))
    extra = os.path.join(ROOT, "data", "extra")
    for grp in sorted(os.listdir(extra)):
        if not grp.startswith("tasks"):
            continue
        for name in sorted(os.listdir(os.path.join(extra, grp))):
            d = os.path.join(extra, grp, name)
            progs.append(open(os.path.join(d, name + ".ail"), encoding="utf-8").read())
            texts.append(open(os.path.join(d, "spec.md"), encoding="utf-8").read())
    pidx, tidx = index_of(progs), index_of(texts)
    print("compared against {} programs and {} texts".format(len(progs), len(texts)), file=sys.stderr)

    if os.path.isdir(args.out):
        shutil.rmtree(args.out)
    os.makedirs(args.out)
    kept, dropped = [], []
    for name in sorted(os.listdir(args.src)):
        d = os.path.join(args.src, name)
        if not os.path.isfile(os.path.join(d, "VERIFIED")):
            continue
        src = open(os.path.join(d, name + ".ail"), encoding="utf-8").read()
        spec = open(os.path.join(d, "spec.md"), encoding="utf-8").read()
        wp, ws = worst(src, pidx), worst(spec, tidx)
        if wp > 0.30 or ws > 0.30:
            dropped.append((name, round(wp, 2), round(ws, 2)))
            continue
        o = os.path.join(args.out, name)
        os.makedirs(os.path.join(o, "cases"))
        for f in ("spec.md", name + ".ail", name + ".py"):
            shutil.copy(os.path.join(d, f), o)
        with open(os.path.join(o, "SIZE"), "w") as f:
            f.write(open(os.path.join(d, "VERIFIED")).read().strip() + "\n")
        for f in sorted(os.listdir(os.path.join(d, "cases"))):
            if f.endswith((".in", ".out")):
                shutil.copy(os.path.join(d, "cases", f), os.path.join(o, "cases"))
        kept.append((name, open(os.path.join(o, "SIZE")).read().strip(), round(wp, 2), round(ws, 2)))
    lines = []
    for root, _, files in sorted(os.walk(args.out)):
        for f in sorted(files):
            p = os.path.join(root, f)
            if f == "MANIFEST.sha256":
                continue
            lines.append("{}  {}".format(hashlib.sha256(open(p, "rb").read()).hexdigest(),
                                         os.path.relpath(p, args.out).replace(os.sep, "/")))
    with open(os.path.join(args.out, "MANIFEST.sha256"), "w") as f:
        f.write("\n".join(sorted(lines, key=lambda l: l.split("  ", 1)[1])) + "\n")
    sizes = {}
    for _, s, _, _ in kept:
        sizes[s] = sizes.get(s, 0) + 1
    print(json.dumps({"kept": len(kept), "by_size": sizes, "dropped_near_dup": dropped,
                      "max_overlap_kept": max([max(k[2], k[3]) for k in kept] or [0])}, indent=1))


if __name__ == "__main__":
    main()
