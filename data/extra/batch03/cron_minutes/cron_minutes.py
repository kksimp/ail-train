def ep(p):
    step = 1; body = p
    try:
        if "/" in p: s = p.find("/"); step = int(p[s + 1:]); body = p[:s]
        lo, hi = 0, 59
        if body != "*":
            if "-" in body: d = body.find("-"); lo = int(body[:d]); hi = int(body[d + 1:])
            else: lo = int(body); hi = 59 if step > 1 else lo
    except ValueError: return None
    if lo < 0 or hi > 59 or lo > hi or step < 1: return None
    return list(range(lo, hi + 1, step))
def ex(f):
    s = set()
    for p in f.split(","):
        g = ep(p)
        if g is None: return None
        s |= set(g)
    return sorted(s)
for f in ["*/15", "5,20,35", "10-14", "0-30/10", "45,0-5/2", "61", "*/0", "a-b"]:
    m = ex(f)
    print(f"{f:<9} {len(m):>2}: {m[:8]}" if m is not None else f"{f:<9} invalid")
