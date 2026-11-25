import re
import sys

lines = sys.stdin.read().split("\n")
if lines and lines[-1] == "":
    lines.pop()

first = lines[0] if lines else ""
if not re.fullmatch(r"-?[0-9]+", first) or int(first) < 1:
    print("bad width")
    sys.exit(0)
width = int(first)


def wrap(words, width):
    out = []
    cur = []
    cur_len = 0
    for w in words:
        if not cur:
            cur = [w]
            cur_len = len(w)
        elif cur_len + 1 + len(w) > width:
            out.append(" ".join(cur))
            cur = [w]
            cur_len = len(w)
        else:
            cur.append(w)
            cur_len += 1 + len(w)
    if cur:
        out.append(" ".join(cur))
    return out


paras = []
cur = []
for line in lines[1:]:
    ws = line.split()
    if not ws:
        if cur:
            paras.append(cur)
            cur = []
    else:
        cur.extend(ws)
if cur:
    paras.append(cur)

for i, p in enumerate(paras):
    if i > 0:
        print("")
    for l in wrap(p, width):
        print(l)
