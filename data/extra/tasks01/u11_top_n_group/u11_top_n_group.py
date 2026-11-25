import sys
import re


def isint(s):
    return re.fullmatch(r"-?[0-9]+", s) is not None


def execq(h, rows, q):
    t = q.split()
    if len(t) != 5 or t[0] != "top" or t[3] != "by":
        return "error: bad query"
    if not isint(t[1]) or int(t[1]) <= 0:
        return "error: bad query"
    n = int(t[1])
    for c in (t[2], t[4]):
        if c not in h:
            return "error: unknown column " + c
    vi, gi = h.index(t[2]), h.index(t[4])
    groups = {}
    for idx, r in enumerate(rows):
        if not isint(r[vi]):
            continue
        groups.setdefault(r[gi], []).append((int(r[vi]), idx))
    if not groups:
        return "(none)"
    out = []
    for g in sorted(groups):
        best = sorted(groups[g], key=lambda p: (-p[0], p[1]))[:n]
        out.append("%s: %s" % (g, ", ".join("%s=%d" % (rows[i][0], v) for v, i in best)))
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
