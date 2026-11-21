def lr(xs):
    n = len(xs)
    if n == 0: return []
    bl = [1] * n; bk = [-1] * n
    for i in range(1, n):
        for j in range(i):
            if xs[j] < xs[i] and bl[j] + 1 > bl[i]: bl[i] = bl[j] + 1; bk[i] = j
    e = 0
    for i in range(1, n):
        if bl[i] > bl[e]: e = i
    out = []; k = e
    while k >= 0: out.append(xs[k]); k = bk[k]
    return out[::-1]
for xs in [[10, 9, 2, 5, 3, 7, 101, 18], [0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15], [5, 4, 3], [1, 2, 3, 4]]:
    r = lr(xs); print(f"{len(r)}: {r}")
