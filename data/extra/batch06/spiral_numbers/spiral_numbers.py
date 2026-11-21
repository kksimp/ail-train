def fl(n):
    g = [[0] * n for _ in range(n)]; D = [(0, 1), (1, 0), (0, -1), (-1, 0)]; r = c = d = 0
    for k in range(1, n * n + 1):
        g[r][c] = k; nr, nc = r + D[d][0], c + D[d][1]
        if not (0 <= nr < n and 0 <= nc < n) or g[nr][nc]: d = (d + 1) % 4
        r += D[d][0]; c += D[d][1]
    return g
for n in [4, 5]:
    for row in fl(n): print("".join(f"{x:>3}" for x in row))
    print("")
