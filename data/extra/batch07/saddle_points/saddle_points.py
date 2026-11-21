def sa(m):
    o = []
    for r in range(len(m)):
        for c in range(len(m[r])):
            if m[r][c] == max(m[r]) and m[r][c] == min(row[c] for row in m): o.append((r + 1, c + 1))
    return o
for g in [[[9, 8, 7], [5, 3, 2], [6, 6, 7]], [[1, 2, 3], [3, 1, 2], [2, 3, 1]], [[4, 5, 4], [3, 5, 5], [1, 5, 4]], [[2]]]:
    s = sa(g); print(f"{len(g)}x{len(g[0])} grid: {' '.join(f'({a}, {b})' for a, b in s) if s else 'none'}")
