"""dev-task eval: held-out input-driven tasks (data/eval/dev-task/NAME/{spec.md, NAME.ail, cases/N.in, N.out}).

The prompt is built exactly like the `task` training family (tools/run3_build.py): the spec, then two example cases
(the first two), under the short system prompt. A sample passes only when its program passes `ail check --no-fix` and
prints exactly the expected stdout on ALL of the item's cases (`ail run --timeout 10000 --max-memory 512`, stdin = the
case). Reported: compile %, pass@1, pass@k, the fraction of cases passed by compiled samples, by size class
(small / medium / large, from the VERIFIED marker).

--rounds N adds the compiler loop of tools/eval_loop.py: while `ail check` fails and rounds are left, the model gets
the task, its current program and the check output (the same correction prompt) and answers with a whole program.
Runtime results are never fed back. Round 0 is the one-shot answer, so one run gives both numbers.

Generation goes through a running llama-server (tools/server_client.py), WORKERS items in flight.
"""

import argparse
import concurrent.futures
import json
import os
import shutil
import subprocess
import sys
import tempfile
import time

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from eval_quick import ROOT, code_of, read  # noqa: E402
from eval_loop import check_only, codes, correction_prompt  # noqa: E402
from server_client import ServerGen  # noqa: E402


def load_items(root):
    items = []
    for name in sorted(os.listdir(root)):
        d = os.path.join(root, name)
        if not os.path.isfile(os.path.join(d, "spec.md")):
            continue
        cases, k = [], 1
        while os.path.isfile(os.path.join(d, "cases", "{}.in".format(k))):
            cases.append((read(os.path.join(d, "cases", "{}.in".format(k))),
                          read(os.path.join(d, "cases", "{}.out".format(k)))))
            k += 1
        size = read(os.path.join(d, "SIZE")).strip() if os.path.isfile(os.path.join(d, "SIZE")) else "?"
        items.append({"name": name, "spec": read(os.path.join(d, "spec.md")).strip(), "cases": cases, "size": size})
    return items


def prompt_of(item):
    """The `task` family's user message: spec + two example cases (as in run3_build.py)."""
    ex = item["cases"][:2]
    nl = lambda s: s if s.endswith("\n") or not s else s + "\n"  # noqa: E731
    return item["spec"] + "\n\nExamples:\n\n" + "\n\n".join(
        "Input:\n```\n{}```\nOutput:\n```\n{}```".format(nl(i), nl(o)) for i, o in ex)


