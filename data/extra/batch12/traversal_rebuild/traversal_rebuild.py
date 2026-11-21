def rebuild(pre, ino, at, lo, hi, ns):
    if lo > hi:
        return -1
    label = pre[at[0]]
    at[0] += 1
    mid = ino.index(label)
    l = rebuild(pre, ino, at, lo, mid - 1, ns)
    r = rebuild(pre, ino, at, mid + 1, hi, ns)
    ns.append([label, l, r])
    return len(ns) - 1

def post(ns, i, out):
    if i >= 0:
        post(ns, ns[i][1], out)
        post(ns, ns[i][2], out)
        out.append(ns[i][0])

def levels(ns, root):
    rows = []
    cur = [root]
    while cur:
        nxt = []
        labels = []
        for i in cur:
            labels.append(ns[i][0])
            if ns[i][1] >= 0:
                nxt.append(ns[i][1])
            if ns[i][2] >= 0:
                nxt.append(ns[i][2])
        rows.append("".join(labels))
        cur = nxt
    return rows

for pre_s, in_s in [("FBADCEGIH", "ABCDEFGHI"), ("ABDECF", "DBEAFC"), ("ABCD", "DCBA")]:
    ns = []
    at = [0]
    root = rebuild(list(pre_s), list(in_s), at, 0, len(pre_s) - 1, ns)
    out = []
    post(ns, root, out)
    po = "".join(out)
    rows = " / ".join(levels(ns, root))
    print(f"pre {pre_s} in {in_s}: post {po}, levels {rows}")
