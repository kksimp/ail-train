def parallel(caps):
    t = 0.0
    for c in caps:
        t = t + c
    return t
def series(caps):
    inv = 0.0
    for c in caps:
        inv = inv + 1.0 / c
    return 1.0 / inv
def energy(c, v):
    return c * v * v / 2.0
for n in [1, 2, 4, 6]:
    caps = [100.0 for k in range(n)]
    cs = series(caps)
    vs = 2.7 * float(n)
    es = energy(cs, vs)
    cp = parallel(caps)
    ep = energy(cp, 2.7)
    print(f"{n} cells: series {cs:>6.2f} F at {vs:>4.1f} V = {es:>6.1f} J, parallel {cp:>5.1f} F at 2.7 V = {ep:>6.1f} J")
mixed = series([parallel([100.0, 100.0]), parallel([100.0, 100.0]), parallel([100.0, 100.0])])
joules = energy(mixed, 8.1)
wh = joules / 3600.0
print(f"3 pairs in series: {mixed:.2f} F at 8.1 V holds {joules:.1f} J = {wh:.4f} Wh")
