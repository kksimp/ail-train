import sys


def execq(ha, ra, hb, rb, q):
    t = q.split()
    if len(t) != 2 or t[0] not in ("inner", "left"):
        return "error: bad query"
    key = t[1]
    if key not in ha:
        return "error: no column " + key
    if key not in hb:
        return "error: no column " + key
    ia = ha.index(key)
    ib = hb.index(key)
    keep = [i for i in range(len(hb)) if i != ib]
    out = [",".join(ha + [hb[i] for i in keep])]
    n = 0
    for a in ra:
        hit = False
        for b in rb:
            if a[ia] == b[ib]:
                hit = True
                out.append(",".join(a + [b[i] for i in keep]))
                n += 1
        if not hit and t[0] == "left":
            out.append(",".join(a + [""] * len(keep)))
            n += 1
    out.append("(%d rows)" % n)
    return "\n".join(out)


def main():
    lines = sys.stdin.read().splitlines()
    cuts = [i for i, l in enumerate(lines) if l == "--"]
    if len(cuts) < 2:
        return
    ta = lines[:cuts[0]]
    tb = lines[cuts[0] + 1:cuts[1]]
    qs = lines[cuts[1] + 1:]
    if not ta or not tb:
        return
    ha = ta[0].split(",")
    ra = [l.split(",") for l in ta[1:]]
    hb = tb[0].split(",")
    rb = [l.split(",") for l in tb[1:]]
    for q in qs:
        q = q.strip()
        if q == "":
            continue
        print("> " + q)
        print(execq(ha, ra, hb, rb, q))


main()
