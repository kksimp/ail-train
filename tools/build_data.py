"""M2 data builder (PLAN.md section 5.4): every AIL source that enters training is checked with the pinned compiler.

Run on the Mac through tools/build_data/run.sh, or directly:
  python tools/build_data.py --ail AIL_ROOT [--out data/build] [--system short|core|FILE] [--tokenizer MODEL_DIR]
                             [--max-tokens 2048] [--jobs 4] [--seed 20261121]

Writes OUT/{train,valid,quick-eval}.jsonl (chat format for mlx_lm.lora) and OUT/manifest.json (counts per family,
source and split, token totals, every dropped item with its reason, the ail commit, the seed). Deterministic: the
same inputs give byte-identical output. Compiler results are cached by content under ~/ail-train-work/build-cache.

Families (PLAN.md 5.2): write, port, fix, change, complete, explain; since run 2 also cursor (fill in the middle:
the rest of a line or a run of lines) fixline (one injected mistake from the drafts; the answer is the line) and function (write one missing
function from its signature and the program around it). Splits are by group (one program, one mistake,
one agent task), so no program appears in two splits. quick-eval holds 10% of corpus programs and 10% of mistakes;
valid holds 5% of the other groups except the agent tasks. Train items whose program shares more than 30% of its
token 8-grams with a quick-eval program are dropped (5.3 rule 5).
"""

import argparse
import concurrent.futures
import difflib
import hashlib
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
import threading

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CACHE = os.path.join(os.path.expanduser("~"), "ail-train-work", "build-cache")
SHORT_SYSTEM = os.path.join(ROOT, "tools", "preflight", "short-system.txt")
RULE = re.compile(r"error\[([a-z][a-z0-9_]*(?:\.[a-z0-9_]+)+)\]")
SKIP_CASE_EXT = {".args", ".err", ".trap", ".stderr", ".rules", ".test", ".stdin", ".txt"}


def sha(*parts):
    h = hashlib.sha256()
    for p in parts:
        h.update(p.encode("utf-8") if isinstance(p, str) else p)
        h.update(b"\0")
    return h.hexdigest()


def read(path):
    with open(path, encoding="utf-8") as f:
        return f.read()


def fence(src, path=None):
    head = "`{}`\n".format(path) if path else ""
    return "{}```ail\n{}\n```".format(head, src.rstrip("\n"))


def files_block(files):
    return "\n\n".join(fence(files[p], p) for p in sorted(files))


def header_text(src):
    """The leading comment of a program (`##` or `#` lines): the task it states."""
    out = []
    for line in src.splitlines():
        s = line.strip()
        if s.startswith("#"):
            out.append(s.lstrip("#").strip())
        elif s == "" and not out:
            continue
        else:
            break
    return " ".join(x for x in out if x)


# ---------------------------------------------------------------- compiler


