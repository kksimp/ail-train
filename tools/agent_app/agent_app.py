"""One agentic-coding test: a strong API model builds the same small app in AIL and in Python, from one spec.

Phases (each writes its result into RUN_DIR and is skipped when that result already exists, so a rerun resumes):
  1. spec   HELPER_MODEL writes a language-neutral spec, a Python reference, public and hidden stdin cases.
            The reference is run here to make the expected outputs; the builders never see it or the hidden cases.
  2. ail    BUILDER_MODEL builds work-ail/app.ail with tools: read the pinned AIL checkout and ail-train data,
            write and edit files, run `ail check|run|test|fmt|fix|explain|card`. Then it writes a self-report.
  3. py     The same builder, same spec, builds work-py/app.py with only `python3` (the comparison arm).
  4. grade  Both programs run on every public and hidden case; stdout must match exactly.
  5. judge  HELPER_MODEL reads the numbers, both programs, both self-reports and the AIL error log and writes the
            analysis. REPORT.md = numbers measured here + that analysis + both self-reports.

Spend is counted from each response's usage and capped per phase and in total (CAP_TOTAL, default 15 USD).
Model names come from config.local through the environment (no model name is written in a committed file).
"""

import hashlib
import json
import os
import re
import subprocess
import sys
import time
from pathlib import Path

import anthropic

RUN_DIR = Path(os.environ["RUN_DIR"])
AIL_ROOT = Path(os.environ["AIL_ROOT"])
TRAIN_ROOT = Path(os.environ["TRAIN_ROOT"])
BUILDER = os.environ["BUILDER_MODEL"]
HELPER = os.environ["HELPER_MODEL"]
CAP_TOTAL = float(os.environ.get("CAP_TOTAL", "15"))
CAPS = {
    "spec": float(os.environ.get("CAP_SPEC", "1.5")),
    "ail": float(os.environ.get("CAP_AIL", "6.5")),
    "py": float(os.environ.get("CAP_PY", "3.0")),
    "judge": float(os.environ.get("CAP_JUDGE", "2.0")),
}
MAX_TURNS = {"ail": int(os.environ.get("TURNS_AIL", "60")), "py": int(os.environ.get("TURNS_PY", "35"))}
REPORT_RESERVE = 0.9  # kept back in a build phase for the self-report call
MAX_OUT = 32000
BETAS = ["server-side-fallback-2026-07-01"]

# USD per million tokens: input, output, cache write (5 min), cache read. Unknown models are priced at the top row.
PRICES = {
    "fable": (8.0, 40.0, 10.0, 0.20),
    "opus-5-5": (4.0, 20.0, 5.0, 0.20),
    "opus": (5.0, 25.0, 6.25, 0.50),
    "sonnet": (3.0, 15.0, 3.75, 0.30),
}

client = anthropic.Anthropic(max_retries=4)
RUN_DIR.mkdir(parents=True, exist_ok=True)
LEDGER = RUN_DIR / "spend.json"


def log(msg):
    line = f"[{time.strftime('%H:%M:%S')}] {msg}"
    print(line, flush=True)
    with open(RUN_DIR / "progress.log", "a") as f:
        f.write(line + "\n")


def ledger():
    if LEDGER.exists():
        return json.loads(LEDGER.read_text())
    return {"total": 0.0, "phases": {}, "calls": 0}


def price_for(model):
    for key, p in PRICES.items():
        if key in model:
            return p
    return PRICES["fable"]


def charge(phase, model, usage):
    pin, pout, pcw, pcr = price_for(model)
    u = {
        "input": getattr(usage, "input_tokens", 0) or 0,
        "output": getattr(usage, "output_tokens", 0) or 0,
        "cache_write": getattr(usage, "cache_creation_input_tokens", 0) or 0,
        "cache_read": getattr(usage, "cache_read_input_tokens", 0) or 0,
    }
    cost = (u["input"] * pin + u["output"] * pout + u["cache_write"] * pcw + u["cache_read"] * pcr) / 1e6
    led = ledger()
    led["total"] += cost
    led["calls"] += 1
    ph = led["phases"].setdefault(phase, {"usd": 0.0, "input": 0, "output": 0, "cache_write": 0, "cache_read": 0, "calls": 0})
    ph["usd"] += cost
    ph["calls"] += 1
    for k, v in u.items():
        ph[k] += v
    LEDGER.write_text(json.dumps(led, indent=1))
    return cost, u


def phase_spent(phase):
    return ledger()["phases"].get(phase, {}).get("usd", 0.0)


def can_spend(phase, reserve=0.0):
    led = ledger()
    return led["total"] + reserve < CAP_TOTAL - 0.5 and phase_spent(phase) + reserve < CAPS[phase]


