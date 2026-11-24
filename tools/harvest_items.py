"""Run 3, phase 3: turn the model's own attempts on train tasks (tools/eval_loop.py over harvest-tasks.jsonl) into
repair and behave training items.

  python tools/harvest_items.py todo  --ail AIL_ROOT --run RUN_DIR --tasks harvest-tasks.jsonl --out HARVEST_DIR
  python tools/harvest_items.py items --ail AIL_ROOT --out HARVEST_DIR

`todo` writes HARVEST_DIR/auto.jsonl (items straight from trajectories that ended with the exact reference output:
each failing revision + its diagnostic -> the final passing program) and HARVEST_DIR/todo/ID.json for every attempt
that stayed broken or compiled but printed the wrong output (task, the model's last program, its diagnostic or its
actual output, the expected output, the reference program). A person or another model writes the smallest edit of
the model's own program that passes the check and prints exactly the expected output to HARVEST_DIR/fixed/ID.ail.

`items` re-checks every fixed/ID.ail with the pinned compiler (check passes, `ail run` prints exactly the expected
output) and writes HARVEST_DIR/items.jsonl = auto items + confirmed fixes, which tools/build_data.py reads.
Only train-split tasks are ever used (harvest-tasks.jsonl comes from train.jsonl).
"""

import argparse
import hashlib
import json
import os
import shutil
import subprocess
import sys
import tempfile

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from eval_quick import code_of  # noqa: E402
from run3_families import behave_prompt, fence, repair_prompt, trap_of  # noqa: E402

SPEC_MARK = "\n\nIt must print exactly:\n\n```\n"


def sha(*parts):
    return hashlib.sha256("\0".join(parts).encode("utf-8")).hexdigest()


def run_prog(ail, src, cmd):
    tmp = tempfile.mkdtemp(prefix="ailharv-")
    try:
        with open(os.path.join(tmp, "main.ail"), "w", encoding="utf-8") as f:
            f.write(src)
        env = dict(os.environ, AIL_FIX="0")
        try:
            r = subprocess.run([ail] + cmd + ["main.ail"], cwd=tmp, capture_output=True, text=True, env=env,
                               timeout=60, stdin=subprocess.DEVNULL)
        except subprocess.TimeoutExpired:
            return {"rc": -1, "stdout": "", "stderr": "timeout"}
        return {"rc": r.returncode, "stdout": r.stdout, "stderr": r.stderr}
    finally:
        shutil.rmtree(tmp, ignore_errors=True)


def task_with_output(user, want):
    """The behave prompt needs the expected output in the task: spec tasks have it; port tasks get it appended."""
    if SPEC_MARK in user:
        return user
    return user.rstrip() + SPEC_MARK + want + ("" if want.endswith("\n") else "\n") + "```"


def cmd_todo(args):
    ail = os.path.join(os.path.abspath(args.ail), "ail")
    tasks = [json.loads(l) for l in open(args.tasks, encoding="utf-8")]
    revs = [json.loads(l) for l in open(os.path.join(args.run, "revisions.jsonl"), encoding="utf-8")]
    os.makedirs(os.path.join(args.out, "todo"), exist_ok=True)
    os.makedirs(os.path.join(args.out, "fixed"), exist_ok=True)
    want_cache = {}
    auto, todo = [], 0
    stats = {"samples": len(revs), "passed": 0, "auto_items": 0, "todo_repair": 0, "todo_behave": 0}
    for r in revs:
        row = tasks[r["i"]]
        user, ref = row["messages"][1]["content"], code_of(row["messages"][2]["content"])
        if r["i"] not in want_cache:
            want_cache[r["i"]] = run_prog(ail, ref, ["run"])["stdout"]
        want = want_cache[r["i"]]
        rid = "{}-{}-{}".format(sha(user)[:12], r["i"], r["sample"])
        last = r["revisions"][-1]
        if r["passed"]:
            stats["passed"] += 1
            for v in r["revisions"][:-1]:
                if v["check_ok"] or not v["source"].strip():
                    continue
                key = "{}#r{}".format(rid, v["round"])
                auto.append({"id": key, "family": "repair", "prog": last["source"],
                             "user": repair_prompt(user, v["source"], v["check_output"].strip(), key),
                             "answer": fence(last["source"])})
            continue
        item = {"id": rid, "i": r["i"], "task": user, "want": want, "reference": ref, "source": last["source"]}
        if r["final_compiled"]:
            got = run_prog(ail, last["source"], ["run"])
            item.update(family="behave", got=got["stdout"], trap=trap_of(got["stderr"]))
            stats["todo_behave"] += 1
        else:
            item.update(family="repair", diag=last["check_output"].strip())
            stats["todo_repair"] += 1
        with open(os.path.join(args.out, "todo", rid + ".json"), "w", encoding="utf-8") as f:
            json.dump(item, f, ensure_ascii=False, indent=1)
        todo += 1
    stats["auto_items"] = len(auto)
    with open(os.path.join(args.out, "auto.jsonl"), "w", encoding="utf-8") as f:
        for it in sorted(auto, key=lambda x: x["id"]):
            f.write(json.dumps(it, ensure_ascii=False) + "\n")
    print(json.dumps(stats, indent=1))


def cmd_items(args):
    ail = os.path.join(os.path.abspath(args.ail), "ail")
    out = []
    if os.path.isfile(os.path.join(args.out, "auto.jsonl")):
        out += [json.loads(l) for l in open(os.path.join(args.out, "auto.jsonl"), encoding="utf-8")]
    n_auto, ok, bad = len(out), 0, []
    tdir, fdir = os.path.join(args.out, "todo"), os.path.join(args.out, "fixed")
    for name in sorted(os.listdir(fdir)) if os.path.isdir(fdir) else []:
        if not name.endswith(".ail"):
            continue
        rid = name[:-4]
        tpath = os.path.join(tdir, rid + ".json")
        if not os.path.isfile(tpath):
            bad.append((rid, "no todo"))
            continue
        t = json.load(open(tpath, encoding="utf-8"))
        fixed = open(os.path.join(fdir, name), encoding="utf-8").read()
        c = run_prog(ail, fixed, ["check", "--no-fix"])
        if c["rc"] != 0:
            bad.append((rid, "check fails"))
            continue
        r = run_prog(ail, fixed, ["run"])
        if r["stdout"] != t["want"] or trap_of(r["stderr"]):
            bad.append((rid, "output differs"))
            continue
        if t["family"] == "repair":
            user = repair_prompt(t["task"], t["source"], t["diag"], rid)
        else:
            user = behave_prompt(task_with_output(t["task"], t["want"]), t["source"], t["got"], t.get("trap", ""))
        out.append({"id": rid, "family": t["family"], "prog": fixed, "user": user, "answer": fence(fixed)})
        ok += 1
    with open(os.path.join(args.out, "items.jsonl"), "w", encoding="utf-8") as f:
        for it in sorted(out, key=lambda x: (x["family"], x["id"])):
            f.write(json.dumps(it, ensure_ascii=False) + "\n")
    print(json.dumps({"auto": n_auto, "fixed_confirmed": ok, "fixed_rejected": len(bad), "rejected": bad[:30],
                      "items": len(out)}, indent=1))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("cmd", choices=["todo", "items"])
    ap.add_argument("--ail", required=True)
    ap.add_argument("--run", default="")
    ap.add_argument("--tasks", default="")
    ap.add_argument("--out", required=True)
    args = ap.parse_args()
    cmd_todo(args) if args.cmd == "todo" else cmd_items(args)


if __name__ == "__main__":
    main()
