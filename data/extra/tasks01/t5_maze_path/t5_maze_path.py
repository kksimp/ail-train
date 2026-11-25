import sys
from collections import deque

lines = [l for l in sys.stdin.read().splitlines() if l.strip()]
rows = len(lines)
start = goal = None
for r, l in enumerate(lines):
    for c, ch in enumerate(l):
        if ch == 'S':
            start = (r, c)
        elif ch == 'E':
            goal = (r, c)
if start is None or goal is None:
    print("invalid")
else:
    cols = len(lines[0])
    dist = {start: 0}
    q = deque([start])
    while q:
        r, c = q.popleft()
        for dr, dc in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and lines[nr][nc] != '#' and (nr, nc) not in dist:
                dist[(nr, nc)] = dist[(r, c)] + 1
                q.append((nr, nc))
    print(dist[goal] if goal in dist else "no path")
