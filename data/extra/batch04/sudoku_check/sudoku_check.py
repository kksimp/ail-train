def ok(x): return sorted(x) == [1, 2, 3, 4]
def ck(g):
    for r in range(4):
        if not ok(g[r]): return f"row {r + 1} broken"
    for c in range(4):
        if not ok([g[r][c] for r in range(4)]): return f"column {c + 1} broken"
    for b in range(4):
        r0 = b // 2 * 2; c0 = b % 2 * 2
        if not ok([g[r0][c0], g[r0][c0 + 1], g[r0 + 1][c0], g[r0 + 1][c0 + 1]]): return f"box {b + 1} broken"
    return "valid"
G = [[[1, 2, 3, 4], [3, 4, 1, 2], [2, 1, 4, 3], [4, 3, 2, 1]], [[1, 2, 3, 4], [2, 1, 4, 3], [3, 4, 1, 2], [4, 3, 2, 1]], [[1, 2, 3, 4], [3, 4, 1, 2], [2, 3, 4, 1], [4, 1, 2, 3]], [[1, 2, 3, 3], [3, 4, 1, 2], [2, 1, 4, 3], [4, 3, 2, 1]]]
for i, g in enumerate(G): print(f"grid {i + 1}: {ck(g)}")
