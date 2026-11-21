def group_of(module, stdlib):
    top = module.split(".")[0]
    if module.startswith(".") or top == "shopapp":
        return 2
    if top in stdlib:
        return 0
    return 1

stdlib = ["os", "sys", "json", "re", "datetime", "collections"]
lines = ["import sys", "from shopapp.models import Order", "import requests", "from collections import defaultdict", "import os", "from .utils import slugify", "from collections import Counter", "import numpy", "import sys", "from shopapp.models import Customer, Basket", "import json"]
plain = set()
froms = {}
for line in lines:
    if line.startswith("from "):
        parts = line[5:].split(" import ")
        names = froms.get(parts[0], set())
        for n in parts[1].split(","):
            names.add(n.strip())
        froms[parts[0]] = names
    elif line.startswith("import "):
        plain.add(line[7:])
titles = ["standard library", "third party", "local"]
written = 0
for g in range(3):
    out = []
    for m in sorted(plain):
        if group_of(m, stdlib) == g:
            out.append(f"import {m}")
    for m in sorted(froms.keys()):
        if group_of(m, stdlib) == g:
            names = ", ".join(sorted(froms[m]))
            out.append(f"from {m} import {names}")
    if len(out) > 0:
        print(f"# {titles[g]}")
        for o in out:
            print(o)
        written += len(out)
print(f"# {len(lines)} lines in, {written} out")
