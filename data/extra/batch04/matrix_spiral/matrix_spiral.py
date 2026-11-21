def sp(g):
    o = []; t = 0; b = len(g) - 1; l = 0; r = len(g[0]) - 1
    while t <= b and l <= r:
        o += [g[t][c] for c in range(l, r + 1)]; t += 1
        o += [g[x][r] for x in range(t, b + 1)]; r -= 1
        if t <= b: o += [g[b][c] for c in range(r, l - 1, -1)]; b -= 1
        if l <= r: o += [g[x][l] for x in range(b, t - 1, -1)]; l += 1
    return o
for g in [[[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]], [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15]]]: print(" ".join(map(str, sp(g))))
