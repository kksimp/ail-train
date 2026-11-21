def visit(u, adj, alive, colour, path):
    colour[u] = 1
    path.append(u)
    for v in adj[u]:
        if alive[v]:
            if colour[v] == 1:
                at = path.index(v)
                return path[at:]
            if colour[v] == 0:
                found = visit(v, adj, alive, colour, path)
                if len(found) > 0:
                    return found
    colour[u] = 2
    path.pop()
    return []

adj = [[1], [2, 4], [0], [4], [5], [3], [5]]
n = len(adj)
alive = [True] * n
while True:
    colour = [0] * n
    path = []
    cycle = []
    for s in range(n):
        if alive[s] and colour[s] == 0 and len(cycle) == 0:
            cycle = visit(s, adj, alive, colour, path)
    if len(cycle) == 0:
        break
    shown = " -> ".join(f"P{p}" for p in cycle)
    victim = max(cycle)
    print(f"deadlock: {shown} -> P{cycle[0]}; abort P{victim}")
    alive[victim] = False
left = " ".join(f"P{p}" for p in [i for i in range(n) if alive[i]])
print(f"no deadlock left among {left}")
