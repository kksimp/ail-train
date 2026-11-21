V = ["Ash", "Bly", "Cor", "Dun", "Elm", "Fen"]
L = [(0, 1, 7), (0, 2, 9), (0, 5, 14), (1, 2, 10), (1, 3, 15), (2, 3, 11), (2, 5, 2), (3, 4, 6), (4, 5, 9)]
p = list(range(len(V)))
def root(x):
    while p[x] != x: x = p[x]
    return x
t = u = 0
for a, b, c in sorted(L, key=lambda l: (l[2], l[0], l[1])):
    ra, rb = root(a), root(b)
    if ra == rb: print(f"skip {V[a]}-{V[b]} ({c})"); continue
    p[ra] = rb; t += c; u += 1; print(f"lay  {V[a]}-{V[b]} ({c})")
print(f"{u} cables, total length {t}")
