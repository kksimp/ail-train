from math import gcd
for d in [[4, 4], [6, 2], [3, 3, 3], [10, 1, 1], [2, 2, 2, 2]]:
    t = sum(d); p = t * (t - 1) // 2; s = sum(n * (n - 1) // 2 for n in d); g = gcd(s, p); print(f"{'/'.join(map(str, d))}: {s // g}/{p // g} ({s * 100 / p:.1f}%)")
