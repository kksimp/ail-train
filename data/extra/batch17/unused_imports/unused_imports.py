def tokens(line):
    out = []
    cur = []
    for c in line:
        if c.isalnum() or c == '_':
            cur.append(c)
        else:
            if len(cur) > 0:
                out.append("".join(cur))
                cur = []
    if len(cur) > 0:
        out.append("".join(cur))
    return out

src = ["import os", "import sys", "import numpy as np", "from json import loads, dumps", "from pathlib import Path", "from typing import List, Dict", "", "def load(p: Path) -> List[str]:", "    data = loads(open(p).read())", "    return [os.path.join(x) for x in data]", "", "print(np.zeros(3))"]
bound = []
line_of = {}
used = set()
for i, line in enumerate(src):
    if line.startswith("from "):
        for n in line[5:].split(" import ")[1].split(","):
            bound.append(n.strip())
            line_of[n.strip()] = i + 1
    elif line.startswith("import "):
        rest2 = line[7:]
        name = rest2.split(" as ")[1] if " as " in rest2 else rest2.split(".")[0]
        bound.append(name)
        line_of[name] = i + 1
    else:
        for t in tokens(line):
            used.add(t)
unused = 0
for b in bound:
    if b not in used:
        unused += 1
        print(f"line {line_of[b]}: '{b}' imported but unused")
print(f"{len(bound)} names imported, {unused} unused")
