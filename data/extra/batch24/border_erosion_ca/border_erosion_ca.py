def count_near(g, r, c, kind):
    n = 0
    for dr in (-1, 0, 1):
        for dc in (-1, 0, 1):
            rr, cc = r + dr, c + dc
            if (dr != 0 or dc != 0) and 0 <= rr < len(g) and 0 <= cc < len(g[0]):
                if g[rr][cc] == kind: n += 1
            elif dr != 0 or dc != 0:
                if kind == '~': n += 1
    return n
def step(g):
    out = [row[:] for row in g]
    for r in range(len(g)):
        for c in range(len(g[0])):
            if g[r][c] == '#' and count_near(g, r, c, '~') >= 5: out[r][c] = '~'
            elif g[r][c] == '~' and count_near(g, r, c, '#') >= 6: out[r][c] = '#'
    return out
mp = ["~~~~~~~~~~~~", "~~###~~~#~~~", "~#####~###~~", "~##~####~##~", "~#~~###~~~#~", "~##~#####~~~", "~~#~~##~~#~~", "~~~~~~~~~~~~"]
g = [list(l) for l in mp]
for s in range(1, 5):
    g = step(g)
    land = sum(row.count('#') for row in g)
    print(f"pass {s}: {land} land cells")
for row in g: print("".join(row))
