def label(halves):
    return f"{halves // 2}" if halves % 2 == 0 else f"{halves // 2}.5"

finds = [[2, 2], [3, 2], [2, 2], [4, 3], [3, 3], [2, 4], [5, 2], [2, 2], [6, 4], [3, 5], [4, 4], [10, 2], [2, 10], [3, 2], [7, 7], [4, 3], [2, 3], [8, 5]]
grid = [[0] * 9 for _ in range(9)]
for f in finds:
    grid[f[0] - 2][f[1] - 2] += 1
filled = 0
best = [0, 0]
header = [label(t + 2).rjust(4) for t in range(9)]
print(f"D\\T {''.join(header)}")
for d in range(9):
    cells = []
    for t in range(9):
        n = grid[d][t]
        if n > 0:
            filled += 1
        if n > grid[best[0]][best[1]]:
            best = [d, t]
        cells.append("   ." if n == 0 else f"{n:>4}")
    print(f"{label(d + 2):<3} {''.join(cells)}")
print(f"{filled} of 81 combinations found; most common D{label(best[0] + 2)}/T{label(best[1] + 2)}")
