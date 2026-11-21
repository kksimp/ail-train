def frozen_near(g, r, c):
    n = 0
    for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        rr, cc = r + dr, c + dc
        if 0 <= rr < len(g) and 0 <= cc < len(g):
            if g[rr][cc]: n += 1
    return n

def grow(g):
    return [[g[r][c] or frozen_near(g, r, c) == 1 for c in range(len(g))] for r in range(len(g))]

size = 9
g = [[r == 4 and c == 4 for c in range(size)] for r in range(size)]
for s in range(1, 5):
    g = grow(g)
    print(f"step {s}: {sum(sum(1 for x in row if x) for row in g)} frozen")
for row in g:
    print("".join('*' if x else '.' for x in row))