class Compiler:
    def __init__(self, ail_root, jobs):
        self.root = ail_root
        self.ail = os.path.join(ail_root, "ail")
        self.commit = subprocess.run(["git", "-C", ail_root, "rev-parse", "HEAD"], capture_output=True,
                                     text=True).stdout.strip()
        self.jobs = jobs
        os.makedirs(CACHE, exist_ok=True)

    def _exec(self, files, cmd, rel):
        """Write FILES (path -> text) into a scratch folder and run `ail CMD rel` there."""
        tmp = tempfile.mkdtemp(prefix="ailbuild-")
        try:
            for p, text in files.items():
                full = os.path.join(tmp, p)
                os.makedirs(os.path.dirname(full), exist_ok=True)
                with open(full, "w", encoding="utf-8") as f:
                    f.write(text)
            env = dict(os.environ, AIL_FIX="0")
            args = [self.ail] + cmd + ([rel] if rel else [])
            try:
                r = subprocess.run(args, cwd=tmp, capture_output=True, text=True, env=env, timeout=300)
                out = (r.stdout or "") + (r.stderr or "")
                return {"rc": r.returncode, "stdout": r.stdout or "", "out": out.replace(tmp + "/", "")}
            except subprocess.TimeoutExpired:
                return {"rc": -1, "stdout": "", "out": "timeout"}
        finally:
            shutil.rmtree(tmp, ignore_errors=True)

    def run(self, files, cmd, rel):
        key = sha(self.commit, json.dumps(files, sort_keys=True), json.dumps(cmd), rel or "")
        path = os.path.join(CACHE, key + ".json")
        try:
            with open(path, encoding="utf-8") as f:
                return json.load(f)
        except (OSError, ValueError):
            pass
        res = self._exec(files, cmd, rel)
        if res["out"] != "timeout":
            part = "{}.{}.part".format(path, threading.get_ident())
            with open(part, "w", encoding="utf-8") as f:
                json.dump(res, f)
            os.replace(part, path)  # atomic, so a parallel reader never sees half a file
        return res

    def many(self, jobs):
        """jobs: list of (key, files, cmd, rel). Returns {key: result}."""
        out = {}
        with concurrent.futures.ThreadPoolExecutor(self.jobs) as ex:
            futs = {ex.submit(self.run, f, c, r): k for k, f, c, r in jobs}
            done = 0
            for fut in concurrent.futures.as_completed(futs):
                out[futs[fut]] = fut.result()
                done += 1
                if done % 200 == 0:
                    print("  {} of {}".format(done, len(jobs)), file=sys.stderr)
        return out


# ---------------------------------------------------------------- sources


def program_sources(ail_root):
    """Single-file programs: (group, source, name, ail, py or None, out or None)."""
    progs = []
    corpus = os.path.join(ail_root, "corpus")
    for name in sorted(os.listdir(corpus)):
        base = os.path.join(corpus, name, name)
        if os.path.isfile(base + ".ail"):
            py = read(base + ".py") if os.path.isfile(base + ".py") else None
            out = read(base + ".out") if os.path.isfile(base + ".out") else None
            progs.append(("corpus/" + name, "corpus", name, read(base + ".ail"), py, out))
    extra = os.path.join(ROOT, "data", "extra")
    for grp in sorted(os.listdir(extra)):
        gdir = os.path.join(extra, grp)
        if not os.path.isdir(gdir):
            continue
        for name in sorted(os.listdir(gdir)):
            base = os.path.join(gdir, name, name)
            if os.path.isfile(base + ".ail"):
                py = read(base + ".py") if os.path.isfile(base + ".py") else None
                out = read(base + ".out") if os.path.isfile(base + ".out") else None
                src = "drills" if grp == "drills" else "extra"
                progs.append(("extra/{}/{}".format(grp, name), src, name, read(base + ".ail"), py, out))
    ex = os.path.join(ail_root, "examples")
    for f in sorted(os.listdir(ex)):
        stem, ext = os.path.splitext(f)
        if ext != ".ail" or os.path.exists(os.path.join(ex, stem + ".rules")):
            continue
        out_path = os.path.join(ex, stem + ".out")
        out = read(out_path) if os.path.isfile(out_path) else None
        progs.append(("examples/" + stem, "examples", stem, read(os.path.join(ex, f)), None, out))
    return progs


def case_sources(ail_root):
    """tests/cases programs with an expected output and nothing else (no args, stdin, expected errors)."""
    cases = os.path.join(ail_root, "tests", "cases")
    stems = {}
    for f in os.listdir(cases):
        stem, ext = os.path.splitext(f)
        stems.setdefault(stem, set()).add(ext)
    out = []
    for stem in sorted(stems):
        exts = stems[stem]
        if ".ail" not in exts or ".out" not in exts or exts & SKIP_CASE_EXT:
            continue
        if stem.startswith(("fuzz", "limit")):
            continue
        out.append(("cases/" + stem, "cases", stem, read(os.path.join(cases, stem + ".ail")), None,
                    read(os.path.join(cases, stem + ".out"))))
    return out


