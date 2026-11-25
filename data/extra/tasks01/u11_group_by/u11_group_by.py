import sys
import re


def isint(s):
    return re.fullmatch(r"-?[0-9]+", s) is not None


def execq(h, rows, q):
    t = q.split()
    if not t or t[0] not in ("count", "sum"):
        return "error: bad query"
    is_sum = t[0] == "sum"
    pos = 1
    vcol = None
    if is_sum:
        if len(t) < 3:
            return "error: bad query"
        vcol = t[1]
        pos = 2
    if pos >= len(t):
        return "error: bad query"
    gcol = t[pos]
    pos += 1
    byval = False
    if pos < len(t) and t[pos] == "byvalue":
        byval = True
        pos += 1
    if pos != len(t):
        return "error: bad query"
    if gcol not in h:
        return "error: unknown column " + gcol
    gi = h.index(gcol)
    if is_sum:
        if vcol not in h:
            return "error: unknown column " + vcol
        vi = h.index(vcol)
    m = {}
    skipped = 0
    for r in rows:
        if is_sum:
            if not isint(r[vi]):
                skipped += 1
                continue
            m[r[gi]] = m.get(r[gi], 0) + int(r[vi])
        else:
            m[r[gi]] = m.get(r[gi], 0) + 1
    keys = sorted(m, key=(lambda k: (-m[k], k)) if byval else (lambda k: k))
    out = ["%s %d" % (k, m[k]) for k in keys]
    if skipped > 0:
        out.append("(skipped %d)" % skipped)
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
        r = execq(h, rows, q)
        if r != "":
            print(r)


main()
