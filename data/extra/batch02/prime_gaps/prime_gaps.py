n = 10000
p = [True] * n; p[0] = p[1] = False
for i in range(2, 100):
    if p[i]:
        for m in range(i * i, n, i): p[m] = False
ps = [k for k in range(n) if p[k]]
gaps = [ps[i] - ps[i - 1] for i in range(1, len(ps))]
fs = {}
for i, g in enumerate(gaps):
    if g not in fs: fs[g] = ps[i]
for g in sorted(fs)[:8]: print(f"gap {g:>2} first after {fs[g]}")
print(f"{len(ps)} primes, widest gap {max(gaps)}, twin pairs {gaps.count(2)}")
