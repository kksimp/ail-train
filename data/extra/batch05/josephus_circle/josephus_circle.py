def sv(n, k):
    p = 0
    for m in range(2, n + 1): p = (p + k) % m
    return p + 1
for n, k in [(7, 3), (10, 2), (12, 5)]:
    r = list(range(1, n + 1)); i = 0; o = []
    while len(r) > 1: i = (i + k - 1) % len(r); o.append(r.pop(i))
    print(f"n={n} k={k}: out {' '.join(map(str, o))}; survivor {r[0]} (formula {sv(n, k)})")
