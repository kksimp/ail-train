"""Run 3 families for tools/build_data.py (whole programs, real code, correction and behaviour).

- appfn: a documented top-level function of a real AIL package (data/apps.lock repos and the pinned ail tree's
  compiler/, std/, tools/), written from its file's context: use lines, types, the other signatures, the bodies of the
  same-file functions it calls, its doc comment and signature.
- appfile: a whole file of a real package (at most ~2,200 tokens) from its header comment, its public outline and the
  public outlines of the local modules it uses.
- testfn: a program or package file with one function removed; the @test functions in it call it and pass.
- repair: the exact correction prompt of tools/eval_loop.py (imported, not retyped) for a program that fails
  `ail check`, answered with the whole corrected program. Sources: repair-mut (1 to 4 injected mistakes of the kinds
  the model really makes), repair-draft (agent drafts joined to their own trial's final), repair-harvest (the model's
  own failing drafts on train tasks, phase 3).
- behave: a program that passes `ail check` but prints the wrong output, with the task's expected output and the
  actual output, answered with the corrected program. Sources: behave-mut (semantic edits of training programs),
  behave-harvest (phase 3).

Every item here is train-only: its group starts with apps/, repair/ or behave/, which tools/build_data.py never puts
in valid or quick-eval, and it is built only from train-split programs (or real app code), never from quick-eval,
valid or dev-spec programs. Every compiler verdict comes from the pinned compiler.
"""

import difflib
import hashlib
import json
import os
import re
import shutil
import subprocess
import tempfile

from eval_loop import correction_prompt  # the arm B prompt, word for word

TOK = 3.35  # characters per token, for budgets
APPFN_PROMPT_CHARS = int(2200 * TOK)
APPFILE_MAX_CHARS = int(2200 * TOK)
APPFILE_OUTLINE_CHARS = int(1400 * TOK)
TESTFN_MAX_CHARS = int(3000 * TOK)
BEHAVE_OUT_CAP = 1500
APPFN_CAP_COMPILER, APPFN_CAP_REPO, APPFN_TOTAL = 1000, 400, 3000
APPFILE_CAP_REPO, APPFILE_TOTAL = 120, 350
TESTFN_TOTAL = 700
REPAIR_MUT_TOTAL, BEHAVE_MUT_TOTAL = 2000, 1500
REPEAT_NOTE = "The previous revision failed with the same rule ({}); change the approach instead of repeating it."
RULE = re.compile(r"error\[([a-z][a-z0-9_]*(?:\.[a-z0-9_]+)+)\]")


def sha(*parts):
    h = hashlib.sha256()
    for p in parts:
        h.update(p.encode("utf-8") if isinstance(p, str) else p)
        h.update(b"\0")
    return h.hexdigest()


def fence(src):
    return "```ail\n{}\n```".format(src.rstrip("\n"))


def ntok(text):
    return len(text) / TOK


# ---------------------------------------------------------------- AIL top-level items

FN = re.compile(r"^(?:@[a-z_]+(?:\([^)]*\))? )*(pub )?fn ([A-Za-z_][A-Za-z0-9_.]*)\s*[(\[]")
TYPE = re.compile(r"^(pub )?(?:error enum|struct|enum|trait|union|type) ([A-Za-z_][A-Za-z0-9_]*)")
CONST = re.compile(r"^(pub )?([A-Za-z_][A-Za-z0-9_]*) :?= ")


