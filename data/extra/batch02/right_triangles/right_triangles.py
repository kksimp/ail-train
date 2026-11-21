from math import gcd
def tr(mc):
    out = []; m = 2
    while m * m + 1 <= mc:
        for n in range(1, m):
            if (m - n) % 2 == 1 and gcd(m, n) == 1:
                a, b, c = m * m - n * n, 2 * m * n, m * m + n * n
                if c <= mc: out.append((min(a, b), max(a, b), c))
        m += 1
    return sorted(out, key=lambda t: (t[2], t[0]))
ts = tr(100)
print(f"{len(ts)} primitive triples with c <= 100")
for t in ts[:8]: print(f"  {t[0]}^2 + {t[1]}^2 = {t[2]}^2")
bp = {}
for t in tr(1000):
    p = sum(t)
    for k in range(p, 1001, p): bp[k] = bp.get(k, 0) + 1
best = max(bp, key=lambda p: (bp[p], -p))
print(f"perimeter up to 1000 with most right triangles: {best} ({bp[best]})")
