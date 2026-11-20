m = ["##..#", "#...#", "..#..", ".###.", "....#"]
g = [[c == "#" for c in l] for l in m]
R, C = len(g), len(g[0])
D = [(-1, 0), (1, 0), (0, -1), (0, 1)]
def shore(r, c):
    return sum(1 for dr, dc in D if not (0 <= r + dr < R and 0 <= c + dc < C and g[r + dr][c + dc]))
seen, out = set(), []
for r in range(R):
    for c in range(C):
        if not g[r][c] or (r, c) in seen:
            continue
        st = [(r, c)]; seen.add((r, c)); size = sh = 0
        while st:
            cr, cc = st.pop()
            size += 1; sh += shore(cr, cc)
            for dr, dc in D:
                nr, nc = cr + dr, cc + dc
                if 0 <= nr < R and 0 <= nc < C and g[nr][nc] and (nr, nc) not in seen:
                    seen.add((nr, nc)); st.append((nr, nc))
        out.append((size, sh))
print(f"islands: {len(out)}")
for i, (a, b) in enumerate(out):
    print(f"island {i + 1}: {a} cells, shore {b}")
print(f"land cells: {sum(a for a, _ in out)}")
