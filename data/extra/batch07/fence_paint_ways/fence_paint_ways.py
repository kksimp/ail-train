def wa(n, k):
    if n == 0: return 0
    if n == 1: return k
    s = k; d = k * (k - 1)
    for _ in range(3, n + 1): s, d = d, (s + d) * (k - 1)
    return s + d
for k in [2, 3, 4]: print(f"{k} colours, 1-8 posts: {' '.join(str(wa(n, k)) for n in range(1, 9))}")
