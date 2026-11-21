from math import gcd
def det(m):
    n = len(m)
    if n == 1:
        return m[0][0]
    total = 0
    for c in range(n):
        minor = [[m[r][k] for k in range(n) if k != c] for r in range(1, n)]
        total += (1 if c % 2 == 0 else -1) * m[0][c] * det(minor)
    return total
def frac(n, d):
    g = gcd(n, d)
    s = -1 if d < 0 else 1
    return f"{s * n // g}" if s * d // g == 1 else f"{s * n // g}/{s * d // g}"
def fl(xs):
    return "[" + ", ".join(map(str, xs)) + "]"
cases = [("bowl", [[2, 1], [1, 4]], [-3, 2]), ("pass", [[2, 3], [3, 2]], [1, 1]), ("hill", [[-4, 1], [1, -2]], [2, 0]), ("3-D bowl", [[4, 1, 0], [1, 3, 1], [0, 1, 2]], [-1, 0, 2]), ("trough", [[1, 2], [2, 4]], [0, 1])]
for name, h, g in cases:
    n = len(h)
    minors = [det([h[i][:k] for i in range(k)]) for k in range(1, n + 1)]
    verdict = "saddle point"
    if minors[n - 1] == 0:
        verdict = "test fails (singular)"
    elif all(m > 0 for m in minors):
        verdict = "minimum"
    elif all((minors[k] > 0) == (k % 2 == 1) for k in range(n)):
        verdict = "maximum"
    where = ""
    d = minors[n - 1]
    if d != 0:
        coords = []
        for c in range(n):
            m = [list(r) for r in h]
            for r in range(n):
                m[r][c] = -g[r]
            coords.append(frac(det(m), d))
        where = f" at ({', '.join(coords)})"
    print(f"{name:<9} minors {fl(minors)}: {verdict}{where}")