def top_items(src):
    """Top-level items of an AIL file: dicts with kind (fn, test, type, const, use, impl, other), name, doc (list of
    `##` lines), attrs, sig (the signature lines), body (lines), start (first doc/attr line), head, end (exclusive)."""
    lines = src.split("\n")
    out = []
    i = 0
    while i < len(lines):
        line = lines[i]
        if not line or line[0] in " \t#" or (line.startswith("@") and " fn " not in line and " pub fn " not in line):
            i += 1
            continue
        a = i
        while a > 0 and lines[a - 1].startswith("@"):
            a -= 1
        d = a
        while d > 0 and lines[d - 1].startswith("##"):
            d -= 1
        depth, k = 0, i
        while True:
            code = re.sub(r'"(?:[^"\\]|\\.)*"', '""', lines[k])
            depth += code.count("(") + code.count("[") - code.count(")") - code.count("]")
            if depth <= 0 or k + 1 >= len(lines) or k - i > 20:
                break
            k += 1
        e = k + 1
        while e < len(lines) and (lines[e].startswith((" ", "\t")) or lines[e].strip() == ""):
            e += 1
        end = e
        while end > k + 1 and lines[end - 1].strip() == "":
            end -= 1
        attrs = lines[a:i] + ([line.split(" fn ")[0]] if line.startswith("@") else [])
        m = FN.match(line)
        if m:
            kind = "test" if any(x.startswith("@test") for x in attrs) else "fn"
            name = m.group(2)
        elif line.startswith("use "):
            kind, name = "use", line[4:].strip()
        elif line.startswith("impl"):
            kind, name = "impl", line
        elif TYPE.match(line):
            kind, name = "type", TYPE.match(line).group(2)
        elif CONST.match(line):
            kind, name = "const", CONST.match(line).group(2)
        else:
            kind, name = "other", line
        out.append({"kind": kind, "name": name, "pub": line.startswith("pub ") or " pub fn " in line,
                    "doc": lines[d:a], "attrs": attrs, "sig": lines[i:k + 1], "body": lines[k + 1:end],
                    "start": d, "head": i, "end": end})
        i = e
    return out


def lines_attr(it):
    """Attribute lines that stand on their own line (an inline `@test fn` keeps its attribute in the signature)."""
    return [x for x in it["attrs"] if not it["sig"] or not it["sig"][0].startswith(x)]


def fn_text(it):
    return "\n".join(lines_attr(it) + it["sig"] + it["body"])


def header_doc(src):
    out = []
    for line in src.split("\n"):
        if line.startswith("##"):
            out.append(line)
        elif line.strip() == "" and not out:
            continue
        else:
            break
    return out


def calls(body_text, names):
    return [n for n in names if re.search(r"(?<![A-Za-z0-9_.])" + re.escape(n) + r"\(", body_text)]


# ---------------------------------------------------------------- packages

def app_packages(ail_root, apps_dir, lock_path):
    """Real AIL code: [(repo, root dir, entry file or None for many programs)]. Checks the clones against the lock."""
    pk = []
    for line in open(lock_path, encoding="utf-8"):
        if not line.strip() or line.startswith("#"):
            continue
        d, _, commit, entry = line.rstrip("\n").split("\t")
        root = os.path.join(apps_dir, d)
        got = subprocess.run(["git", "-C", root, "rev-parse", "HEAD"], capture_output=True, text=True).stdout.strip()
        if got != commit:
            raise SystemExit("apps: {} is at {!r}, data/apps.lock pins {}".format(root, got, commit))
        pk.append((d, root, entry))
    pk.append(("ail-compiler", ail_root, "compiler/main.ail"))
    return pk


def ail_files(root, sub=""):
    out = {}
    base = os.path.join(root, sub)
    for dp, dns, fs in os.walk(base):
        dns[:] = sorted(x for x in dns if x != ".git")
        for f in sorted(fs):
            if f.endswith(".ail") or f == "ail.pkg":
                full = os.path.join(dp, f)
                with open(full, encoding="utf-8") as fh:
                    out[os.path.relpath(full, root)] = fh.read()
    return out


