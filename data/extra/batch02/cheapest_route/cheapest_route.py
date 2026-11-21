def ch(g):
    C = len(g[0]); row = [0] * C
    for r in range(len(g)):
        for c in range(C):
            if r == 0 and c == 0: row[c] = g[0][0]
            elif r == 0: row[c] = row[c - 1] + g[r][c]
            elif c == 0: row[c] += g[r][c]
            else: row[c] = min(row[c], row[c - 1]) + g[r][c]
    return row[-1]
def gr(g):
    r = c = 0; t = g[0][0]
    while r < len(g) - 1 or c < len(g[0]) - 1:
        d = g[r + 1][c] if r + 1 < len(g) else 10**6
        rt = g[r][c + 1] if c + 1 < len(g[0]) else 10**6
        if d <= rt: r += 1
        else: c += 1
        t += g[r][c]
    return t
for g in [[[1, 3, 1], [1, 5, 1], [4, 2, 1]], [[1, 2, 3], [4, 5, 6]], [[1, 1, 9, 9], [9, 1, 9, 9], [9, 1, 1, 1], [9, 9, 9, 1]], [[2, 1, 50], [3, 40, 1], [1, 1, 1]]]:
    print(f"best {ch(g)}, greedy {gr(g)}")
