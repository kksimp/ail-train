pool = []

def build(xs, lo, hi):
    if hi - lo == 1:
        pool.append((-1, -1, xs[lo]))
        return len(pool) - 1
    mid = (lo + hi) // 2
    l = build(xs, lo, mid)
    r = build(xs, mid, hi)
    pool.append((l, r, 0))
    return len(pool) - 1

def setv(node, lo, hi, idx, v):
    if hi - lo == 1:
        pool.append((-1, -1, v))
        return len(pool) - 1
    mid = (lo + hi) // 2
    l, r, _ = pool[node]
    if idx < mid:
        l = setv(pool[node][0], lo, mid, idx, v)
    else:
        r = setv(pool[node][1], mid, hi, idx, v)
    pool.append((l, r, 0))
    return len(pool) - 1

def values(node, out):
    l, r, v = pool[node]
    if l < 0:
        out.append(v)
        return
    values(l, out)
    values(r, out)

v0 = build([10, 20, 30, 40, 50, 60, 70, 80], 0, 8)
print(f"v0 uses {len(pool)} nodes")
v1 = setv(v0, 0, 8, 2, 33)
v2 = setv(v1, 0, 8, 7, 88)
v3 = setv(v0, 0, 8, 0, 11)
for i, root in enumerate([v0, v1, v2, v3]):
    out = []
    values(root, out)
    print(f"v{i}: {out}")
print(f"pool has {len(pool)} nodes: 15 for v0 plus 4 per update")
