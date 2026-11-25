import sys
import re


def isint(s):
    return re.fullmatch(r"-?[0-9]+", s) is not None


def execq(h, rows, q):
    t = q.split()
    if t[:1] != ["pivot"]:
        return "error: bad query"
    if len(t) == 4 and t[3] == "count":
        is_sum = False
    elif len(t) == 5 and t[3] == "sum":
        is_sum = True
    else:
        return "error: bad query"
    names = [t[1], t[2]] + ([t[4]] if is_sum else [])
    for n in names:
        if n not in h:
            return "error: unknown column " + n
    ri, ci = h.index(t[1]), h.index(t[2])
    vi = h.index(t[4]) if is_sum else 0
    cells = {}
    for r in rows:
        if is_sum:
            if not isint(r[vi]):
                continue
            add = int(r[vi])
        else:
            add = 1
        k = (r[ri], r[ci])
        cells[k] = cells.get(k, 0) + add
    if not cells:
        return "(empty)"
    rs = sorted({k[0] for k in cells})
    cs = sorted({k[1] for k in cells})
    out = [",".join([t[1]] + cs + ["total"])]
    coltot = [0] * len(cs)
    grand = 0
    for r in rs:
        vals = []
        rt = 0
        for j, c in enumerate(cs):
            if (r, c) in cells:
                vals.append(str(cells[(r, c)]))
                rt += cells[(r, c)]
                coltot[j] += cells[(r, c)]
            else:
                vals.append(".")
        grand += rt
        out.append(",".join([r] + vals + [str(rt)]))
    out.append(",".join(["total"] + [str(x) for x in coltot] + [str(grand)]))
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
