def active_near(g, r, c):
    n = 0
    for dr in (-1, 0, 1):
        for dc in (-1, 0, 1):
            rr, cc = r + dr, c + dc
            if (dr != 0 or dc != 0) and 0 <= rr < 8 and 0 <= cc < 8 and g[rr][cc] == 1: n += 1
    return n
def next_phase(cur, near):
    if cur == 0: return 1 if near == 2 else 0
    if cur == 1: return 3
    if cur == 3: return 2
    return 0
gl = {0: '.', 1: 'O', 3: 'x', 2: '+'}
g = [[0]*8 for r in range(8)]
g[3][3] = 1; g[3][4] = 1
counts = []
for s in range(1, 8):
    g = [[next_phase(g[r][c], active_near(g, r, c)) for c in range(8)] for r in range(8)]
    act = sum(row.count(1) for row in g)
    counts.append(act)
print(f"active cells per step: {counts}")
for row in g: print("".join(gl[v] for v in row))
