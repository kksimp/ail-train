import math

elev = [[50, 48, 46, 45, 47, 52], [47, 44, 40, 38, 41, 49], [45, 40, 35, 30, 36, 44], [44, 38, 31, 25, 29, 40], [46, 41, 34, 22, 30, 42]]
rows = len(elev)
cols = len(elev[0])
moves = [(0, 1, "→"), (1, 1, "↘"), (1, 0, "↓"), (1, -1, "↙"), (0, -1, "←"), (-1, -1, "↖"), (-1, 0, "↑"), (-1, 1, "↗")]
diag = math.sqrt(2.0)
target = []
for r in range(rows):
    line = []
    for c in range(cols):
        best = -1
        best_slope = 0.0
        arrow = "o"
        for dr, dc, sym in moves:
            nr = r + dr
            nc = c + dc
            if 0 <= nr < rows and 0 <= nc < cols:
                drop = float(elev[r][c] - elev[nr][nc])
                slope = drop / diag if dr != 0 and dc != 0 else drop
                if slope > best_slope:
                    best_slope = slope
                    best = nr * cols + nc
                    arrow = sym
        target.append(best)
        line.append(arrow)
    print(" ".join(line))
order = sorted(range(rows * cols), key=lambda i: -elev[i // cols][i % cols])
acc = [1] * (rows * cols)
for i in order:
    if target[i] >= 0:
        acc[target[i]] += acc[i]
for r in range(rows):
    print("".join(f"{a:>3}" for a in acc[r * cols:r * cols + cols]))
outlet = order[-1]
print(f"outlet at row {outlet // cols}, column {outlet % cols} drains {acc[outlet]} cells")
