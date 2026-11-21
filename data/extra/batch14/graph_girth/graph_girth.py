def girth(n, edges):
    adj = [[] for _ in range(n)]
    for a, b in edges:
        adj[a].append(b)
        adj[b].append(a)
    best = n + 1
    for s in range(n):
        dist = [-1] * n
        parent = [-1] * n
        dist[s] = 0
        queue = [s]
        head = 0
        while head < len(queue):
            u = queue[head]
            head += 1
            for w in adj[u]:
                if dist[w] == -1:
                    dist[w] = dist[u] + 1
                    parent[w] = u
                    queue.append(w)
                elif parent[u] != w:
                    best = min(best, dist[u] + dist[w] + 1)
    return 0 if best > n else best

def cube():
    es = []
    for v in range(8):
        for bit in [1, 2, 4]:
            w = v ^ bit
            if v < w:
                es.append([v, w])
    return es

petersen = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 0], [0, 5], [1, 6], [2, 7], [3, 8], [4, 9], [5, 7], [7, 9], [9, 6], [6, 8], [8, 5]]
k4 = [[0, 1], [0, 2], [0, 3], [1, 2], [1, 3], [2, 3]]
hexring = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 0]]
tree = [[0, 1], [0, 2], [1, 3], [1, 4], [2, 5]]
for name, n, edges in [("K4", 4, k4), ("cube", 8, cube()), ("Petersen", 10, petersen), ("hexagon", 6, hexring), ("tree", 6, tree)]:
    g = girth(n, edges)
    text = "no cycle" if g == 0 else f"girth {g}"
    print(f"{name:<9} {n:>2} vertices {len(edges):>2} edges: {text}")