class AppRunner:
    """`ail check` / `ail test` on a scratch copy of a whole package, cached by content like the builder's Compiler."""

    def __init__(self, ail, commit, cache):
        self.ail, self.commit, self.cache = ail, commit, cache

    def run(self, root, files, cmd, entry, timeout=1200):
        key = sha("app", self.commit, json.dumps(files, sort_keys=True), json.dumps(cmd), entry)
        path = os.path.join(self.cache, key + ".json")
        try:
            with open(path, encoding="utf-8") as f:
                return json.load(f)
        except (OSError, ValueError):
            pass
        tmp = tempfile.mkdtemp(prefix="ailapp-")
        try:
            dst = os.path.join(tmp, "pkg")
            shutil.copytree(root, dst, ignore=shutil.ignore_patterns(".git"))
            env = dict(os.environ, AIL_FIX="0")
            try:
                r = subprocess.run([self.ail] + cmd + [entry], cwd=dst, capture_output=True, text=True, env=env,
                                   timeout=timeout, stdin=subprocess.DEVNULL)
                res = {"rc": r.returncode, "out": ((r.stdout or "") + (r.stderr or "")).replace(dst + "/", "")}
            except subprocess.TimeoutExpired:
                res = {"rc": -1, "out": "timeout"}
        finally:
            shutil.rmtree(tmp, ignore_errors=True)
        if res["out"] != "timeout":
            with open(path + ".part", "w", encoding="utf-8") as f:
                json.dump(res, f)
            os.replace(path + ".part", path)
        return res


ERR_FILE = re.compile(r"^(?:\./)?([^\s:]+\.ail):\d+:\d+: error\[", re.M)
TEST_OK = re.compile(r"^ok ([A-Za-z0-9_.]+)\s*$", re.M)


def usable_files(repo, root, entry, files, runner, comp_tools, notes):
    """Files whose code the pinned compiler accepts. A package that fails check loses its failing files and, for a
    failing file, every file that uses its module (its own directory's module name). Pinned tools/ programs are
    checked one by one (comp_tools: path -> passed)."""
    if repo == "ail-compiler":
        keep = {}
        for p, s in files.items():
            if p.startswith(("compiler/", "std/")) or (p.startswith("tools/") and comp_tools.get(p)):
                keep[p] = s
        return keep, set()
    res = runner.run(root, files, ["check", "--no-fix"], entry)
    bad = set(ERR_FILE.findall(res["out"])) if res["rc"] != 0 else set()
    if res["rc"] != 0 and not bad:
        notes.append("{}: check failed without a file position; package skipped".format(repo))
        return {}, set()
    # A failing file goes, and so does every file that imports its module directly (`use MOD`), since their check
    # result leans on it. The failing file's sibling files in the same module were checked without errors and stay.
    mods = {os.path.basename(os.path.dirname(b)) for b in bad if os.path.dirname(b)}
    drop = set(bad)
    for p, s in files.items():
        for m in mods:
            if re.search(r"^use (?:[A-Za-z_][A-Za-z0-9_]*\.)*" + re.escape(m) + r"\s*$", s, re.M):
                drop.add(p)
    if bad:
        notes.append("{}: check fails in {}; dropped {} files: {}".format(repo, sorted(bad), len(drop), sorted(drop)))
    return {p: s for p, s in files.items() if p not in drop and p.endswith(".ail")}, drop


def module_outline(root_files, path, use_name, cap):
    """Public outline of a local module `use NAME` seen from PATH: the nearest NAME/ directory upward."""
    parts = use_name.split(".")
    d = os.path.dirname(path)
    while True:
        cand = os.path.join(d, *parts) if d else os.path.join(*parts)
        mfiles = sorted(p for p in root_files if os.path.dirname(p) == cand and p.endswith(".ail"))
        if mfiles:
            break
        if not d:
            return None
        d = os.path.dirname(d)
    out = []
    for p in mfiles:
        for it in top_items(root_files[p]):
            if not it["pub"] or it["kind"] in ("test", "use", "other"):
                continue
            if it["kind"] == "type":
                out.append("\n".join(it["doc"][:1] + it["sig"] + it["body"]))
            else:
                out.append("\n".join(it["doc"][:1] + it["sig"]))
    text = "\n".join(out)
    if len(text) > cap:
        text = text[:cap].rsplit("\n", 1)[0] + "\n# ..."
    return text


# ---------------------------------------------------------------- appfn / appfile / testfn


