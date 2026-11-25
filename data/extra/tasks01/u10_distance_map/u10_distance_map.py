import sys
from collections import deque
g = [l for l in sys.stdin.read().split("\n") if l != ""]
R = len(g); C = len(g[0]) if g else 0
dist = [[-1] * C for _ in range(R)]
q = deque()
for r in range(R):
    for c in range(C):
        if g[r][c] == "S":
            dist[r][c] = 0; q.append((r, c))
if not q:
    print("no sources"); sys.exit(0)
while q:
    r, c = q.popleft()
    for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
        nr, nc = r + dr, c + dc
        if 0 <= nr < R and 0 <= nc < C and g[nr][nc] != "#" and dist[nr][nc] < 0:
            dist[nr][nc] = dist[r][c] + 1; q.append((nr, nc))
reach = unreach = far = 0
for r in range(R):
    cells = []
    for c in range(C):
        if g[r][c] == "#":
            cells.append("#")
        elif dist[r][c] < 0:
            cells.append("-"); unreach += 1
        else:
            cells.append(str(dist[r][c]))
            if g[r][c] != "S":
                reach += 1
            far = max(far, dist[r][c])
    print(" ".join(cells))
print(f"reachable {reach} unreachable {unreach} farthest {far}")
