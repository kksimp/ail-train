def degree(adj, removed, v):
    return sum(1 for u in range(len(adj)) if adj[v][u] and not removed[u])

names = ["a", "b", "c", "d", "e", "f", "g"]
edges = [[0, 1], [0, 2], [0, 3], [1, 2], [1, 3], [2, 3], [3, 4], [4, 5], [5, 6], [4, 6], [2, 4]]
n = len(names)
k = 3
adj = [[False] * n for _ in range(n)]
removed = [False] * n
for e in edges:
    adj[e[0]][e[1]] = True
    adj[e[1]][e[0]] = True
stack = []
while len(stack) < n:
    pick = -1
    for i in range(n):
        if not removed[i] and degree(adj, removed, i) < k:
            pick = i
            break
    if pick < 0:
        for i in range(n):
            if not removed[i] and (pick < 0 or degree(adj, removed, i) > degree(adj, removed, pick)):
                pick = i
        print(f"stuck: {names[pick]} is a spill candidate")
    removed[pick] = True
    stack.append(pick)
colour = [-1] * n
while stack:
    v = stack.pop()
    used = set()
    for u in range(n):
        if adj[v][u] and colour[u] >= 0:
            used.add(colour[u])
    c = 0
    while c in used:
        c += 1
    if c < k:
        colour[v] = c
        print(f"{names[v]} -> r{c}")
    else:
        print(f"{names[v]} -> spilled to memory")