def mistake_sources(ail_root):
    d = os.path.join(ail_root, "tests", "mistakes")
    out = []
    for f in sorted(os.listdir(d)):
        stem, ext = os.path.splitext(f)
        if ext == ".ail" and os.path.isfile(os.path.join(d, stem + ".fixed")):
            rules = read(os.path.join(d, stem + ".rules")).split() if os.path.isfile(
                os.path.join(d, stem + ".rules")) else []
            out.append(("mistakes/" + stem, stem, read(os.path.join(d, f)), read(os.path.join(d, stem + ".fixed")),
                        rules))
    return out


def task_seeds(ail_root):
    """agentbench change tasks: id -> (issue text, seed files)."""
    tdir = os.path.join(ail_root, "tools", "agentbench", "tasks")
    out = {}
    for t in sorted(os.listdir(tdir)):
        issue = os.path.join(tdir, t, "issue.md")
        seed = os.path.join(tdir, t, "seed", "ail")
        if not (os.path.isfile(issue) and os.path.isdir(seed)):
            continue
        files = {}
        for dp, _, fs in os.walk(seed):
            for f in fs:
                if f.endswith(".ail"):
                    full = os.path.join(dp, f)
                    files[os.path.relpath(full, seed)] = read(full)
        out[t] = (read(issue), files)
    return out


# ---------------------------------------------------------------- helpers


def function_cut(src, key):
    """Remove one whole top-level function (not main, not a test): (program without it, signature, function) or None.
    AIL resolves top-level names in any order, so the function can be written back anywhere in the file."""
    lines = src.split("\n")
    cands = []
    i = 0
    while i < len(lines):
        m = re.match(r"^fn ([A-Za-z_][A-Za-z0-9_]*)\(", lines[i])
        if m:
            j = i + 1
            while j < len(lines) and (lines[j].startswith(" ") or lines[j].strip() == ""):
                j += 1
            k = j
            while k > i + 1 and lines[k - 1].strip() == "":
                k -= 1
            is_test = i > 0 and lines[i - 1].strip().startswith("@test")
            if m.group(1) != "main" and not is_test and 3 <= k - (i + 1) <= 25:
                cands.append((i, k, j))
            i = j
        else:
            i += 1
    if not cands:
        return None
    i, k, j = sorted(cands, key=lambda c: sha(key, "function", str(c[0])))[0]
    rest = "\n".join(lines[:i] + lines[j:]).rstrip("\n") + "\n"
    return rest, lines[i].strip(), "\n".join(lines[i:k])


def complete_cut(src, key):
    """Remove one top-level, non-test, non-main function body. Returns (prompt_src, fn_name, body) or None."""
    lines = src.split("\n")
    cands = []
    i = 0
    while i < len(lines):
        m = re.match(r"^fn ([A-Za-z_][A-Za-z0-9_]*)\(", lines[i])
        if m:
            j = i + 1
            while j < len(lines) and (lines[j].startswith(" ") or lines[j].strip() == ""):
                j += 1
            k = j
            while k > i + 1 and lines[k - 1].strip() == "":
                k -= 1
            is_test = i > 0 and lines[i - 1].strip().startswith("@test")
            n = k - (i + 1)
            if m.group(1) != "main" and not is_test and 2 <= n <= 30:
                cands.append((i, k, m.group(1)))
            i = j
        else:
            i += 1
    if not cands:
        return None
    i, k, name = sorted(cands, key=lambda c: sha(key, c[2]))[0]
    body = "\n".join(lines[i + 1:k])
    prompt = "\n".join(lines[:i + 1] + ["    ⟨BODY⟩"] + lines[k:])
    return prompt, name, body