def appfn_candidates(repo, files, seed):
    out = []
    for p in sorted(files):
        src = files[p]
        its = top_items(src)
        fns = [it for it in its if it["kind"] == "fn"]
        names = [it["name"] for it in fns]
        for it in fns:
            if it["name"] == "main" or not it["doc"] or not 4 <= len(it["body"]) <= 60:
                continue
            out.append((sha(str(seed), "appfn", repo, p, it["name"]), repo, p, it, its))
    return out


def appfn_item(repo, path, it, its):
    target = fn_text(it)
    uses = [x for x in its if x["kind"] == "use"]
    types = [x for x in its if x["kind"] in ("type", "const")]
    fns = [x for x in its if x["kind"] == "fn" and x is not it]
    used_text = "\n".join(it["sig"] + it["body"])
    callees = [x for x in fns if x["name"] in set(calls(used_text, [f["name"] for f in fns]))]
    ref_types = [x for x in types if re.search(r"\b" + re.escape(x["name"]) + r"\b", used_text)]
    other_types = [x for x in types if x not in ref_types]
    budget = APPFN_PROMPT_CHARS - len(target) // 3 - 600
    parts = {"uses": "\n".join(u["sig"][0] for u in uses), "types": [], "callees": [], "sigs": []}
    budget -= len(parts["uses"])

    def take(lst, key, render):
        nonlocal budget
        for x in lst:
            t = render(x)
            if len(t) + 2 > budget:
                continue
            parts[key].append(t)
            budget -= len(t) + 2

    take(ref_types, "types", lambda x: "\n".join(x["doc"][:1] + x["sig"] + x["body"]))
    take(callees, "callees", lambda x: "\n".join(x["doc"] + [fn_text(x)]))
    take([x for x in fns if x not in callees], "sigs", lambda x: "\n".join(x["doc"][:1] + x["sig"]))
    take(other_types, "types", lambda x: "\n".join(x["doc"][:1] + x["sig"] + x["body"]))
    ctx = "\n\n".join(x for x in [parts["uses"]] + parts["types"] if x)
    user = "In the AIL package `{}`, the file `{}` is missing one function.".format(repo, path)
    if ctx:
        user += " The file's imports and types:\n\n" + fence(ctx)
    if parts["sigs"]:
        user += "\n\nOther functions in this file (signatures):\n\n" + fence("\n".join(parts["sigs"]))
    if parts["callees"]:
        user += "\n\nFunctions it calls, in full:\n\n" + fence("\n\n".join(parts["callees"]))
    user += "\n\nWrite this function:\n\n" + fence("\n".join(it["doc"] + it["sig"]))
    return user, fence(target)


def appfile_item(repo, path, src, files):
    head = header_doc(src)
    if not head or len(src) > APPFILE_MAX_CHARS:
        return None
    its = top_items(src)
    pub = [x for x in its if x["pub"] and x["kind"] in ("fn", "type", "const")]
    outline_items = pub or [x for x in its if x["kind"] in ("fn", "type")]
    outline = []
    for x in outline_items:
        if x["kind"] == "type":
            outline.append("\n".join(x["doc"][:1] + x["sig"] + x["body"]))
        else:
            outline.append("\n".join(x["doc"][:1] + x["sig"]))
    user = "Write the AIL file `{}` of the package `{}`. Its header comment:\n\n```\n{}\n```\n\n".format(
        path, repo, "\n".join(head))
    user += ("It defines these public items:" if pub else "It defines:") + "\n\n" + fence("\n".join(outline))
    budget = APPFILE_OUTLINE_CHARS - len(user)
    mods = []
    for u in [x for x in its if x["kind"] == "use"]:
        name = u["name"].split(" ")[0]
        o = module_outline(files, path, name, max(0, min(budget, 2500)))
        if o:
            mods.append("`{}`:\n\n{}".format(name, fence(o)))
            budget -= len(o) + 40
        if budget <= 200:
            break
    if mods:
        user += "\n\nThe local modules it uses offer (public outlines):\n\n" + "\n\n".join(mods)
    user += "\n\nAnswer with the whole file."
    return user, fence(src)


