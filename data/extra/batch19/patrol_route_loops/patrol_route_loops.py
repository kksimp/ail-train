def patrol(g, sr, sc, extra):
    dr = [-1, 0, 1, 0]; dc = [0, 1, 0, -1]
    r, c, d = sr, sc, 0
    states = set(); tiles = set()
    while True:
        tiles.add(r * 100 + c)
        s = (r * 100 + c) * 4 + d
        if s in states:
            return -1
        states.add(s)
        nr = r + dr[d]; nc = c + dc[d]
        if nr < 0 or nr >= len(g) or nc < 0 or nc >= len(g[0]):
            return len(tiles)
        if g[nr][nc] == '#' or nr * 100 + nc == extra:
            d = (d + 1) % 4
        else:
            r, c = nr, nc

rows = [".#.#.#..", "...#..#.", "......##", ".#......", "......#.", "...^..#.", ".#......", "..#.##.."]
g = [list(r) for r in rows]
for r in range(len(g)):
    for c in range(len(g[0])):
        if g[r][c] == '^': sr, sc = r, c
print(f"part 1: the watchman covers {patrol(g, sr, sc, -1)} tiles")
traps = [f"({r},{c})" for r in range(len(g)) for c in range(len(g[0])) if g[r][c] == '.' and patrol(g, sr, sc, r * 100 + c) < 0]
print(f"trap spots: {' '.join(traps)}")
print(f"part 2: {len(traps)} spots would trap him")
