import sys
import re


def isint(s):
    return re.fullmatch(r"-?[0-9]+", s) is not None


def execq(h, rows, q):
    t = q.split()
    if len(t) < 3 or len(t) > 4 or t[0] != "rank" or t[2] not in ("standard", "dense"):
        return "error: bad query"
    if len(t) == 4 and t[3] != "asc":
        return "error: bad query"
    if t[1] not in h:
        return "error: unknown column " + t[1]
    vi = h.index(t[1])
    items = [(int(r[vi]), r[0], n) for n, r in enumerate(rows) if isint(r[vi])]
    if not items:
        return "(none)"
    asc = len(t) == 4
    items.sort(key=lambda x: (x[0] if asc else -x[0], x[2]))
    out = []
    rank = 0
    prev = None
    for pos, (v, i, _) in enumerate(items):
        if v != prev:
            rank = pos + 1 if t[2] == "standard" else rank + 1
            prev = v
        out.append("%d %s %d" % (rank, i, v))
    return "\n".join(out)


def main():
    lines = sys.stdin.read().splitlines()
    if not lines:
        return
    h = lines[0].split(",")
    rows = []
    k = 1
    while k < len(lines) and lines[k] != "":
        rows.append(lines[k].split(","))
        k += 1
    for q in lines[k:]:
        q = q.strip()
        if q == "":
            continue
        print("> " + q)
        print(execq(h, rows, q))


main()