def testfn_cands(key, path, src, passed):
    """(target item, prompt, answer) for each function of SRC called by a passing @test function in SRC."""
    its = top_items(src)
    tests = [x for x in its if x["kind"] == "test" and passed(x["name"])]
    fns = [x for x in its if x["kind"] == "fn" and x["name"] != "main" and 3 <= len(x["body"]) <= 40]
    if not tests or not fns or len(src) > TESTFN_MAX_CHARS:
        return []
    out = []
    lines = src.split("\n")
    for f in fns:
        callers = [t for t in tests if calls("\n".join(t["body"]), [f["name"]])]
        if not callers:
            continue
        rest = "\n".join(lines[:f["start"]] + lines[f["end"]:]).rstrip("\n") + "\n"
        rest = re.sub(r"\n{3,}", "\n\n", rest)
        doc = "\n".join(f["doc"])
        user = ("This AIL file needs the function `{}`, which is missing. The @test functions in it ({}) call it and "
                "pass with the right function.{} Write it.\n\n`{}`\n{}").format(
            f["sig"][0].strip() if len(f["sig"]) == 1 else " ".join(s.strip() for s in f["sig"]),
            ", ".join("`{}`".format(t["name"]) for t in callers[:4]),
            " Its doc comment:\n\n```\n{}\n```\n\n".format(doc) if doc else "", path, fence(rest))
        out.append((sha(key, "testfn", f["name"]), f["name"], user, fence(fn_text(f))))
    return out


# ---------------------------------------------------------------- mistakes the model really makes

# Line edits, each (name, regex, replacement). An item is kept only when the pinned check then FAILS. Names come from
# the round-0 expr.name.1 messages of the arm B digest and data/raw/draft-error-lines.txt, as habits of other
# languages, not from any test program.
REPAIR_MUTATIONS = [
    ("len_length", r"\.len\(\)", ".length()"),
    ("len_size", r"\.len\(\)", ".size()"),
    ("push_append", r"\.push\(", ".append("),
    ("contains_includes", r"\.contains\(", ".includes("),
    ("to_lower", r"\.to_lower\(", ".lower("),
    ("to_upper", r"\.to_upper\(", ".upper("),
    ("trim_strip", r"\.trim\(\)", ".strip()"),
    ("starts_with", r"\.starts_with\(", ".startswith("),
    ("ends_with", r"\.ends_with\(", ".endswith("),
    ("is_empty", r"\.is_empty\(\)", ".empty()"),
    ("sorted_sort", r"\.sorted\(\)", ".sort()"),
    ("chars", r"\.chars\(\)", ".to_chars()"),
    ("index_of", r"\.index_of\(", ".indexOf("),
    ("remove_at", r"\.remove_at\(", ".pop_at("),
    ("pad_left", r"\.pad_left\(", ".rjust("),
    ("pad_right", r"\.pad_right\(", ".ljust("),
    ("words", r"\.words\(\)", ".split_whitespace()"),
    ("join_py", r"(?<![\w.)\]])([a-z_][a-z0-9_]*)\.join\((\"[^\"]*\")\)", r"\2.join(\1)"),
    ("slice_py", r"\.slice\(([^,()]+), ([^()]+)\)", r"[\1:\2]"),
    ("to_int_call", r"\b([a-z_][a-z0-9_]*)\.to_int\(\)", r"int(\1)"),
    ("to_int_parse", r"\.to_int\(", ".parse_int("),
    ("interp_str", r"\"\{([a-z_][a-z0-9_]*)\}\"", r"str(\1)"),
    ("interp_to_string", r"\"\{([a-z_][a-z0-9_]*)\}\"", r"\1.to_string()"),
    ("drop_else", r"^(\s*(?:mut )?[a-z_][a-z0-9_]* := .+?) else [^\s].*$", r"\1"),
    ("int_float_div", r"( / )(\d+)\b(?![.\d])", r"\g<1>\2.0"),
    ("int_float_mul", r"( \* )(\d+)\b(?![.\d])", r"\g<1>\2.5"),
    ("try_nofail", r"^(\s+(?:mut )?[a-z_][a-z0-9_]* := [a-z_][a-z0-9_]*\([^()]*\))$", r"\1?"),
    ("mixed_list", r"\[(\d+), (\d+)", r'[\1, "\2"'),
    ("move_name", r"^(\s+)([a-z_][a-z0-9_]*) := ", r"\1move := "),
    ("todo_name", r"^(\s+)([a-z_][a-z0-9_]*) := ", r"\1todo := "),
    ("drop_mut", r"^(\s+)mut ([a-z_][a-z0-9_]*) := ", r"\1\2 := "),
    ("range_py", r"for ([a-z_][a-z0-9_]*) in 0\.\.([A-Za-z_][A-Za-z0-9_.()]*)$", r"for \1 in range(\2)"),
    ("incr", r"^(\s+[a-z_][a-z0-9_.]*) \+= 1$", r"\1++"),
    ("elif", r"^(\s*)elif ", r"\1else if "),
    ("and", r"^(\s*(?:if|elif|while) .*) and ", r"\1 && "),
    ("or", r"^(\s*(?:if|elif|while) .*) or ", r"\1 || "),
    ("not", r"^(\s*(?:if|elif|while) )not ", r"\1!"),
    ("true", r"\btrue\b", "True"),
    ("param_colon", r"^(fn [A-Za-z_][A-Za-z0-9_.]*\()([a-z_][a-z0-9_]*) ([A-Za-z])", r"\1\2: \3"),
    ("arrow", r"^(fn [^\n]*\)) ([A-Z][A-Za-z0-9_\[\], ?!]*)$", r"\1 -> \2"),
    ("interp_dollar", r"\"\{([a-z_][a-z0-9_]*)\}", r'"${\1}'),
    ("bind_eq", r"^(\s*)([a-z_][a-z0-9_]*) := ", r"\1\2 = "),
]


