grid = ["S...#....", ".##.#.##.", "...#...#.", ".#...#.#.", ".#.#.#...", "...#...#G"]
rows = len(grid); cols = len(grid[0]); cells = [list(l) for l in grid]
for r in range(rows):
    for c in range(cols):
        if cells[r][c] == "S": start = r * cols + c
        if cells[r][c] == "G": goal = r * cols + c
gr, gc = divmod(goal, cols)
cost = [-1] * (rows * cols); parent = [-1] * (rows * cols); closed = [False] * (rows * cols)
cost[start] = 0; opn = [start]; exp = 0
def h(a): return abs(a // cols - gr) + abs(a % cols - gc)
while opn:
    pick = 0
    for i in range(len(opn)):
        a = opn[i]; b = opn[pick]
        if cost[a] + h(a) < cost[b] + h(b) or (cost[a] + h(a) == cost[b] + h(b) and h(a) < h(b)): pick = i
    cur = opn.pop(pick)
    if closed[cur]: continue
    closed[cur] = True; exp += 1
    if cur == goal: break
    r, c = divmod(cur, cols)
    for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        nr = r + dr; nc = c + dc
        if 0 <= nr < rows and 0 <= nc < cols and cells[nr][nc] != "#":
            n = nr * cols + nc
            if not closed[n] and (cost[n] == -1 or cost[cur] + 1 < cost[n]): cost[n] = cost[cur] + 1; parent[n] = cur; opn.append(n)
k = parent[goal]
while k != start and k >= 0: cells[k // cols][k % cols] = "*"; k = parent[k]
for row in cells: print("".join(row))
print(f"route {cost[goal]} steps, {exp} cells expanded")
