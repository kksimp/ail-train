def cheats(cells, dist, k, least):
    n = 0
    for a in cells:
        for b in cells:
            jump = abs(a[0] - b[0]) + abs(a[1] - b[1])
            if jump <= k:
                if dist[b[0] * 100 + b[1]] - dist[a[0] * 100 + a[1]] - jump >= least:
                    n += 1
    return n

rows = ["#########", "#S..#...#", "###.#.#.#", "#...#.#.#", "#.###.#.#", "#...#.#.#", "###.#.#E#", "#...#.###", "#.....###", "#########"]
for r, row in enumerate(rows):
    c = row.find("S")
    if c >= 0: start = [r, c]
dist = {start[0] * 100 + start[1]: 0}
cells = [start]; i = 0
while i < len(cells):
    p = cells[i]; i += 1
    for d in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
        nr = p[0] + d[0]; nc = p[1] + d[1]
        ch = rows[nr][nc] if 0 <= nc < len(rows[nr]) else '#'
        if ch != '#' and nr * 100 + nc not in dist:
            dist[nr * 100 + nc] = dist[p[0] * 100 + p[1]] + 1
            cells.append([nr, nc])
print(f"the track is {len(cells)} tiles, {max(dist.values())} steps end to end")
print(f"part 1: {cheats(cells, dist, 2, 6)} two-move cheats save at least 6")
print(f"part 2: {cheats(cells, dist, 4, 6)} four-move cheats save at least 6")
