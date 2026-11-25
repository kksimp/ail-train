import sys
from collections import deque

lines = [l.strip() for l in sys.stdin.read().splitlines() if l.strip()]
if lines:
    start = lines[0]
    adj = {}
    nodes = {start}
    skipped = 0
    for l in lines[1:]:
        w = l.split()
        if len(w) != 2:
            skipped += 1
            continue
        nodes.update(w)
        adj.setdefault(w[0], []).append(w[1])
        adj.setdefault(w[1], []).append(w[0])
    dist = {start: 0}
    q = deque([start])
    while q:
        cur = q.popleft()
        for nb in adj.get(cur, []):
            if nb not in dist:
                dist[nb] = dist[cur] + 1
                q.append(nb)
    for n in sorted(nodes):
        print(n, dist.get(n, -1))
    if skipped:
        print("skipped", skipped)
