import heapq

def routes(n, links, src):
    adj = [[] for _ in range(n)]
    dist = [1000000] * n
    ways = [0] * n
    for a, b, w in links:
        adj[a].append([b, w])
        adj[b].append([a, w])
    dist[src] = 0
    ways[src] = 1
    h = [src]
    while h:
        code = heapq.heappop(h)
        d = code // 100
        u = code % 100
        if d > dist[u]:
            continue
        for v, w in adj[u]:
            nd = d + w
            if nd < dist[v]:
                dist[v] = nd
                ways[v] = ways[u]
                heapq.heappush(h, nd * 100 + v)
            elif nd == dist[v]:
                ways[v] += ways[u]
    return [dist, ways]

stops = ["Depot", "Market", "Bridge", "Park", "School", "Museum", "Harbour", "Airport"]
links = [[0, 1, 4], [0, 2, 3], [1, 3, 2], [2, 3, 3], [1, 4, 5], [3, 4, 3], [3, 5, 4], [4, 6, 2], [5, 6, 1], [2, 5, 7], [6, 7, 6], [4, 7, 8]]
result = routes(len(stops), links, 0)
for v in range(1, len(stops)):
    print(f"{stops[v]:<8} {result[0][v]:>2} min, {result[1][v]} shortest routes")
