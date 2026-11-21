g = [[False] * 5 for _ in range(5)]
for r, c in [(0, 0), (2, 2), (4, 4), (2, 3), (1, 2), (0, 0)]:
    for dr, dc in [(0, 0), (1, 0), (-1, 0), (0, 1), (0, -1)]:
        a, b = r + dr, c + dc
        if 0 <= a < 5 and 0 <= b < 5: g[a][b] = not g[a][b]
for r in g: print("".join("O" if x else "." for x in r))
print(f"{sum(x for r in g for x in r)} lamps lit")
