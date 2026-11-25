import sys

adj = {}
nodes = set()
for line in sys.stdin.read().splitlines():
    w = line.split()
    if len(w) != 2:
        continue
    nodes.update(w)
    adj.setdefault(w[0], []).append(w[1])

color = {}
path = []


def visit(u):
    color[u] = 1
    path.append(u)
    for v in sorted(adj.get(u, [])):
        state = color.get(v, 0)
        if state == 1:
            return path[path.index(v):] + [v]
        if state == 0:
            found = visit(v)
            if found:
                return found
    path.pop()
    color[u] = 2
    return []


for n in sorted(nodes):
    if color.get(n, 0) != 0:
        continue
    found = visit(n)
    if found:
        print("cycle: " + " ".join(found))
        break
else:
    print("acyclic")
