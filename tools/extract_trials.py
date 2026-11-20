#!/usr/bin/env python3
"""Pull every AIL agent trial out of agentbench result archives (no build, read only).

  extract_trials.py OUT.jsonl ARCHIVE[,PART2,...] ...

An archive is a .tgz of agentbench `results/`; a split archive is given as its parts joined by commas.
Writes one JSON line per AIL trial: run, task, arm, trial, metrics (correct, versions_to_green, ...),
spec (SPEC.md or issue.md), files {path: source} for every .ail under ws/src (and ws/ for single-file tasks).
C and Rust trials are skipped. Task names matching --deny (regex) are skipped (sealed or eval tasks).
"""
import io, json, os, re, sys, tarfile, argparse

ap = argparse.ArgumentParser()
ap.add_argument("out"); ap.add_argument("archives", nargs="+")
ap.add_argument("--deny", default=r"sealed|heldout|held-out")
a = ap.parse_args()
deny = re.compile(a.deny)

def open_archive(spec):
    parts = spec.split(",")
    if len(parts) == 1:
        return tarfile.open(parts[0], "r:*"), os.path.basename(parts[0])
    buf = b"".join(open(p, "rb").read() for p in parts)
    return tarfile.open(fileobj=io.BytesIO(buf), mode="r:*"), os.path.basename(parts[0])

trial_re = re.compile(r"(?:^|/)results/([^/]+)/((ail[^/]*)-(\d+))/(.*)$")
n = skipped = 0
seen = set()
with open(a.out, "a") as out:
    for spec in a.archives:
        tf, run = open_archive(spec)
        trials = {}
        for m in tf:
            if not m.isfile(): continue
            g = trial_re.search(m.name)
            if not g: continue
            task, trial, arm, _, rest = g.groups()
            if ".invalid-" in trial or "/.git/" in "/" + rest or "/DOCS/" in "/" + rest or "/.bench/" in "/" + rest: continue
            want = rest in ("metrics.json", "ws/SPEC.md", "ws/issue.md") or (rest.startswith("ws/") and rest.endswith(".ail"))
            if not want: continue
            t = trials.setdefault((task, trial, arm), {"files": {}})
            data = tf.extractfile(m).read().decode("utf-8", "replace")
            if rest == "metrics.json":
                try: t["metrics"] = json.loads(data)
                except Exception: t["metrics"] = None
            elif rest in ("ws/SPEC.md", "ws/issue.md"): t["spec"] = data
            else: t["files"][rest[3:]] = data
        for (task, trial, arm), t in sorted(trials.items()):
            if deny.search(task): skipped += 1; continue
            if not t["files"]: continue
            key = (task, trial, json.dumps(t["files"], sort_keys=True))
            if key in seen: continue
            seen.add(key)
            m = t.get("metrics") or {}
            keep = {k: m.get(k) for k in ("correct", "stopped", "versions_to_green", "fix_rounds", "first_check_clean", "turns_to_green", "passed", "total", "model") if k in m}
            out.write(json.dumps({"run": run, "task": task, "arm": arm, "trial": trial, "metrics": keep,
                                  "spec": t.get("spec", ""), "files": t["files"]}) + "\n")
            n += 1
print(f"{n} trials written, {skipped} skipped by --deny", file=sys.stderr)
