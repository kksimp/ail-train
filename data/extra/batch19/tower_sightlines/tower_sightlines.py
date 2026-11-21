def look(g, r, c, dr, dc):
    dist = 0; y = r + dr; x = c + dc
    while 0 <= y < len(g) and 0 <= x < len(g[0]):
        dist += 1
        if g[y][x] >= g[r][c]:
            return [dist, 0]
        y += dr; x += dc
    return [dist, 1]

rows = ["41528", "26341", "73912", "15664", "38257", "92413"]
g = [[int(ch) for ch in row] for row in rows]
dirs = [[-1, 0], [1, 0], [0, -1], [0, 1]]
seen = 0; best = 0; best_at = ""
for r in range(len(g)):
    for c in range(len(g[0])):
        visible = False; scenic = 1
        for d in dirs:
            v = look(g, r, c, d[0], d[1])
            scenic *= v[0]
            if v[1] == 1: visible = True
        if visible: seen += 1
        if scenic > best:
            best = scenic; best_at = f"row {r} col {c}"
print(f"{len(g)} by {len(g[0])} towers")
print(f"part 1: {seen} towers are visible from outside")
print(f"part 2: best view score {best} at {best_at}")
