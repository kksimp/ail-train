import heapq
import re
import sys

lines = [l.strip() for l in sys.stdin.read().splitlines() if l.strip()]
first = lines[0].split() if lines else []
if len(first) != 2:
    print("bad input")
    sys.exit(0)
src, dst = first
adj = {}
for l in lines[1:]:
    w = l.split()
    if len(w) != 3 or not re.fullmatch(r"[0-9]+", w[2]):
        continue
    cost = int(w[2])
    adj.setdefault(w[0], []).append((w[1], cost))
    adj.setdefault(w[1], []).append((w[0], cost))
if src not in adj or dst not in adj:
    print("unknown node")
    sys.exit(0)
dist = {src: 0}
parent = {}
heap = [(0, src)]
while heap:
    d, u = heapq.heappop(heap)
    if d > dist[u]:
        continue
    for v, c in adj[u]:
        nd = d + c
        if v not in dist or nd < dist[v]:
            dist[v] = nd
            parent[v] = u
            heapq.heappush(heap, (nd, v))
if dst not in dist:
    print("unreachable")
    sys.exit(0)
path = [dst]
while path[-1] != src:
    path.append(parent[path[-1]])
path.reverse()
print(f"distance: {dist[dst]}")
print("path: " + " -> ".join(path))