def call(phase, model, *, system, messages, tools=None, tool_choice=None, effort="high", output_format=None,
         max_tokens=MAX_OUT):
    """One streamed request. Returns the final message and its cost."""
    kw = dict(model=model, max_tokens=max_tokens, system=system, messages=messages, betas=BETAS,
              extra_body={"fallbacks": "default", "cache_control": {"type": "ephemeral"}})
    oc = {"effort": effort}
    if output_format:
        oc["format"] = output_format
    kw["output_config"] = oc
    if tools:
        kw["tools"] = tools
    if tool_choice:
        kw["tool_choice"] = tool_choice
    t0 = time.time()
    while True:
        try:
            with client.beta.messages.stream(**kw) as stream:
                msg = stream.get_final_message()
            break
        except anthropic.BadRequestError as e:  # a rejected request is not billed; drop the optional extras once
            text = str(e)
            extra = kw.get("extra_body", {})
            dropped = [k for k in ("fallbacks", "cache_control") if k in extra and k in text]
            if not dropped:
                raise
            for k in dropped:
                extra.pop(k)
            if "fallbacks" in dropped:
                kw["betas"] = []
            log(f"{phase}: request rejected over {dropped}; retrying without")
    cost, u = charge(phase, msg.model or model, msg.usage)
    led = ledger()
    log(f"{phase}: call {led['phases'][phase]['calls']} {time.time() - t0:.0f}s out={u['output']} "
        f"in={u['input']}+{u['cache_write']}w+{u['cache_read']}r ${cost:.3f} (phase ${phase_spent(phase):.2f}, "
        f"total ${led['total']:.2f}) stop={msg.stop_reason}")
    return msg


def text_of(msg):
    return "".join(b.text for b in msg.content if getattr(b, "type", "") == "text")


# ---------------------------------------------------------------- phase 1: spec

SPEC_SCHEMA = {
    "type": "object",
    "additionalProperties": False,
    "required": ["app_name", "spec_markdown", "python_reference", "public_cases", "hidden_cases"],
    "properties": {
        "app_name": {"type": "string"},
        "spec_markdown": {"type": "string"},
        "python_reference": {"type": "string"},
        "public_cases": {"type": "array", "items": {
            "type": "object", "additionalProperties": False, "required": ["name", "stdin"],
            "properties": {"name": {"type": "string"}, "stdin": {"type": "string"}}}},
        "hidden_cases": {"type": "array", "items": {
            "type": "object", "additionalProperties": False, "required": ["name", "stdin", "covers"],
            "properties": {"name": {"type": "string"}, "stdin": {"type": "string"}, "covers": {"type": "string"}}}},
    },
}

SPEC_PROMPT = """You are setting the task for an experiment in agentic coding. A strong coding agent will build the
same small console app twice, once in Python and once in AIL, a new systems language it has barely seen. You write
the task; you never see the agent's code. We want to learn what helps an agent write correct programs in a new
language, so the task must be fair to both languages and graded exactly.

Write a spec for one small, realistic command-line app:
- It reads all of standard input: one command or record per line. It writes only to standard output.
- A competent programmer writes it in 150 to 300 lines. It should need: records (structs), a closed set of
  kinds (an enum), a map and a list, sorting with explicit tie-breaks, parsing and validating text fields,
  error handling for bad input lines (each bad line prints a specified error line and processing continues),
  and a formatted report with fixed-width columns.
- Integers only (money in cents, quantities as whole numbers). No floating point anywhere, no dates or times,
  no randomness, no files, no environment, no command-line arguments, ASCII only, no regular expressions needed.
- Specify every output byte: exact message texts, column widths, alignment, padding, how cents print
  (for example 1234 -> "12.34", -5 -> "-0.05"), sort orders and tie-breaks, what happens on duplicates, empty
  input and unknown commands. Include one worked example (input and its exact output) in the spec.
- Pick something other than a todo list. Keep the name short.

Then write python_reference: a Python 3 (standard library only) program that implements the spec exactly,
reading sys.stdin. It is the source of truth for expected outputs, so it must follow the spec to the byte.

Then write 3 public_cases (shown to the agent with their expected output) and 8 hidden_cases (used only for
grading; each says what it covers). Hidden cases must cover the spec's edge cases: every error message, ties in
sorting, negative and zero amounts if allowed, large values (up to 10^12 cents), empty input, duplicate keys,
unusual spacing if the spec allows it. Each stdin ends with a newline unless the case is empty input.
"""