def edit_cands(src, table, skip_comments=True):
    lines = src.split("\n")
    out = []
    for name, pat, rep in table:
        rx = re.compile(pat)
        for i, line in enumerate(lines):
            if skip_comments and line.lstrip().startswith("#"):
                continue
            if not rx.search(line):
                continue
            new = rx.sub(rep, line, count=1) if isinstance(rep, str) else rep(line)
            if new is not None and new != line:
                out.append((name, i, new))
    return out


def apply_edits(src, edits):
    lines = src.split("\n")
    for _, i, new in edits:
        lines[i] = new
    return "\n".join(lines)


def mutate(src, key, n):
    """N line edits from REPAIR_MUTATIONS on distinct lines, chosen by hash; None when fewer than N are possible."""
    cands = sorted(edit_cands(src, REPAIR_MUTATIONS), key=lambda c: sha(key, c[0], str(c[1])))
    picked, lines_used, names_used = [], set(), set()
    for c in cands:
        if c[1] in lines_used or c[0] in names_used:
            continue
        picked.append(c)
        lines_used.add(c[1])
        names_used.add(c[0])
        if len(picked) == n:
            break
    return picked if len(picked) == n else None


def _width(line):
    m = re.search(r":([<>^]?)(\d+)\}", line)
    if not m:
        return None
    w = int(m.group(2))
    return line[:m.start(2)] + str(w + 1 if w < 9 else w - 1) + line[m.end(2):]


