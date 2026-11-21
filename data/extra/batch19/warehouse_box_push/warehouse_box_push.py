def push(g, at, d):
    dr = -1 if d == '^' else (1 if d == 'v' else 0)
    dc = -1 if d == '<' else (1 if d == '>' else 0)
    r = at[0] + dr; c = at[1] + dc
    while g[r][c] == 'O':
        r += dr; c += dc
    if g[r][c] == '#':
        return False
    nr = at[0] + dr; nc = at[1] + dc
    if r != nr or c != nc:
        g[r][c] = 'O'
    g[nr][nc] = '@'
    g[at[0]][at[1]] = '.'
    at[0] = nr; at[1] = nc
    return True

def score(g):
    s = 0
    for r in range(len(g)):
        for c in range(len(g[r])):
            if g[r][c] == 'O':
                s += 100 * r + c
    return s

plan = ["########", "#..O..O#", "#.O@...#", "#..O.#.#", "#O...O.#", "#......#", "########"]
moves = list(">>v<<<^^>vv>>>^<<v")
g = [list(row) for row in plan]
at = [2, 3]
print(f"start score {score(g)}, {len(moves)} moves")
blocked = 0
for rnd in range(1, 4):
    for m in moves:
        if not push(g, at, m):
            blocked += 1
    if rnd == 1:
        print(f"part 1, after one run: score {score(g)}, robot at row {at[0]} col {at[1]}")
print(f"part 2, after three runs: score {score(g)}")
print(f"{blocked} moves hit a wall")
for row in g:
    print("".join(row))