def phase_spec():
    out = RUN_DIR / "spec.json"
    if out.exists():
        return json.loads(out.read_text())
    log("spec: asking the helper model for the task")
    msg = call("spec", HELPER, system="You design fair, exactly-graded programming tasks.",
               messages=[{"role": "user", "content": SPEC_PROMPT}],
               output_format={"type": "json_schema", "schema": SPEC_SCHEMA})
    if msg.stop_reason != "end_turn":
        sys.exit(f"spec: stopped with {msg.stop_reason}")
    spec = json.loads(text_of(msg))
    ref = RUN_DIR / "reference.py"
    ref.write_text(spec["python_reference"])
    for kind in ("public_cases", "hidden_cases"):
        for case in spec[kind]:
            r = subprocess.run([sys.executable, "-I", str(ref)], input=case["stdin"], capture_output=True,
                               text=True, timeout=30)
            if r.returncode != 0:
                sys.exit(f"spec: reference failed on {case['name']}: {r.stderr[-2000:]}")
            case["expected"] = r.stdout
    out.write_text(json.dumps(spec, indent=1))
    log(f"spec: {spec['app_name']}, {len(spec['public_cases'])} public and {len(spec['hidden_cases'])} hidden cases")
    return spec


# ---------------------------------------------------------------- tools

ROOTS = {"ail": AIL_ROOT, "ail-train": TRAIN_ROOT}
SKIP_PARTS = {".git", "runs", ".venv", "__pycache__", "node_modules"}
OUT_LIMIT = 14000


def clip(s, limit=OUT_LIMIT):
    if len(s) <= limit:
        return s
    return s[:limit] + f"\n... [{len(s) - limit} more characters cut; read a narrower range]"


