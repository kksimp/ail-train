def fit(kb):
    size = 1
    while size < kb:
        size *= 2
    return size

def alloc(free, kb):
    want = fit(kb)
    size = want
    while size <= 256 and len(free.get(size, [])) == 0:
        size *= 2
    if size > 256:
        return -1
    off = free[size].pop(0)
    while size > want:
        size //= 2
        free.setdefault(size, []).append(off + size)
    return off

def release(free, off, size):
    while size < 256:
        buddy = off ^ size
        lst = free.get(size, [])
        if buddy not in lst:
            break
        lst.remove(buddy)
        free[size] = lst
        off = min(off, buddy)
        size *= 2
    free.setdefault(size, []).append(off)

def show(free):
    parts = []
    for size in sorted(free.keys()):
        if len(free[size]) > 0:
            parts.append(f"{size}K at {sorted(free[size])}")
    return ", ".join(parts)

free = {256: [0]}
reqs = [("A", 30), ("B", 60), ("C", 7), ("D", 60), ("E", 100)]
where = {}
for who, kb in reqs:
    off = alloc(free, kb)
    if off < 0:
        print(f"{who} wants {kb}K: no block free")
    else:
        where[who] = off
        print(f"{who} wants {kb}K: {fit(kb)}K block at {off}K")
print(f"free: {show(free)}")
for who in ["A", "C", "B"]:
    kb = [r for r in reqs if r[0] == who][0][1]
    release(free, where[who], fit(kb))
    print(f"free {who}: {show(free)}")
