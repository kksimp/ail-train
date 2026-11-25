import sys

lines = sys.stdin.read().split("\n")
ini, queries = [], []
for i, l in enumerate(lines):
    if l.strip() == "---":
        ini, queries = lines[:i], lines[i + 1:]
        break
data = {}
sec = ""
for raw in ini:
    l = raw.strip()
    if l == "" or l[0] in ";#":
        continue
    if l.startswith("[") and l.endswith("]"):
        sec = l[1:-1].strip()
        continue
    if "=" not in l:
        continue
    k, v = l.split("=", 1)
    k = k.strip()
    if k == "":
        continue
    data[sec + "." + k] = v.strip()
if any(l.strip() == "---" for l in lines):
    for q in queries:
        q = q.strip()
        if q == "":
            continue
        if "." not in q:
            print("(bad query)")
        else:
            print(data.get(q, "(missing)"))