class Workspace:
    def __init__(self, lang):
        self.lang = lang
        self.work = RUN_DIR / f"work-{lang}"
        self.work.mkdir(exist_ok=True)
        self.roots = {"work": self.work}
        if lang == "ail":
            self.roots.update(ROOTS)
        self.events = []  # one dict per tool call

    def resolve(self, vpath, write=False):
        vpath = (vpath or "").strip().lstrip("/")
        head, _, rest = vpath.partition("/")
        if head not in self.roots:
            raise ValueError(f"paths start with one of: {', '.join(r + '/' for r in self.roots)}")
        if write and head != "work":
            raise ValueError("you can write only under work/")
        base = self.roots[head].resolve()
        p = (base / rest).resolve()
        if p != base and base not in p.parents:
            raise ValueError("path leaves its root")
        if SKIP_PARTS & set(p.relative_to(base).parts):
            raise ValueError("that folder is not available")
        return p

    @staticmethod
    def category(vpath):
        v = (vpath or "").strip().lstrip("/")
        if v.startswith("work"):
            return "own code"
        if v.startswith("ail-train"):
            return "ail-train data"
        if v.startswith("ail/docs/spec"):
            return "ail spec"
        if v.startswith("ail/docs") or v.startswith("ail/llms") or v in ("ail/README.md", "ail", "ail/"):
            return "ail docs"
        if v.startswith("ail/examples"):
            return "ail examples"
        if v.startswith("ail/tests"):
            return "ail tests"
        if v.startswith("ail/std"):
            return "ail std source"
        if v.startswith("ail/compiler"):
            return "ail compiler source"
        return "other"

    # -- tool bodies; each returns (text, is_error, extra-event-fields)

    def t_list_files(self, a):
        p = self.resolve(a.get("path", ""))
        if not p.is_dir():
            return f"not a folder: {a.get('path')}", True, {}
        names = sorted(os.listdir(p))
        rows = [n + ("/" if (p / n).is_dir() else "") for n in names if n not in SKIP_PARTS][:400]
        more = "" if len(names) <= 400 else f"\n... {len(names) - 400} more"
        return "\n".join(rows) + more, False, {}

    def t_read_file(self, a):
        p = self.resolve(a["path"])
        if not p.is_file():
            return f"no such file: {a['path']}", True, {}
        lines = p.read_text(errors="replace").splitlines()
        start = max(1, int(a.get("start_line") or 1))
        count = min(int(a.get("max_lines") or 600), 1500)
        chunk = lines[start - 1:start - 1 + count]
        body = "\n".join(f"{start + i:5} {l}" for i, l in enumerate(chunk))
        tail = f"\n[lines {start}-{start + len(chunk) - 1} of {len(lines)}]"
        return clip(body) + tail, False, {"lines": len(chunk)}

    def t_search(self, a):
        p = self.resolve(a.get("path", ""))
        cmd = ["grep", "-rIn", "-E", a["pattern"], str(p)]
        for d in SKIP_PARTS:
            cmd.insert(1, f"--exclude-dir={d}")
        r = subprocess.run(cmd, capture_output=True, text=True, timeout=60)
        base = str(self.roots[a.get("path", "").strip().lstrip("/").partition("/")[0]].resolve())
        head = a.get("path", "").strip().lstrip("/").partition("/")[0]
        out = r.stdout.replace(base, head)
        lines = out.splitlines()
        res = "\n".join(lines[:120]) + (f"\n... {len(lines) - 120} more matches" if len(lines) > 120 else "")
        return clip(res or "no matches"), False, {"matches": len(lines)}

    def t_write_file(self, a):
        p = self.resolve(a["path"], write=True)
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(a["content"])
        return f"wrote {a['path']} ({len(a['content'].splitlines())} lines)", False, {}

    def t_edit_file(self, a):
        p = self.resolve(a["path"], write=True)
        if not p.is_file():
            return f"no such file: {a['path']}", True, {}
        s = p.read_text()
        n = s.count(a["old_text"])
        if n != 1:
            return f"old_text occurs {n} times; it must occur exactly once", True, {}
        p.write_text(s.replace(a["old_text"], a["new_text"]))
        return f"edited {a['path']}", False, {}

    def t_run_ail(self, a):
        sub = a["command"]
        args = [str(AIL_ROOT / "ail"), sub]
        target = None
        if sub in ("check", "run", "test", "fmt", "fix"):
            target = self.resolve(a.get("file") or "work/app.ail", write=True)
            if sub == "run":
                args += ["--timeout", "10000", "--max-memory", "512"]
            args.append(str(target))
        elif sub == "explain":
            args.append(a.get("rule", ""))
        elif sub != "card":
            return "command must be one of check, run, test, fmt, fix, explain, card", True, {}
        before = hashlib.sha1(target.read_bytes()).hexdigest() if target and target.exists() else None
        t0 = time.time()
        try:
            r = subprocess.run(args, input=a.get("stdin", ""), capture_output=True, text=True, timeout=120,
                               cwd=self.work)
            code, out, err = r.returncode, r.stdout, r.stderr
        except subprocess.TimeoutExpired:
            code, out, err = -9, "", "timed out after 120 s"
        after = hashlib.sha1(target.read_bytes()).hexdigest() if target and target.exists() else None
        text = (out + ("\n[stderr]\n" + err if err.strip() else "")).replace(str(self.work), "work")
        text = text.replace(str(AIL_ROOT), "ail")
        rules = sorted(set(re.findall(r"error\[([a-z_]+(?:\.[a-z_0-9]+)+)\]", text)))
        changed = before is not None and before != after
        note = "\n[the compiler rewrote the file]" if changed and sub not in ("fmt", "fix") else ""
        return (clip(text or "(no output)") + f"\n[exit {code}]{note}", False,
                {"exit": code, "rules": rules, "file_changed": changed, "secs": round(time.time() - t0, 1),
                 "first_error": next((l for l in text.splitlines() if "error[" in l), "")})

    def t_run_python(self, a):
        target = self.resolve(a.get("file") or "work/app.py", write=True)
        try:
            r = subprocess.run([sys.executable, "-I", str(target)], input=a.get("stdin", ""), capture_output=True,
                               text=True, timeout=30, cwd=self.work)
            code, out, err = r.returncode, r.stdout, r.stderr
        except subprocess.TimeoutExpired:
            code, out, err = -9, "", "timed out after 30 s"
        text = (out + ("\n[stderr]\n" + err if err.strip() else "")).replace(str(self.work), "work")
        exc = re.findall(r"^(\w+(?:Error|Exception)):", err, re.M)
        return clip(text or "(no output)") + f"\n[exit {code}]", False, {"exit": code, "exceptions": exc}

    def run(self, turn, name, a):
        fn = getattr(self, "t_" + name, None)
        t0 = time.time()
        ev = {"turn": turn, "tool": name, "path": a.get("path") or a.get("file") or a.get("rule") or "",
              "command": a.get("command", "")}
        ev["category"] = self.category(ev["path"]) if name in ("list_files", "read_file", "search") else ""
        try:
            if fn is None:
                raise ValueError(f"unknown tool {name}")
            text, is_err, extra = fn(a)
        except Exception as e:  # report the failure to the model, never crash the run
            text, is_err, extra = f"error: {e}", True, {}
        ev.update(extra)
        ev["is_error"] = is_err
        ev["secs"] = ev.get("secs", round(time.time() - t0, 1))
        self.events.append(ev)
        return text, is_err


