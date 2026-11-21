def step(g):
    ready = []
    for r in range(len(g)):
        for c in range(len(g[0])):
            g[r][c] += 1
            if g[r][c] == 10: ready.append([r, c])
    flashes = 0
    while ready:
        p = ready.pop(); flashes += 1
        for dr in (-1, 0, 1):
            for dc in (-1, 0, 1):
                nr = p[0] + dr; nc = p[1] + dc
                if (dr != 0 or dc != 0) and 0 <= nr < len(g) and 0 <= nc < len(g[0]):
                    g[nr][nc] += 1
                    if g[nr][nc] == 10: ready.append([nr, nc])
    for r in range(len(g)):
        for c in range(len(g[0])):
            if g[r][c] > 9: g[r][c] = 0
    return flashes

rows = ["38152", "61746", "27439", "54617", "19286"]
g = [[int(ch) for ch in r] for r in rows]
total = 0
for _ in range(50):
    total += step(g)
print(f"part 1: {total} flashes in 50 steps")
h = [[int(ch) for ch in r] for r in rows]
n = 1
while step(h) != 25 and n < 2000:
    n += 1
print(f"part 2: every jelly flashes together on step {n}")
for row in h:
    print("".join(str(v) for v in row))
