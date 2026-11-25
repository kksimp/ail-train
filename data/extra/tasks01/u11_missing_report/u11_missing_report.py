import sys

MISSING = {"", "na", "n/a", "null", "none", "-"}


def miss(v):
    return v.strip().lower() in MISSING


def execq(h, rows, q):
    t = q.split()
    if not t or t[0] != "missing" or len(t) > 2:
        return "error: bad query"
    if len(t) == 1:
        out = []
        for i, c in enumerate(h):
            n = sum(1 for r in rows if miss(r[i]))
            p = n * 100 // len(rows) if rows else 0
            out.append("%s: %d/%d (%d%%)" % (c, n, len(rows), p))
        return "\n".join(out)
    if t[1] == "rows":
        out = []
        for r in rows:
            cols = [h[i] for i in range(len(h)) if miss(r[i])]
            if cols:
                out.append("%s: %s" % (r[0], ",".join(cols)))
        return "\n".join(out) if out else "(complete)"
    if t[1] not in h:
        return "error: unknown column " + t[1]
    i = h.index(t[1])
    ids = [r[0] for r in rows if miss(r[i])]
    return "%s: %s" % (t[1], ", ".join(ids) if ids else "-")


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