def tool_defs(lang):
    defs = []
    path_doc = ("A path such as work/app.ail, ail/docs/for-agents.md or ail-train/data/extra"
                if lang == "ail" else "A path such as work/app.py")
    if lang == "ail":
        defs += [
            {"name": "list_files", "description": "List a folder.",
             "input_schema": {"type": "object", "properties": {"path": {"type": "string", "description": path_doc}},
                              "required": ["path"]}},
            {"name": "search", "description": "grep -rn -E PATTERN under a folder or file (at most 120 matches).",
             "input_schema": {"type": "object", "properties": {
                 "pattern": {"type": "string"}, "path": {"type": "string", "description": path_doc}},
                 "required": ["pattern", "path"]}},
        ]
    defs += [
        {"name": "read_file", "description": "Read a text file with line numbers (default 600 lines from start_line).",
         "input_schema": {"type": "object", "properties": {
             "path": {"type": "string", "description": path_doc},
             "start_line": {"type": "integer"}, "max_lines": {"type": "integer"}}, "required": ["path"]}},
        {"name": "write_file", "description": "Create or replace a file under work/.",
         "input_schema": {"type": "object", "properties": {
             "path": {"type": "string"}, "content": {"type": "string"}}, "required": ["path", "content"]}},
        {"name": "edit_file", "description": "Replace old_text (must occur exactly once) with new_text in a file under work/.",
         "input_schema": {"type": "object", "properties": {
             "path": {"type": "string"}, "old_text": {"type": "string"}, "new_text": {"type": "string"}},
             "required": ["path", "old_text", "new_text"]}},
    ]
    if lang == "ail":
        defs.append({"name": "run_ail", "description": (
            "Run the AIL CLI. command: check|run|test|fmt|fix (on file, default work/app.ail), explain (rule, "
            "e.g. expr.name.1), card (prints the short language card). For run, stdin is piped to the program; "
            "the command is `ail run --timeout 10000 --max-memory 512 FILE`, exactly how it is graded."),
            "input_schema": {"type": "object", "properties": {
                "command": {"type": "string", "enum": ["check", "run", "test", "fmt", "fix", "explain", "card"]},
                "file": {"type": "string"}, "rule": {"type": "string"}, "stdin": {"type": "string"}},
                "required": ["command"]}})
    else:
        defs.append({"name": "run_python", "description": (
            "Run `python3 FILE` (default work/app.py) with stdin piped to it, exactly how it is graded."),
            "input_schema": {"type": "object", "properties": {
                "file": {"type": "string"}, "stdin": {"type": "string"}}, "required": []}})
    defs.append({"name": "finish", "description": "Call once when the program is done and you have tested it.",
                 "input_schema": {"type": "object", "properties": {"note": {"type": "string"}}, "required": []}})
    return defs


# ---------------------------------------------------------------- phases 2 and 3: build

def task_text(spec, lang):
    cases = "\n\n".join(
        f"### Public case {c['name']}\nstdin:\n```\n{c['stdin']}```\nexpected stdout:\n```\n{c['expected']}```"
        for c in spec["public_cases"])
    if lang == "ail":
        where = f"""Write the program in AIL as work/app.ail. AIL is a new language (version 0.2.0 release candidate);
you have probably seen little or none of it, so look things up rather than guess. You have:
- ail/: the AIL repository at the exact compiler version you run. Its README.md and llms.txt are the entry points;
  there are docs, examples, tests, the std library source and the compiler source.
- ail-train/: a project that teaches AIL to small models; data/extra/ holds about 2,600 compiler-checked AIL programs.
- run_ail: the real compiler (check, run, test, fmt, fix, explain RULE, card).
Use whatever helps you most; we record which resources you reach for."""
    else:
        where = "Write the program in Python 3 (standard library only) as work/app.py. run_python runs it."
    return f"""Build this console app. It is graded by running it on hidden test inputs and comparing standard output
byte for byte, so follow the spec exactly.

{where}

Test it yourself on the public cases below and on edge cases you make up from the spec. Work efficiently: you have
about {MAX_TURNS[lang] - 5} tool turns. Call finish when you are confident it is correct.

# Spec: {spec['app_name']}

{spec['spec_markdown']}

{cases}
"""


REPORT_ASK = {
    "ail": """Now write your report on this task, for the people who design AIL and teach it to models. Be concrete and
honest; name files, rule IDs and error messages. Under 900 words, these headings:
1. Result: does the program work? Your evidence.
2. What helped: the resources, compiler messages, fixes or examples that moved you forward, most useful first.
3. What did not help or misled you: wrong guesses, confusing errors, missing or wrong docs, with the exact text.
4. What would help more: specific changes to the docs, the card, the compiler's messages or tools, and the kind of
   training examples a model would need to write this app first time.
5. AIL for agentic coding: compared with writing the same app in a language you know well, where did AIL make the
   work easier or safer, and where harder? Separate what comes from the language itself from what comes from your
   unfamiliarity with it.""",
    "py": """Now write a short report (under 400 words): 1. Result and evidence. 2. What took more than one try and why.
3. Bugs you caught only by running the program, and bugs a stricter compiler could have caught before running.""",
}

BUILDER_SYSTEM = ("You are an expert software engineer working alone with the tools given. Read the task, look up what "
                  "you need, write the program, compile and test it, and fix it until it matches the spec exactly.")


