grid = ["AABBB", "AABCC", "DDBCC", "DAAAC", "DDDAA"]
R, C = len(grid), len(grid[0]); seen = [[False] * C for _ in range(R)]; out = []
for r in range(R):
    for c in range(C):
        if seen[r][c]: continue
        L = grid[r][c]; st = [(r, c)]; seen[r][c] = True; sz = 0
        while st:
            cr, cc = st.pop(); sz += 1
            for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                nr, nc = cr + dr, cc + dc
                if 0 <= nr < R and 0 <= nc < C and not seen[nr][nc] and grid[nr][nc] == L: seen[nr][nc] = True; st.append((nr, nc))
        out.append((L, sz))
for L, s in out: print(f"{L}: {s} cells")
print(f"{len(out)} regions")
