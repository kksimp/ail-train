# Usage: python3 tools/split_bundle/split.py BUNDLE.txt batchNN
# Bundle format: "=== name", "--- ail", the AIL program, "--- py", the Python twin.
# Lints the AIL for known traps (keywords as names, `+` on strings, `else` inside an index, ...).
# Split a bundle into data/extra/BATCH/NAME/{NAME.ail,NAME.py,NAME.out}; run the twin for .out.
import sys, os, subprocess, re
bundle, batch = sys.argv[1], sys.argv[2]
extra = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "data", "extra")
extra = os.path.normpath(extra)
root = os.path.join(extra, batch)
text = open(bundle).read()
progs = re.split(r"^=== (\S+)\n", text, flags=re.M)[1:]
for name, body in zip(progs[0::2], progs[1::2]):
    m = re.match(r"--- ail\n(.*?)^--- py\n(.*)\Z", body, flags=re.S | re.M)
    if not m:
        print("BAD BUNDLE", name); continue
    ail, py = m.group(1).rstrip("\n") + "\n", m.group(2).rstrip("\n") + "\n"
    import glob
    other = [g for g in glob.glob(f"{extra}/*/{name}") if not g.startswith(root + "/")]
    bad = re.search(r"maze|calc|depgraph|invjson|ledger|outline|stock|tally|till|wrap", name)
    if other or bad:
        print("NAME CLASH", name, other, bool(bad)); continue
    d = os.path.join(root, name); os.makedirs(d, exist_ok=True)
    open(f"{d}/{name}.ail", "w").write(ail)
    open(f"{d}/{name}.py", "w").write(py)
    r = subprocess.run([sys.executable, "-I", f"{name}.py"], cwd=d, capture_output=True, text=True, timeout=20)
    if r.returncode != 0:
        print("PY FAIL", name, r.stderr[-500:]); continue
    open(f"{d}/{name}.out", "w").write(r.stdout)
    probs = []
    for i, l in enumerate(ail.split("\n"), 1):
        if "\t" in l: probs.append(f"tab line {i}")
        ind = len(l) - len(l.lstrip(" "))
        if ind % 4: probs.append(f"indent {ind} line {i}")
        if re.search(r"&&|\|\||\bnull\b|\belse if\b|\blet\b|\+= \"|\" \+ |\+ \"|\.(lower|upper)\(\)|\$\{|\.unwrap_or\(|\bpar\b|\bselect\b|\bany\b [a-z_]+ :=", l.split("#")[0]) : probs.append(f"habit line {i}: {l.strip()}")
        code = l.split("#")[0]
        if re.search(r"\w\[[^\]\(]*\belse\b", code): probs.append(f"else inside index line {i}")
        if ":+" in code: probs.append(f"sign format line {i}")
        if re.match(r"impl [A-Z]\w*(\[.*\])?\s*$", code): probs.append(f"impl without trait line {i}")
        if "from_code(" in code and " else " not in code: probs.append(f"from_code without else line {i}")
        if re.search(r"\b(move|case|unsafe|range|len|sum|all|type|bytes|str|int|float|char|bool|match|loop|in|fn|use|pub|ref|mut|spawn|defer|yield|where|impl|trait|enum|struct|self|super|as|is|not|and|or|then|elif|while|for|return|break|continue|true|false|none|some|par|select)\s*:=", code): probs.append(f"keyword as name line {i}")
        if re.search(r'\{[^}]*"[^}]*\}', code) and re.search(r'"[^"]*\{[^}"]*"', code) and re.search(r'\{[^{}]*"[^{}]*"[^{}]*\}', code): probs.append(f"maybe nested literal line {i}")
    fns = re.split(r"\n(?=(?:@test )?fn )", ail)
    for f in fns:
        if len(re.findall(r"\bfor _ in\b", f)) > 1: probs.append("_ bound twice in one fn")
    if not ail.startswith("## "): probs.append("no header")
    if "fn main()" not in ail: probs.append("no main")
    if "@test" not in ail: probs.append("no test")
    print(("WARN " + name + " " + "; ".join(probs)) if probs else f"ok {name} ({len(r.stdout.splitlines())} lines out)")