def phase_build(spec, lang):
    out = RUN_DIR / f"build-{lang}.json"
    if out.exists():
        return json.loads(out.read_text())
    if not can_spend(lang, REPORT_RESERVE):
        log(f"{lang}: skipped, not enough budget left")
        return None
    ws = Workspace(lang)
    tools = tool_defs(lang)
    messages = [{"role": "user", "content": task_text(spec, lang)}]
    t0 = time.time()
    finished, nudges, turn, stop = False, 0, 0, "turns"
    transcript = RUN_DIR / f"transcript-{lang}.jsonl"
    for turn in range(1, MAX_TURNS[lang] + 1):
        if not can_spend(lang, REPORT_RESERVE):
            stop = "budget"
            break
        msg = call(lang, BUILDER, system=BUILDER_SYSTEM, messages=messages, tools=tools)
        messages.append({"role": "assistant", "content": msg.content})
        with open(transcript, "a") as f:
            f.write(json.dumps({"turn": turn, "content": [b.model_dump() for b in msg.content]}) + "\n")
        if msg.stop_reason == "refusal":
            stop = "refusal"
            break
        uses = [b for b in msg.content if getattr(b, "type", "") == "tool_use"]
        if not uses:
            nudges += 1
            if nudges > 2:
                stop = "no tool calls"
                break
            messages.append({"role": "user", "content": "Continue with the tools; call finish when the program is done."})
            continue
        results = []
        for b in uses:
            if b.name == "finish":
                finished = True
                results.append({"type": "tool_result", "tool_use_id": b.id, "content": "noted"})
                ws.events.append({"turn": turn, "tool": "finish", "note": (b.input or {}).get("note", "")})
                continue
            if msg.stop_reason == "max_tokens":
                text, err = "your reply hit the output limit, so this call was not run; send shorter steps", True
            else:
                text, err = ws.run(turn, b.name, b.input or {})
            results.append({"type": "tool_result", "tool_use_id": b.id, "content": text, "is_error": err})
        if finished:
            stop = "finished"
            messages.append({"role": "user", "content": results + [{"type": "text", "text": REPORT_ASK[lang]}]})
            break
        messages.append({"role": "user", "content": results})
        with open(RUN_DIR / f"events-{lang}.jsonl", "w") as f:
            for ev in ws.events:
                f.write(json.dumps(ev) + "\n")
    if not finished:
        ask = {"type": "text", "text": "Stop here (" + stop + "). " + REPORT_ASK[lang]}
        last = messages[-1]
        if last["role"] == "user" and isinstance(last["content"], list):
            last["content"].append(ask)
        elif last["role"] == "user":
            last["content"] = [{"type": "text", "text": last["content"]}, ask]
        else:
            pending = [b for b in last["content"] if getattr(b, "type", "") == "tool_use"]
            messages.append({"role": "user", "content": [
                {"type": "tool_result", "tool_use_id": b.id, "content": "not run: stopped", "is_error": True}
                for b in pending] + [ask]})
    report = ""
    if stop != "refusal" and ledger()["total"] < CAP_TOTAL - 0.3:
        msg = call(lang, BUILDER, system=BUILDER_SYSTEM, messages=messages, tools=tools,
                   tool_choice={"type": "none"}, max_tokens=12000)
        report = text_of(msg)
    with open(RUN_DIR / f"events-{lang}.jsonl", "w") as f:
        for ev in ws.events:
            f.write(json.dumps(ev) + "\n")
    result = {"lang": lang, "stop": stop, "turns": turn, "minutes": round((time.time() - t0) / 60, 1),
              "report": report, "metrics": metrics(ws, lang)}
    (RUN_DIR / f"self-report-{lang}.md").write_text(report)
    out.write_text(json.dumps(result, indent=1))
    log(f"{lang}: {stop} after {turn} turns, ${phase_spent(lang):.2f}")
    return result


def metrics(ws, lang):
    ev = ws.events
    m = {"tool_calls": len(ev), "by_tool": {}, "reads_by_category": {}, "files_read": {}}
    for e in ev:
        m["by_tool"][e["tool"]] = m["by_tool"].get(e["tool"], 0) + 1
        if e.get("category"):
            m["reads_by_category"][e["category"]] = m["reads_by_category"].get(e["category"], 0) + 1
        if e["tool"] == "read_file" and not e.get("is_error"):
            m["files_read"][e["path"]] = m["files_read"].get(e["path"], 0) + 1
    if lang == "ail":
        checks = [e for e in ev if e["tool"] == "run_ail" and e["command"] in ("check", "run", "test")]
        fails = [e for e in checks if e.get("rules")]
        rules = {}
        for e in fails:
            for r in e["rules"]:
                rules[r] = rules.get(r, 0) + 1
        m.update({
            "compile_runs": len(checks),
            "compile_failures": len(fails),
            "rule_ids": dict(sorted(rules.items(), key=lambda kv: -kv[1])),
            "compiler_rewrote_file": sum(1 for e in ev if e.get("file_changed") and e["command"] not in ("fmt", "fix")),
            "runtime_traps": sum(1 for e in checks if e["command"] == "run" and e.get("exit") == 1),
            "first_clean_check_turn": next((e["turn"] for e in checks if e["command"] == "check" and e.get("exit") == 0), None),
            "explain_calls": sum(1 for e in ev if e["tool"] == "run_ail" and e["command"] == "explain"),
            "error_log": [f"t{e['turn']} {e['command']}: {e.get('first_error', '')}" for e in fails][:80],
        })
    else:
        runs = [e for e in ev if e["tool"] == "run_python"]
        m.update({"runs": len(runs), "runs_with_exception": sum(1 for e in runs if e.get("exceptions")),
                  "exceptions": [x for e in runs for x in e.get("exceptions", [])]})
    return m


