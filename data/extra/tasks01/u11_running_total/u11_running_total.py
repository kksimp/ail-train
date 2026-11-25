import sys
import re


def isint(s):
    return re.fullmatch(r"-?[0-9]+", s) is not None


def execq(h, rows, q):
    t = q.split()
    if len(t) != 4 or t[0] not in ("running", "runmax") or t[2] != "by":
        return "error: bad query"
    for c in (t[1], t[3]):
        if c not in h:
            return "error: unknown column " + c
    vi, ki = h.index(t[1]), h.index(t[3])
    state = {}
    out = []
    skipped = 0
    for r in rows:
        if not isint(r[vi]):
            skipped += 1
            continue
        v = int(r[vi])
        k = r[ki]
        if k not in state:
            state[k] = v
        elif t[0] == "running":
            state[k] += v
        else:
            state[k] = max(state[k], v)
        out.append("%s %s: %d -> %d" % (r[0], k, v, state[k]))
    if skipped > 0:
        out.append("(skipped %d)" % skipped)
    if not out:
        out.append("(none)")
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