def run_cases(ail, src, cases):
    """(compiled, cases passed, first failure note)."""
    tmp = tempfile.mkdtemp(prefix="aildt-")
    try:
        with open(os.path.join(tmp, "main.ail"), "w", encoding="utf-8") as f:
            f.write(src)
        env = dict(os.environ, AIL_FIX="0")
        try:
            c = subprocess.run([ail, "check", "--no-fix", "main.ail"], cwd=tmp, capture_output=True, text=True,
                               env=env, timeout=120)
        except subprocess.TimeoutExpired:
            return False, 0, "check timeout"
        if c.returncode != 0:
            return False, 0, (c.stdout + c.stderr)[:1000]
        ok, note = 0, ""
        for k, (inp, want) in enumerate(cases, 1):
            try:
                r = subprocess.run([ail, "run", "--timeout", "10000", "--max-memory", "512", "main.ail"], cwd=tmp,
                                   input=inp, capture_output=True, text=True, env=env, timeout=120)
                good = r.stdout == want and "trap[" not in r.stderr
                if not good and not note:
                    note = "case {}: {}".format(k, (r.stderr.strip() or "output differs")[:300])
            except subprocess.TimeoutExpired:
                good = False
                note = note or "case {}: timeout".format(k)
            ok += good
        return True, ok, note
    finally:
        shutil.rmtree(tmp, ignore_errors=True)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--ail", required=True)
    ap.add_argument("--model", default="", help="base model dir (generation_config.json: top_k, repetition penalty)")
    ap.add_argument("--data", default=os.path.join(ROOT, "data", "eval", "dev-task"))
    ap.add_argument("--out", required=True)
    ap.add_argument("--samples", type=int, default=3)
    ap.add_argument("--temp", type=float, default=0.2)
    ap.add_argument("--max-tokens", type=int, default=1536)
    ap.add_argument("--rounds", type=int, default=0)
    ap.add_argument("--server-url", default="http://127.0.0.1:8080")
    ap.add_argument("--workers", type=int, default=8)
    args = ap.parse_args()

    ail = os.path.join(os.path.abspath(args.ail), "ail")
    system = read(os.path.join(ROOT, "tools", "preflight", "short-system.txt")).strip()
    items = load_items(args.data)
    sg = ServerGen(args.server_url, args.temp, args.max_tokens, args.model)
    os.makedirs(args.out, exist_ok=True)
    t0 = time.time()

    def do_item(ix):
        it = items[ix]
        user = prompt_of(it)
        texts, _, _, _ = sg.gen([{"role": "system", "content": system}, {"role": "user", "content": user}],
                                1000 * ix, args.samples)
        recs = []
        for s, text in enumerate(texts):
            src = code_of(text)
            first = run_cases(ail, src, it["cases"])
            c_ok, c_out = (first[0], "") if first[0] else check_only(ail, src)
            rounds = []
            for r in range(1, args.rounds + 1):
                if c_ok or not src.strip():
                    break
                msg = correction_prompt(user, src, c_out, args.rounds - r)
                t2, _, _, _ = sg.gen([{"role": "system", "content": system}, {"role": "user", "content": msg}],
                                     1000 * ix + 100 * r + s, 1)
                src = code_of(t2[0])
                c_ok, c_out = check_only(ail, src)
                rounds.append({"round": r, "check_ok": c_ok, "codes": [] if c_ok else codes(c_out)})
            final = first if not rounds else run_cases(ail, src, it["cases"])
            n = len(it["cases"])
            recs.append({"name": it["name"], "size": it["size"], "sample": s, "cases": n,
                         "initial_compiled": first[0], "initial_cases_passed": first[1],
                         "initial_passed": first[0] and first[1] == n,
                         "compiled": final[0], "cases_passed": final[1], "passed": final[0] and final[1] == n,
                         "rounds_used": len(rounds), "rounds": rounds, "note": final[2],
                         "answer": text, "final_source": src})
        return ix, recs

    allrecs = []
    with open(os.path.join(args.out, "answers.jsonl"), "w", encoding="utf-8") as out, \
            concurrent.futures.ThreadPoolExecutor(args.workers) as ex:
        for fut in concurrent.futures.as_completed([ex.submit(do_item, i) for i in range(len(items))]):
            ix, recs = fut.result()
            for r in recs:
                out.write(json.dumps(r, ensure_ascii=False) + "\n")
            out.flush()
            allrecs.extend(recs)
            print("{} {} {}  ({:.0f} min)".format(items[ix]["name"], items[ix]["size"], "".join(
                "P" if r["passed"] else ("c" if r["compiled"] else ".") for r in recs), (time.time() - t0) / 60),
                file=sys.stderr)

    def table(pre):
        t = {}
        for grp in ("all", "small", "medium", "large"):
            rs = [r for r in allrecs if grp == "all" or r["size"] == grp]
            names = sorted({r["name"] for r in rs})
            if not names:
                continue
            comp = [r for r in rs if r[pre + "compiled"]]
            t[grp] = {"items": len(names),
                      "compile": round(100 * len(comp) / len(rs), 1),
                      "pass@1": round(100 * sum(r[pre + "passed"] for r in rs) / len(rs), 1),
                      "pass@k": round(100 * sum(any(r[pre + "passed"] for r in rs if r["name"] == n)
                                                for n in names) / len(names), 1),
                      "cases_passed_of_compiled": round(100 * sum(r[pre + "cases_passed"] for r in comp) /
                                                        max(1, sum(r["cases"] for r in comp)), 1)}
        return t

    summary = {"items": len(items), "samples": args.samples, "temp": args.temp, "max_tokens": args.max_tokens,
               "rounds": args.rounds, "minutes": round((time.time() - t0) / 60, 1),
               "one_shot": table("initial_"), "final": table("")}
    with open(os.path.join(args.out, "summary.json"), "w", encoding="utf-8") as f:
        json.dump(summary, f, indent=1, sort_keys=True)
    for key in ("one_shot", "final") if args.rounds else ("one_shot",):
        print(key)
        print("| size | items | compile | pass@1 | pass@{} | cases passed (compiled) |".format(args.samples))
        print("|---|---|---|---|---|---|")
        for g, v in summary[key].items():
            print("| {} | {} | {} | {} | {} | {} |".format(g, v["items"], v["compile"], v["pass@1"], v["pass@k"],
                                                         v["cases_passed_of_compiled"]))


if __name__ == "__main__":
    main()
