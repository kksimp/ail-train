def rot(g):
    n = len(g); return [[g[n - 1 - r][c] for r in range(n)] for c in range(n)]
g = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]; st = g
for t in range(1, 5):
    g = rot(g); print(f"after {t}:")
    for row in g: print("  " + " ".join(f"{x:>2}" for x in row))
print(f"back to start: {str(g == st).lower()}")
print(f"4x4 corner after one turn: {rot([[r * 4 + c for c in range(4)] for r in range(4)])[0][0]}")
