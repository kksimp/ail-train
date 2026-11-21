def st(n):
    c = 0
    while n != 1: n = n // 2 if n % 2 == 0 else 3 * n + 1; c += 1
    return c
for n in [1, 6, 7, 27, 97]: print(f"{n}: {st(n)} steps")
L = 100000; cache = [-1] * L; cache[1] = 0; b = 1; bl = 0
for n in range(1, L):
    v = n; c = 0; path = []
    while v != 1:
        if v < L and cache[v] >= 0: break
        path.append(v); v = v // 2 if v % 2 == 0 else 3 * v + 1; c += 1
    t = c + (0 if v == 1 else cache[v])
    for i, p in enumerate(path):
        if p < L: cache[p] = t - i
    if t > bl: b = n; bl = t
print(f"longest below {L}: {b} with {bl} steps")