# ---------------------------------------------------------------- phase 4: grade

def norm(s):
    return "\n".join(l.rstrip() for l in s.rstrip("\n").splitlines())


def phase_grade(spec):
    out = RUN_DIR / "grade.json"
    grade = {}
    for lang, rel, cmd in (("ail", "work-ail/app.ail", [str(AIL_ROOT / "ail"), "run", "--timeout", "10000",
                                                        "--max-memory", "512"]),
                           ("py", "work-py/app.py", [sys.executable, "-I"])):
        prog = RUN_DIR / rel
        if not prog.exists():
            grade[lang] = {"present": False}
            continue
        rows = []
        for kind in ("public_cases", "hidden_cases"):
            for c in spec[kind]:
                try:
                    r = subprocess.run(cmd + [str(prog)], input=c["stdin"], capture_output=True, text=True,
                                       timeout=120, cwd=prog.parent)
                    got, code = r.stdout, r.returncode
                except subprocess.TimeoutExpired:
                    got, code = "", -9
                exact = got == c["expected"]
                rows.append({"kind": kind[:-6], "name": c["name"], "exact": exact,
                             "pass": exact or norm(got) == norm(c["expected"]), "exit": code,
                             "got_head": got[:600] if not exact else ""})
        src = prog.read_text()
        grade[lang] = {
            "present": True, "rows": rows,
            "public_pass": sum(r["pass"] for r in rows if r["kind"] == "public"),
            "hidden_pass": sum(r["pass"] for r in rows if r["kind"] == "hidden"),
            "public_total": len(spec["public_cases"]), "hidden_total": len(spec["hidden_cases"]),
            "lines": len(src.splitlines()), "chars": len(src), "tokens": count_tokens(src),
        }
    grade["reference_py"] = {"lines": len(spec["python_reference"].splitlines()),
                             "tokens": count_tokens(spec["python_reference"])}
    out.write_text(json.dumps(grade, indent=1))
    for lang in ("ail", "py"):
        g = grade.get(lang, {})
        if g.get("present"):
            log(f"grade {lang}: public {g['public_pass']}/{g['public_total']}, hidden {g['hidden_pass']}/{g['hidden_total']}, "
                f"{g['lines']} lines, {g['tokens']} tokens")
    return grade


def count_tokens(text):
    try:
        base = client.messages.count_tokens(model=BUILDER, messages=[{"role": "user", "content": "x"}]).input_tokens
        full = client.messages.count_tokens(model=BUILDER, messages=[{"role": "user", "content": "x\n" + text}]).input_tokens
        return full - base
    except Exception as e:  # counting is free but optional
        log(f"count_tokens failed: {e}")
        return None


# ---------------------------------------------------------------- phase 5: judge and report

def numbers_table(spec, builds, grade):
    led = ledger()
    rows = [("", "AIL", "Python")]

    def g(lang, key):
        return grade.get(lang, {}).get(key, "-")

    def b(lang):
        return builds.get(lang) or {}

    def bm(lang, key):
        return b(lang).get("metrics", {}).get(key, "-")

    rows += [
        ("Hidden cases passed", f"{g('ail', 'hidden_pass')}/{g('ail', 'hidden_total')}",
         f"{g('py', 'hidden_pass')}/{g('py', 'hidden_total')}"),
        ("Public cases passed", f"{g('ail', 'public_pass')}/{g('ail', 'public_total')}",
         f"{g('py', 'public_pass')}/{g('py', 'public_total')}"),
        ("How the build ended", b("ail").get("stop", "-"), b("py").get("stop", "-")),
        ("Model turns", b("ail").get("turns", "-"), b("py").get("turns", "-")),
        ("Tool calls", bm("ail", "tool_calls"), bm("py", "tool_calls")),
        ("Compile or run attempts", bm("ail", "compile_runs"), bm("py", "runs")),
        ("Attempts that failed to compile / raised", bm("ail", "compile_failures"), bm("py", "runs_with_exception")),
        ("Program lines", g("ail", "lines"), g("py", "lines")),
        ("Program tokens (same tokenizer)", g("ail", "tokens"), g("py", "tokens")),
        ("Wall time (min)", b("ail").get("minutes", "-"), b("py").get("minutes", "-")),
        ("API cost (USD)", f"{led['phases'].get('ail', {}).get('usd', 0):.2f}", f"{led['phases'].get('py', {}).get('usd', 0):.2f}"),
        ("Builder output tokens (incl. thinking)", led["phases"].get("ail", {}).get("output", "-"),
         led["phases"].get("py", {}).get("output", "-")),
    ]
    md = "| " + " | ".join(rows[0]) + " |\n|---|---|---|\n"
    md += "".join(f"| {a} | {x} | {y} |\n" for a, x, y in rows[1:])
    return md


