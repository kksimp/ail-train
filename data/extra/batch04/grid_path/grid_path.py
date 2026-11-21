from collections import deque
rows = ["S..#......", ".#.#.####.", ".#...#....", ".####.#.#.", "......#.#E"]
g = [list(r) for r in rows]; H, W = len(g), len(g[0])
def find(t):
    for r in range(H):
        for c in range(W):
            if g[r][c] == t: return (r, c)
s, e = find("S"), find("E"); prev = {s: s}; q = deque([s])
while q:
    cur = q.popleft()
    if cur == e: break
    r, c = cur
    for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
        nr, nc = r + dr, c + dc
        if 0 <= nr < H and 0 <= nc < W and g[nr][nc] != "#" and (nr, nc) not in prev: prev[(nr, nc)] = cur; q.append((nr, nc))
st = 0; at = prev[e]
while at != s: g[at[0]][at[1]] = "*"; at = prev[at]; st += 1
for row in g: print("".join(row))
print(f"path length {st + 1}")