# Mistakes the agent drafts made (data/raw/draft-error-lines.txt) and names from other languages, as one-line edits.
# Each is (name, regex on one line, replacement). An injected item is kept only when `ail check` then fails.
MUTATIONS = [
    ("to_lower", r"\.to_lower\(", ".lower("),
    ("to_upper", r"\.to_upper\(", ".upper("),
    ("to_int", r"\.to_int\(", ".parse_int("),
    ("trim", r"\.trim\(\)", ".strip()"),
    ("len", r"\.len\(\)", ".length()"),
    ("starts_with", r"\.starts_with\(", ".startswith("),
    ("ends_with", r"\.ends_with\(", ".endswith("),
    ("push", r"\.push\(", ".append("),
    ("contains", r"\.contains\(", ".includes("),
    ("try", r"\)\?$", ")"),
    ("elif", r"^(\s*)elif ", r"\1else if "),
    ("and", r"^(\s*(?:if|elif|while) .*) and ", r"\1 && "),
    ("or", r"^(\s*(?:if|elif|while) .*) or ", r"\1 || "),
    ("not", r"^(\s*(?:if|elif|while) )not ", r"\1!"),
    ("true", r"\btrue\b", "True"),
    ("param_colon", r"^(fn [A-Za-z_][A-Za-z0-9_.]*\()([a-z_][a-z0-9_]*) ([A-Z])", r"\1\2: \3"),
    ("arrow", r"^(fn [^\n]*\)) ([A-Z][A-Za-z0-9_\[\], ?!]*)$", r"\1 -> \2"),
    ("interp", r"\"\{([a-z_][a-z0-9_]*)\}", r'"${\1}'),
    ("bind", r"^(\s*)([a-z_][a-z0-9_]*) := ", r"\1\2 = "),
    ("mut_arg", r"\(mut ([a-z_][a-z0-9_]*)\)", r"(\1)"),
]


def inject(src, key):
    """One mutated variant of SRC: (mutated source, 1-based line number, original line), or None."""
    lines = src.split("\n")
    cands = []
    for name, pat, rep in MUTATIONS:
        rx = re.compile(pat)
        for i, line in enumerate(lines):
            if line.lstrip().startswith("#") or not rx.search(line):
                continue
            new = rx.sub(rep, line, count=1)
            if new != line:
                cands.append((sha(key, name, str(i)), i, new))
    if not cands:
        return None
    _, i, new = sorted(cands)[0]
    out = list(lines)
    out[i] = new
    return "\n".join(out), i + 1, lines[i]


def cursor_cuts(src, key):
    """Up to two fill-in-the-middle cuts inside function bodies: the rest of one line, and a run of 1 to 5 lines.
    Returns [(kind, prefix, middle, suffix)]."""
    lines = src.split("\n")
    body = [i for i, l in enumerate(lines) if l.startswith("    ") and l.strip() and not l.strip().startswith("#")]
    if not body:
        return []
    out = []
    i = sorted(body, key=lambda j: sha(key, "line", str(j)))[0]
    line = lines[i]
    indent = len(line) - len(line.lstrip())
    stops = [m.start() for m in re.finditer(r"[ (.,\[]", line[indent:])]
    stops = [indent + k + 1 for k in stops if indent + k + 1 < len(line)]
    if stops:
        cut = sorted(stops, key=lambda k: sha(key, "col", str(k)))[0]
        prefix = "\n".join(lines[:i] + [line[:cut]])
        suffix = "\n".join(lines[i + 1:])
        out.append(("line", prefix, line[cut:], "\n" + suffix))
    starts = sorted(body, key=lambda j: sha(key, "block", str(j)))
    for j in starts[:5]:
        n = 1 + int(sha(key, "n", str(j))[:2], 16) % 5
        run = [k for k in range(j, min(j + n, len(lines))) if k in set(body)]
        if run and run == list(range(j, j + len(run))):
            k = j + len(run)
            prefix = "\n".join(lines[:j]) + "\n"
            middle = "\n".join(lines[j:k]) + "\n"
            suffix = "\n".join(lines[k:])
            out.append(("block", prefix, middle, suffix))
            break
    return out


