def cores(n, links):
    adj = [[] for _ in range(n)]
    deg = [0] * n
    gone = [False] * n
    core = [0] * n
    for a, b in links:
        adj[a].append(b)
        adj[b].append(a)
        deg[a] += 1
        deg[b] += 1
    k = 0
    for step in range(n):
        pick = -1
        for v in range(n):
            if not gone[v] and (pick < 0 or deg[v] < deg[pick]):
                pick = v
        k = max(k, deg[pick])
        core[pick] = k
        gone[pick] = True
        for w in adj[pick]:
            if not gone[w]:
                deg[w] -= 1
    return core

names = ["Ada", "Bo", "Cy", "Di", "Ed", "Flo", "Gus", "Hy", "Ira", "Jo"]
links = [[0, 1], [0, 2], [0, 3], [1, 2], [1, 3], [2, 3], [3, 4], [4, 5], [4, 6], [5, 6], [6, 7], [7, 8], [2, 4], [9, 8]]
core = cores(len(names), links)
for v in range(len(names)):
    print(f"{names[v]:<4} core {core[v]}")
top = max(core)
group = [names[v] for v in range(len(names)) if core[v] == top]
shown = " ".join(group)
print(f"tightest group ({top}-core): {shown}")
