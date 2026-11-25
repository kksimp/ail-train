import sys
g = [l for l in sys.stdin.read().split("\n") if l != ""]
R = len(g); C = len(g[0]) if g else 0
seen = [[False] * C for _ in range(R)]
n = 0
for r in range(R):
    for c in range(C):
        if seen[r][c]:
            continue
        ch = g[r][c]
        st = [(r, c)]; seen[r][c] = True
        area = per = 0
        while st:
            y, x = st.pop(); area += 1
            for dy, dx in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                ny, nx = y + dy, x + dx
                if 0 <= ny < R and 0 <= nx < C and g[ny][nx] == ch:
                    if not seen[ny][nx]:
                        seen[ny][nx] = True; st.append((ny, nx))
                else:
                    per += 1
        print(f"{ch} {area} {per}"); n += 1
print(f"regions {n}")
