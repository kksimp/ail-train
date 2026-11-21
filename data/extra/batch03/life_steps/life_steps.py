g = [[False] * 7 for _ in range(6)]
for r, c in [(0, 1), (1, 2), (2, 0), (2, 1), (2, 2)]: g[r][c] = True
def nb(g, r, c):
    return sum(1 for dr in (-1, 0, 1) for dc in (-1, 0, 1) if (dr or dc) and 0 <= r + dr < len(g) and 0 <= c + dc < len(g[0]) and g[r + dr][c + dc])
def adv(g):
    return [[nb(g, r, c) == 3 or (g[r][c] and nb(g, r, c) == 2) for c in range(len(g[0]))] for r in range(len(g))]
live = lambda g: [(r, c) for r in range(len(g)) for c in range(len(g[0])) if g[r][c]]
st = live(g)
for gen in range(1, 5):
    g = adv(g); print(f"generation {gen}:")
    for row in g: print("".join("#" if x else "." for x in row))
print(f"moved diagonally: {str(live(g) == [(r + 1, c + 1) for r, c in st]).lower()}")
