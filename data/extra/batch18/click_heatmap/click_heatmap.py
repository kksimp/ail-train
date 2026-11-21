g = [[0] * 8 for _ in range(4)]
seed = 2026
for i in range(60):
    seed = (seed * 1103515245 + 12345) % 2147483648
    x = (seed // 65536) % 800; y = (seed // 7) % 400
    if i % 3 == 0: x = 650 + seed % 50; y = 300 + seed % 40
    g[y // 100][x // 100] += 1
def shade(n): return "." if n == 0 else ("-" if n == 1 else ("+" if n < 4 else "#"))
for r in range(4): print(f"{''.join(shade(n) for n in g[r])}  {sum(g[r])}")
best = 0; at = (0, 0)
for r in range(4):
    for c in range(8):
        if g[r][c] > best: best = g[r][c]; at = (r, c)
print(f"hottest cell row {at[0]} col {at[1]} with {best} clicks")
