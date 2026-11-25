import sys
import re


def isint(s):
    return re.fullmatch(r"-?[0-9]+", s) is not None


def shown(v):
    return v if v != "" else "<empty>"


def uniq(vals):
    seen = []
    for v in vals:
        if v not in seen:
            seen.append(v)
    return seen


def execq(h, rows, q):
    t = q.split()
    if len(t) < 2 or len(t) > 3 or t[0] != "distinct":
        return "error: bad query"
    if len(t) == 3 and (t[2] != "sorted" or t[1] == "*"):
        return "error: bad query"
    if t[1] == "*":
        return "\n".join("%s: %d" % (n, len(uniq([r[i] for r in rows]))) for i, n in enumerate(h))
    if t[1] not in h:
        return "error: unknown column " + t[1]
    i = h.index(t[1])
    vals = uniq([r[i] for r in rows])
    if len(t) == 3:
        if rows and all(isint(v) for v in vals):
            vals.sort(key=int)
        else:
            vals.sort()
    body = ", ".join(shown(v) for v in vals) if vals else "-"
    return "%s (%d): %s" % (t[1], len(vals), body)


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
