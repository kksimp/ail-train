import re
import sys

edges = []
parent = {}
for line in sys.stdin.read().splitlines():
    w = line.split()
    if len(w) != 3 or not re.fullmatch(r"-?[0-9]+", w[2]):
        continue
    edges.append((int(w[2]), w[0], w[1]))
    parent[w[0]] = w[0]
    parent[w[1]] = w[1]


def find(x):
    while parent[x] != x:
        parent[x] = parent[parent[x]]
        x = parent[x]
    return x


total = 0
chosen = 0
for wt, a, b in sorted(edges):
    ra, rb = find(a), find(b)
    if ra != rb:
        parent[ra] = rb
        total += wt
        chosen += 1
comps = sum(1 for n in list(parent) if find(n) == n)
print(f"total: {total}")
print(f"edges: {chosen}")
print(f"components: {comps}")