def phase_judge(spec, builds, grade):
    out = RUN_DIR / "REPORT.md"
    table = numbers_table(spec, builds, grade)
    ail_m = (builds.get("ail") or {}).get("metrics", {})
    analysis = ""
    if can_spend("judge"):
        def src(rel):
            p = RUN_DIR / rel
            return p.read_text() if p.exists() else "(no program)"
        failing = {lang: [r for r in grade.get(lang, {}).get("rows", []) if not r["pass"]] for lang in ("ail", "py")}
        prompt = f"""You are judging one experiment. The question behind it: can AIL, a new language designed for AI
agents, be more helpful for agentic coding than current languages, and what would help agents (and the small models
we train) write it better? The same builder model built the app below twice from the same spec: once in AIL, using
the AIL docs and compiler it found in a tool sandbox, and once in Python. You wrote the spec earlier.

# Spec
{spec['spec_markdown']}

# Numbers measured by the harness
{table}
Resources the AIL build read (category: count): {json.dumps(ail_m.get('reads_by_category', {}))}
Files the AIL build read (path: times): {json.dumps(ail_m.get('files_read', {}))}
Compiler rule IDs hit (rule: times): {json.dumps(ail_m.get('rule_ids', {}))}
First clean `ail check` on turn {ail_m.get('first_clean_check_turn')}; runtime traps: {ail_m.get('runtime_traps')};
`ail explain` calls: {ail_m.get('explain_calls')}; times the compiler rewrote the file itself: {ail_m.get('compiler_rewrote_file')}.
AIL compile errors in order (first line each):
{chr(10).join(ail_m.get('error_log', [])) or '(none)'}
Failing grade cases: {json.dumps(failing)[:6000]}

# AIL program
```
{src('work-ail/app.ail')}
```

# Python program
```
{src('work-py/app.py')}
```

# Builder's self-report, AIL build
{(builds.get('ail') or {}).get('report', '(none)')}

# Builder's self-report, Python build
{(builds.get('py') or {}).get('report', '(none)')}

Write the analysis in Markdown, under 1,300 words, with these headings:
## Verdict (three sentences: did the AIL app work, how it compares with Python, what this one run can and cannot show)
## What helped (evidence from the numbers, files read and the self-report)
## What did not help
## What would help more (ranked, each one concrete and owned by: AIL docs, AIL compiler/tools, or ail-train data)
## Evidence for AIL being better for agents (where the AIL program or process shows an advantage: errors caught
before running, local reasoning, readability, tokens; and where it does not. Be skeptical: one run, one app,
a builder that knows Python far better. Say what experiment would settle the question.)
## Code review (short: correctness risks and idiom in each program)
"""
        msg = call("judge", HELPER, system="You are a careful, skeptical evaluator of programming-language experiments.",
                   messages=[{"role": "user", "content": prompt}], max_tokens=24000)
        analysis = text_of(msg)
    led = ledger()
    cost = "\n".join(f"- {k}: ${v['usd']:.2f} ({v['calls']} calls)" for k, v in led["phases"].items())
    report = f"""# Agentic coding test: {spec['app_name']} in AIL and Python

Builder: the API builder model; spec, hidden tests and analysis: the helper model (names in config.local).
AIL at the commit in .ail-version. {len(spec['hidden_cases'])} hidden cases, graded byte for byte.

## Numbers

{table}
AIL build read (category: count): {json.dumps(ail_m.get('reads_by_category', {}))}

Compiler rule IDs hit: {json.dumps(ail_m.get('rule_ids', {}))}

## Spend

{cost}
- total: ${led['total']:.2f} of the ${CAP_TOTAL:.2f} cap

{analysis or '(no analysis: budget)'}

## Builder's self-report: AIL

{(builds.get('ail') or {}).get('report', '(none)')}

## Builder's self-report: Python

{(builds.get('py') or {}).get('report', '(none)')}
"""
    out.write_text(report)
    log(f"report: {out}")


def main():
    if not os.environ.get("ANTHROPIC_API_KEY"):
        sys.exit("no ANTHROPIC_API_KEY")
    spec = phase_spec()
    builds = {"ail": phase_build(spec, "ail")}
    builds["py"] = phase_build(spec, "py")
    grade = phase_grade(spec)
    phase_judge(spec, builds, grade)
    log(f"done, total ${ledger()['total']:.2f}")


if __name__ == "__main__":
    main()
