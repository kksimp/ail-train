def bp(g):
    R, C = len(g), len(g[0]); t = [[0] * C for _ in range(R)]
    for r in range(R):
        for c in range(C):
            t[r][c] = g[r][c] + max(t[r - 1][c] if r else 0, t[r][c - 1] if c else 0)
    mv = []; r, c = R - 1, C - 1
    while r > 0 or c > 0:
        if r == 0: mv.append("R"); c -= 1
        elif c == 0: mv.append("D"); r -= 1
        elif t[r - 1][c] >= t[r][c - 1]: mv.append("D"); r -= 1
        else: mv.append("R"); c -= 1
    return t[R - 1][C - 1], "".join(reversed(mv))
for g in [[[0, 3, 1, 1], [2, 0, 0, 4], [1, 5, 3, 1]], [[5]], [[1, 1, 1], [1, 9, 1], [1, 1, 1]]]:
    n, p = bp(g)
    print(f"{n} coins via {p if p else '-'}")
