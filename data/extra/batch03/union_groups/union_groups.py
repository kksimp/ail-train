ppl = ["Ada", "Bo", "Cy", "Di", "Ed", "Fi", "Gus", "Hal"]
par = list(range(8)); sz = [1] * 8
def fr(x):
    r = x
    while par[r] != r: r = par[r]
    while par[x] != r: par[x], x = r, par[x]
    return r
def jn(a, b):
    ra, rb = fr(a), fr(b)
    if ra == rb: return
    if sz[ra] < sz[rb]: par[ra] = rb; sz[rb] += sz[ra]
    else: par[rb] = ra; sz[ra] += sz[rb]
for a, b in [(0, 1), (2, 3), (1, 3), (4, 5), (6, 6)]: jn(a, b)
g = {}
for i in range(8): g.setdefault(fr(i), []).append(ppl[i])
for v in g.values(): print(", ".join(v))
print(f"{len(g)} groups")
