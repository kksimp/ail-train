def find_cycle(n, edges):
    dist = [0] * n
    pred = [-1] * n
    last = -1
    for rnd in range(n):
        last = -1
        for e in edges:
            if dist[e[0]] + e[2] < dist[e[1]]:
                dist[e[1]] = dist[e[0]] + e[2]
                pred[e[1]] = e[0]
                last = e[1]
    if last < 0:
        return []
    v = last
    for step in range(n):
        v = pred[v]
    cycle = [v]
    u = pred[v]
    while u != v:
        cycle.append(u)
        u = pred[u]
    cycle.reverse()
    return cycle

def cost(edges, a, b):
    for e in edges:
        if e[0] == a and e[1] == b:
            return e[2]
    return 0

def show(title, names, edges):
    cycle = find_cycle(len(names), edges)
    if len(cycle) == 0:
        print(f"{title}: no loop goes back in time")
        return
    total = 0
    parts = []
    for i in range(len(cycle)):
        a = cycle[i]
        b = cycle[(i + 1) % len(cycle)]
        total += cost(edges, a, b)
        parts.append(names[a])
    parts.append(names[cycle[0]])
    route = " -> ".join(parts)
    print(f"{title}: {route} arrives {-total} hours before it left")

names = ["barn", "pond", "mill", "well", "orchard"]
fair = [[0, 1, 3], [1, 2, 2], [2, 3, 4], [3, 0, -5], [1, 4, 1], [4, 2, 2], [3, 4, 6]]
for e in fair:
    print(f"  {names[e[0]]:<7} -> {names[e[1]]:<7} {e[2]:>3}")
show("farm 1", names, fair)
tilted = [[0, 1, 3], [1, 2, 2], [2, 3, 4], [3, 0, -5], [1, 4, 1], [4, 2, -4], [3, 4, 6]]
show("farm 2", names, tilted)
