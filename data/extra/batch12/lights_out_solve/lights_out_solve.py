def press(g, r, c):
    for d in [[0, 0], [1, 0], [-1, 0], [0, 1], [0, -1]]:
        nr = r + d[0]; nc = c + d[1]
        if 0 <= nr < 5 and 0 <= nc < 5:
            g[nr][nc] = not g[nr][nc]

def attempt(start, top, presses):
    g = [list(row) for row in start]
    for c in range(5):
        if ((top >> c) & 1) == 1:
            press(g, 0, c)
            presses[0][c] = True
    for r in range(1, 5):
        for c in range(5):
            if g[r - 1][c]:
                press(g, r, c)
                presses[r][c] = True
    return not any(g[4])

def blank():
    return [[False] * 5 for _ in range(5)]

rows = ["#.#.#", ".##..", "#...#", "..##.", "#.#.#"]
start = [[ch == '#' for ch in s] for s in rows]
best = 26
plan = blank()
solvable = 0
for top in range(32):
    presses = blank()
    if attempt(start, top, presses):
        solvable += 1
        n = sum(sum(1 for x in row if x) for row in presses)
        if n < best:
            best = n
            plan = presses
print(f"{solvable} of 32 top rows clear the board")
for row in plan:
    print("".join("X" if x else "." for x in row))
print(f"fewest presses: {best}")