def grams(text, n=8):
    toks = re.findall(r"[A-Za-z_][A-Za-z0-9_]*|\d+|\S", text)
    return {" ".join(toks[i:i + n]) for i in range(max(0, len(toks) - n + 1))}


def pick(group, seed, pct):
    return int(sha(str(seed), group)[:8], 16) % 1000 < pct * 10


def first_error_line(out, rule):
    for line in out.splitlines():
        if "error[{}]".format(rule) in line:
            return line.strip()
    return None


# ---------------------------------------------------------------- build


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--ail", required=True)
    ap.add_argument("--out", default=os.path.join(ROOT, "data", "build"))
    ap.add_argument("--system", default="short")
    ap.add_argument("--tokenizer", default="")
    ap.add_argument("--max-tokens", type=int, default=2048)
    ap.add_argument("--jobs", type=int, default=4)
    ap.add_argument("--seed", type=int, default=20261121)
    args = ap.parse_args()

    ail_root = os.path.abspath(args.ail)
    want = read(os.path.join(ROOT, ".ail-version")).strip()
    comp = Compiler(ail_root, args.jobs)
    if comp.commit != want:
        sys.exit("the ail checkout is at {}, but .ail-version pins {}".format(comp.commit, want))
    if args.system == "short":
        system = read(SHORT_SYSTEM).strip()
    elif args.system == "core":
        system = read(os.path.join(ail_root, "docs", "language-card-core.md"))
    else:
        system = read(args.system)

    dropped = []

    def drop(item_id, reason):
        dropped.append({"id": item_id, "reason": reason})

    progs = program_sources(ail_root)
    cases = case_sources(ail_root)
    mistakes = mistake_sources(ail_root)
    seeds = task_seeds(ail_root)
    trials = [json.loads(l) for l in open(os.path.join(ROOT, "data", "raw", "trials.jsonl"), encoding="utf-8")]
    drafts = [json.loads(l) for l in open(os.path.join(ROOT, "data", "raw", "drafts.jsonl"), encoding="utf-8")]

    # 1. Compiler jobs.
    jobs = []
    for g, _, name, src, _, out in progs + cases:
        files = {name + ".ail": src}
        jobs.append(("check:" + g, files, ["check", "--no-fix"], name + ".ail"))
        if out is not None:
            jobs.append(("run:" + g, files, ["run"], name + ".ail"))
    injected = {}
    for g, source, name, src, _, _ in progs:
        v = inject(src, g)
        if v:
            injected[g] = v
            jobs.append(("inject:" + g, {"main.ail": v[0]}, ["check", "--no-fix"], "main.ail"))
    for g, name, bad, fixed, _ in mistakes:
        jobs.append(("check:" + g, {"main.ail": bad}, ["check", "--no-fix"], "main.ail"))
        jobs.append(("fixed:" + g, {"main.ail": fixed}, ["check", "--no-fix"], "main.ail"))
    for t in trials:
        tid = "trials/{}/{}/{}".format(t["run"], t["task"], t["trial"])
        jobs.append(("check:" + tid, t["files"], ["check", "--no-fix"], "src/main.ail"))
    for d in drafts:
        jobs.append(("check:drafts/" + d["key"], {"src/main.ail": d["source"]}, ["check", "--no-fix"],
                     "src/main.ail"))
    print("compiler: {} jobs on ail {}".format(len(jobs), comp.commit[:9]), file=sys.stderr)
    res = comp.many(jobs)

    items = []  # dicts: id, group, family, source, prog (text for the 8-gram filter), messages

    def add(item_id, group, family, source, prog, user, assistant):
        items.append({"id": item_id, "group": group, "family": family, "source": source, "prog": prog,
                      "messages": [{"role": "system", "content": system}, {"role": "user", "content": user},
                                   {"role": "assistant", "content": assistant}]})

    diag_lines = {}  # rule -> first diagnostic line seen, for the explain family

    # 2. Programs: write, port, complete, cursor (fill in the middle) and fixline (an injected mistake).
    for g, source, name, src, py, out in progs + cases:
        c = res["check:" + g]
        if c["rc"] != 0:
            drop(g, "check failed")
            continue
        if out is not None and res["run:" + g]["stdout"] != out:
            drop(g, "output differs")
            continue
        if source != "cases":
            task = header_text(src)
            if task:
                add("write:" + g, g, "write", source, src, task, fence(src))
            elif out is not None:
                add("write:" + g, g, "write", source, src,
                    "Write an AIL program that prints exactly:\n\n```\n{}```".format(out), fence(src))
            if py is not None:
                add("port:" + g, g, "port", source, src,
                    "Port this Python program to AIL.\n\n```python\n{}\n```".format(py.rstrip("\n")), fence(src))
        if source != "cases":
            cuts = cursor_cuts(src, g)
            # One cut per program keeps the epoch near one night on the Mac; alternate the kind by hash.
            cuts = sorted(cuts, key=lambda c: sha(g, "kind", c[0]))[:1]
            for kind, prefix, middle, suffix in cuts:
                add("cursor-{}:{}".format(kind, g), g, "cursor", source, src,
                    "Fill in the AIL code at \u27e8FILL\u27e9.\n\n```ail\n{}\u27e8FILL\u27e9{}\n```".format(prefix, suffix),
                    "```ail\n{}\n```".format(middle.rstrip("\n")) if kind == "block" else "```ail\n{}\n```".format(middle))
            if g in injected:
                bad, n, orig = injected[g]
                c = res["inject:" + g]
                if c["rc"] == 0:
                    drop("inject:" + g, "injected mistake still passes check")
                else:
                    for r in RULE.findall(c["out"]):
                        diag_lines.setdefault(r, first_error_line(c["out"], r))
                    add("fixline:" + g, g, "fixline", source, src,
                        "This AIL program fails `ail check`:\n\n{}\n\n```\n{}\n```\n\nGive the corrected line.".format(
                            fence(bad, "main.ail"), c["out"].strip()),
                        "Line {}:\n```ail\n{}\n```".format(n, orig))
        fc = function_cut(src, g) if source != "cases" else None
        if fc:
            rest, sig, fn_src = fc
            add("function:" + g, g, "function", source, src,
                "This AIL program needs the function `{}`, which is missing. Write it.\n\n{}".format(sig, fence(rest)),
                fence(fn_src))
        cut = complete_cut(src, g)
        if cut:
            prompt, fn, body = cut
            add("complete:" + g, g, "complete", source, src,
                "Write the body of `fn {}` in this AIL program; it is marked ⟨BODY⟩.\n\n{}".format(
                    fn, fence(prompt)), fence(body))

    # 3. Mistakes: fix.
    for g, name, bad, fixed, rules in mistakes:
        c, f = res["check:" + g], res["fixed:" + g]
        if c["rc"] == 0:
            drop(g, "mistake now passes check")
            continue
        if f["rc"] != 0:
            drop(g, "fixed version fails check")
            continue
        found = RULE.findall(c["out"])
        if rules and not set(rules) & set(found):
            drop(g, "check no longer reports the listed rule")
            continue
        for r in found:
            diag_lines.setdefault(r, first_error_line(c["out"], r))
        add("fix:" + g, g, "fix", "mistakes", fixed,
            "This AIL program fails `ail check`:\n\n{}\n\n```\n{}\n```\n\nFix it.".format(
                fence(bad, "main.ail"), c["out"].strip()), fence(fixed, "main.ail"))

    # 4. Agent trials: write (spec) and change (issue + seed).
    good = {}
    seen = set()
    for t in trials:
        tid = "trials/{}/{}/{}".format(t["run"], t["task"], t["trial"])
        group = "task/" + t["task"]
        if not t["metrics"].get("correct"):
            drop(tid, "trial not correct")
            continue
        if res["check:" + tid]["rc"] != 0:
            drop(tid, "check failed")
            continue
        key = sha(json.dumps(t["files"], sort_keys=True))
        if key in seen:
            drop(tid, "duplicate of another trial")
            continue
        seen.add(key)
        if len(t["files"]) == 1:
            good.setdefault(t["task"], []).append(t["files"]["src/main.ail"])
        prog = "\n".join(t["files"][p] for p in sorted(t["files"]))
        if t["task"] in seeds:
            issue, seed = seeds[t["task"]]
            seed_files = seed  # paths relative to seed/ail, so they start with src/ like the trial's
            changed = {p: s for p, s in t["files"].items() if seed_files.get(p) != s}
            if not changed:
                drop(tid, "no file changed")
                continue
            add("change:" + tid, group, "change", "trials", prog,
                "{}\n\nThe program's files:\n\n{}\n\nMake the change. Answer with every file you change, in full.".format(
                    issue.strip(), files_block(seed_files)), files_block(changed))
        else:
            add("write:" + tid, group, "write", "trials", prog, t["spec"].strip(),
                fence(t["files"]["src/main.ail"]) if len(t["files"]) == 1 else files_block(t["files"]))

    # 5. Agent drafts: fix, toward the closest correct single-file final of the same task.
    for d in drafts:
        did = "drafts/" + d["key"]
        c = res["check:" + did]
        if c["rc"] == 0:
            drop(did, "draft now passes check")
            continue
        # Pick the closest final by lines (character matching costs ~1 s per pair, hours in all),
        # then apply the character ratio threshold to that one.
        best, ratio = None, 0.0
        dl = d["source"].splitlines()
        for final in good.get(d["task"], []):
            r = difflib.SequenceMatcher(None, dl, final.splitlines(), autojunk=False).ratio()
            if r > ratio:
                best, ratio = final, r
        if best is not None:
            ratio = difflib.SequenceMatcher(None, d["source"], best, autojunk=False).ratio()
        if best is None or ratio < 0.85:
            drop(did, "no correct final close to the draft")
            continue
        for r in RULE.findall(c["out"]):
            diag_lines.setdefault(r, first_error_line(c["out"], r))
        add("fix:" + did, "task/" + d["task"], "fix", "drafts", best,
            "This AIL program fails `ail check`:\n\n{}\n\n```\n{}\n```\n\nFix it.".format(
                fence(d["source"], "src/main.ail"), c["out"].strip()), fence(best, "src/main.ail"))

    # 6. Explain: one item per rule seen in a fix item.
    ex_jobs = [("explain:" + r, {}, ["explain", r], None) for r in sorted(diag_lines) if diag_lines[r]]
    ex_res = comp.many(ex_jobs)
    for r in sorted(diag_lines):
        e = ex_res.get("explain:" + r)
        if not diag_lines[r] or not e or e["rc"] != 0 or not e["stdout"].strip():
            drop("explain:" + r, "no explain text")
            continue
        text = e["stdout"].strip()
        if len(text) > 1500:
            text = text[:1500].rsplit("\n", 1)[0]
        add("explain:" + r, "rule/" + r, "explain", "explain", "",
            "Explain this AIL diagnostic and how to fix it:\n\n```\n{}\n```".format(diag_lines[r]), text)

    # 7. Splits by group.
    def split_of(it):
        g = it["group"]
        if g.startswith("corpus/") and pick(g, args.seed, 10):
            return "quick-eval"
        if g.startswith("mistakes/") and pick(g, args.seed, 10):
            return "quick-eval"
        if g.startswith(("task/", "rule/")):
            return "train"
        return "valid" if pick(g, args.seed + 1, 5) else "train"

    for it in items:
        it["split"] = split_of(it)

    # 8. Near-duplicate filter against quick-eval programs.
    index = {}
    eval_groups = sorted({it["group"] for it in items if it["split"] == "quick-eval"})
    eval_prog = {}
    for it in items:
        if it["split"] == "quick-eval" and it["prog"]:
            eval_prog.setdefault(it["group"], it["prog"])
    for g in eval_groups:
        for h in grams(eval_prog.get(g, "")):
            index.setdefault(h, set()).add(g)
    kept = []
    for it in items:
        if it["split"] != "quick-eval" and it["prog"]:
            gs = grams(it["prog"])
            if gs:
                counts = {}
                for h in gs:
                    for g in index.get(h, ()):
                        counts[g] = counts.get(g, 0) + 1
                worst = max(counts.values()) if counts else 0
                if worst / len(gs) > 0.30:
                    drop(it["id"], "near-duplicate of a quick-eval program")
                    continue
        kept.append(it)

    # 9. Token lengths.
    tok = None
    if args.tokenizer:
        from transformers import AutoTokenizer

        tok = AutoTokenizer.from_pretrained(args.tokenizer)

    def length(msgs):
        if tok is None:
            return int(sum(len(m["content"]) for m in msgs) / 3.35) + 12
        ids = tok.apply_chat_template(msgs, tokenize=True)
        if not isinstance(ids, list):
            ids = ids["input_ids"]
        return len(ids)

    final = []
    for it in kept:
        n = length(it["messages"])
        if n > args.max_tokens:
            drop(it["id"], "longer than {} tokens".format(args.max_tokens))
            continue
        it["tokens"] = n
        final.append(it)

    # 10. Write.
    os.makedirs(args.out, exist_ok=True)
    manifest = {
        "ail_commit": comp.commit,
        "ail_train_commit": subprocess.run(["git", "-C", ROOT, "rev-parse", "HEAD"], capture_output=True,
                                           text=True).stdout.strip(),
        "seed": args.seed,
        "system": args.system if args.system in ("short", "core") else os.path.basename(args.system),
        "system_sha256": sha(system),
        "max_tokens": args.max_tokens,
        "tokens_measured": tok is not None,
        "splits": {},
        "dropped_counts": {},
        "dropped": sorted(dropped, key=lambda d: (d["reason"], d["id"])),
        "quick_eval_groups": eval_groups,
    }
    for d in dropped:
        manifest["dropped_counts"][d["reason"]] = manifest["dropped_counts"].get(d["reason"], 0) + 1
    for split in ("train", "valid", "quick-eval"):
        rows = sorted((it for it in final if it["split"] == split), key=lambda it: it["id"])
        with open(os.path.join(args.out, split + ".jsonl"), "w", encoding="utf-8") as f:
            for it in rows:
                f.write(json.dumps({"messages": it["messages"]}, ensure_ascii=False) + "\n")
        fam, src = {}, {}
        for it in rows:
            for table, k in ((fam, it["family"]), (src, it["source"])):
                e = table.setdefault(k, {"items": 0, "tokens": 0})
                e["items"] += 1
                e["tokens"] += it["tokens"]
        manifest["splits"][split] = {"items": len(rows), "tokens": sum(it["tokens"] for it in rows),
                                     "families": fam, "sources": src}
    with open(os.path.join(args.out, "manifest.json"), "w", encoding="utf-8") as f:
        json.dump(manifest, f, indent=1, sort_keys=True, ensure_ascii=False)
        f.write("\n")
    summary = {s: v["items"] for s, v in manifest["splits"].items()}
    print(json.dumps({"splits": summary, "families": manifest["splits"]["train"]["families"],
                      "dropped": manifest["dropped_counts"]}, indent=1, sort_keys=True))


if __name__ == "__main__":
    main()
