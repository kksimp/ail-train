import sys


def norm_text(s):
    s = "".join(c.lower() if c.isascii() and c.isalpha() else c for c in s)
    s = "".join(c for c in s if (c.isascii() and c.isalnum()) or c == " ")
    return " ".join(w for w in s.split(" ") if w)


def norm_digits(s):
    return "".join(c for c in s if c in "0123456789")


def execq(h, rows, q):
    t = q.split()
    if len(t) != 2 or t[0] != "dups":
        return "error: bad query"
    items = []
    for it in t[1].split(","):
        if it == "":
            return "error: bad query"
        if ":" in it:
            col, _, suf = it.partition(":")
            if suf != "digits" or col == "":
                return "error: bad query"
            items.append((col, True))
        else:
            items.append((it, False))
    idxs = []
    for col, dg in items:
        if col not in h:
            return "error: unknown column " + col
        idxs.append((h.index(col), dg))
    groups = {}
    for r in rows:
        parts = [norm_digits(r[i]) if dg else norm_text(r[i]) for i, dg in idxs]
        if any(p == "" for p in parts):
            continue
        groups.setdefault("|".join(parts), []).append(r[0])
    shared = [ids for ids in groups.values() if len(ids) >= 2]
    if not shared:
        return "(no duplicates)"
    out = ["group %d: %s" % (n + 1, ", ".join(ids)) for n, ids in enumerate(shared)]
    out.append("(%d groups, %d records)" % (len(shared), sum(len(i) for i in shared)))
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
