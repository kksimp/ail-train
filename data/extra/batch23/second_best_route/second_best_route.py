import heapq
INF = 1000000

def two_best(n, links, src):
    adj = [[] for _ in range(n)]
    first = [INF] * n
    second = [INF] * n
    for a, b, w in links:
        adj[a].append([b, w])
        adj[b].append([a, w])
    first[src] = 0
    h = [src]
    while h:
        code = heapq.heappop(h)
        d = code // 100
        u = code % 100
        if d > second[u]:
            continue
        for v, w in adj[u]:
            nd = d + w
            if nd < first[v]:
                old = first[v]
                first[v] = nd
                heapq.heappush(h, nd * 100 + v)
                if old < second[v]:
                    second[v] = old
                    heapq.heappush(h, old * 100 + v)
            elif nd > first[v] and nd < second[v]:
                second[v] = nd
                heapq.heappush(h, nd * 100 + v)
    return [first, second]

places = ["Station", "Mill", "Ford", "Church", "Green", "Hospital"]
links = [[0, 1, 4], [0, 2, 2], [1, 2, 1], [1, 3, 5], [2, 3, 8], [2, 4, 10], [3, 4, 2], [3, 5, 6], [4, 5, 3]]
r = two_best(len(places), links, 0)
for v in range(1, len(places)):
    extra = r[1][v] - r[0][v]
    print(f"{places[v]:<8} best {r[0][v]:>2}, backup {r[1][v]:>2} (+{extra})")
