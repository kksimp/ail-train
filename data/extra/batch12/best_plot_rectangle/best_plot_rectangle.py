grid = [[2, -1, -4, 3, 1], [-3, 4, 2, -1, -2], [1, 3, -2, 5, -6], [-4, -1, 6, 2, 1], [3, -5, 1, -2, 4]]
rows = len(grid)
cols = len(grid[0])
for r in grid:
    print("".join(f"{v:>3}" for v in r))
best = grid[0][0]
box = [0, 0, 0, 0]
for top in range(rows):
    sums = [0] * cols
    for bot in range(top, rows):
        for c in range(cols):
            sums[c] += grid[bot][c]
        run = 0
        frm = 0
        for c in range(cols):
            if run <= 0:
                run = sums[c]
                frm = c
            else:
                run += sums[c]
            if run > best:
                best = run
                box = [top, frm, bot, c]
print(f"best total {best}")
print(f"rows {box[0] + 1} to {box[2] + 1}, columns {box[1] + 1} to {box[3] + 1}")
area = (box[2] - box[0] + 1) * (box[3] - box[1] + 1)
print(f"{area} cells")