# Semantic edits for behave: the program still passes `ail check` but should print something else.
BEHAVE_MUTATIONS = [
    ("lt_le", r"^(\s*(?:if|elif|while) .*?) < ", r"\1 <= "),
    ("le_lt", r"^(\s*(?:if|elif|while) .*?) <= ", r"\1 < "),
    ("gt_ge", r"^(\s*(?:if|elif|while) .*?) > ", r"\1 >= "),
    ("ge_gt", r"^(\s*(?:if|elif|while) .*?) >= ", r"\1 > "),
    ("eq_ne", r"^(\s*(?:if|elif|while) .*?) == ", r"\1 != "),
    ("range_end", r"(in [A-Za-z0-9_.()]+\.\.)([A-Za-z_][A-Za-z0-9_.()]*|\d+)$", r"\1\2 - 1"),
    ("range_start", r"in 0\.\.", "in 1.."),
    ("width", r":[<>^]?\d+\}", _width),
    ("sep_comma", r"\.join\(\", \"\)", '.join(",")'),
    ("sep_space", r"\.join\(\" \"\)", '.join(", ")'),
    ("negate_if", r"^(\s*)if (.+)$", r"\1if not (\2)"),
    ("plus_minus", r"(\w) \+ (\w)", r"\1 - \2"),
    ("minus_plus", r"(\w) - (\w)", r"\1 + \2"),
    ("times_plus", r"(\w) \* (\w)", r"\1 + \2"),
    ("plus_one", r" \+ 1\b", " + 2"),
    ("bool_flip", r"\b(true|false)\b", lambda l: re.sub(r"\b(true|false)\b",
                                                         lambda m: "false" if m.group(1) == "true" else "true", l,
                                                         count=1)),
    ("drop_stmt", r"^\s+[a-z_][a-z0-9_.\[\]]* (?:\+|-|\*)?= .+$", lambda l: None),
    ("drop_push", r"^\s+[a-z_][a-z0-9_.\[\]]*\.push\(.+\)$", lambda l: None),
]


def behave_edit(src, key, attempt):
    """One semantic edit (name, new source) chosen by hash for ATTEMPT, or None."""
    lines = src.split("\n")
    cands = []
    for name, pat, rep in BEHAVE_MUTATIONS:
        rx = re.compile(pat)
        for i, line in enumerate(lines):
            if line.lstrip().startswith("#") or line.startswith("@") or "@test" in line or not rx.search(line):
                continue
            if callable(rep):
                new = rep(line)
                if new is None and name.startswith("drop"):
                    cands.append((name, i, None))
                    continue
            else:
                new = rx.sub(rep, line, count=1)
            if new is not None and new != line:
                cands.append((name, i, new))
    if not cands:
        return None
    # spread over kinds: pick the kind first, then the line
    kinds = sorted({c[0] for c in cands}, key=lambda k: sha(key, "bk", str(attempt), k))
    kind = kinds[0]
    name, i, new = sorted((c for c in cands if c[0] == kind), key=lambda c: sha(key, "bl", str(attempt), str(c[1])))[0]
    out = list(lines)
    if new is None:
        del out[i]
    else:
        out[i] = new
    return name, "\n".join(out)


def behave_prompt(spec_task, prog, actual, trap=""):
    shown = actual if len(actual) <= BEHAVE_OUT_CAP else actual[:BEHAVE_OUT_CAP] + "\n[... output cut ...]\n"
    user = (spec_task.rstrip() + "\n\nYour current complete program:\n\n" + fence(prog) +
            "\n\nIt passes `ail check`, but it prints:\n\n```\n" + shown.rstrip("\n") + "\n```")
    if trap:
        user += "\n\nand then stops with:\n\n```\n" + trap.strip()[:600] + "\n```"
    user += ("\n\nFix the program so it prints exactly the expected output. Answer with the whole corrected program "
             "in one ```ail block.")
    return user


def repair_prompt(task, source, diag, key, repeat_rule=None):
    rounds_left = int(sha(key, "rounds")[:4], 16) % 3
    p = correction_prompt(task, source, diag, rounds_left)
    if repeat_rule:
        p = p.replace("\nAnswer with the whole corrected program",
                      " " + REPEAT_NOTE.format(repeat_rule) + "\nAnswer with the whole corrected program", 1)
    return p


def trap_of(stderr):
    for line in (stderr or "").splitlines():
        if "trap[" in line:
            return line.strip()
    return ""


def ratio(a, b):
    return difflib.SequenceMatcher(None, a, b, autojunk=False).ratio()
