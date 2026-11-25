import sys


import re


def isint(s):
    return re.fullmatch(r"-?[0-9]+", s) is not None


def is_num(rows, i):
    return bool(rows) and all(isint(r[i]) for r in rows)


def cmp(a, b, num):
    if num:
        a, b = int(a), int(b)
    return -1 if a < b else (1 if a > b else 0)


def execq(h, rows, q):
    t = q.split()
    if len(t) < 2 or t[0] != "select":
        return "error: bad query"
    pos = 2
    has_where = False
    if pos < len(t) and t[pos] == "where":
        if pos + 3 >= len(t):
            return "error: bad query"
        wcol, wop, wval = t[pos + 1], t[pos + 2], t[pos + 3]
        if wop not in ("=", "!=", "<", ">", "<=", ">="):
            return "error: bad query"
        has_where = True
        pos += 4
    has_order = False
    desc = False
    if pos < len(t) and t[pos] == "order":
        if pos + 1 >= len(t):
            return "error: bad query"
        ocol = t[pos + 1]
        has_order = True
        pos += 2
        if pos < len(t) and t[pos] == "desc":
            desc = True
            pos += 1
    if pos != len(t):
        return "error: bad query"
    names = h if t[1] == "*" else t[1].split(",")
    idxs = []
    for n in names:
        if n not in h:
            return "error: unknown column " + n
        idxs.append(h.index(n))
    if has_where:
        if wcol not in h:
            return "error: unknown column " + wcol
        wi = h.index(wcol)
        wnum = is_num(rows, wi)
        if wnum and not isint(wval):
            return "error: bad value " + wval
    if has_order:
        if ocol not in h:
            return "error: unknown column " + ocol
        oi = h.index(ocol)
        onum = is_num(rows, oi)
    sel = []
    for r in rows:
        if not has_where:
            sel.append(r)
            continue
        c = cmp(r[wi], wval, wnum)
        ok = {"=": c == 0, "!=": c != 0, "<": c < 0, ">": c > 0, "<=": c <= 0, ">=": c >= 0}[wop]
        if ok:
            sel.append(r)
    if has_order:
        out = []
        for r in sel:
            at = len(out)
            for j in range(len(out)):
                c = cmp(out[j][oi], r[oi], onum)
                d = -c if desc else c
                if d > 0:
                    at = j
                    break
            out.insert(at, r)
        sel = out
    res = [",".join(r[i] for i in idxs) for r in sel]
    res.append("(%d rows)" % len(sel))
    return "\n".join(res)


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
