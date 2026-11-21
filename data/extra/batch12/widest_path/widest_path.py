import heapq

def widest(n, links, src, prev):
    best = [0] * n
    best[src] = 1000
    h = [-(1000 * 100 + src)]
    while h:
        v = -heapq.heappop(h)
        w = v // 100
        u = v % 100
        if w < best[u]:
            continue
        for l in links:
            other = -1
            if l[0] == u:
                other = l[1]
            elif l[1] == u:
                other = l[0]
            if other >= 0:
                cand = min(w, l[2])
                if cand > best[other]:
                    best[other] = cand
                    prev[other] = u
                    heapq.heappush(h, -(cand * 100 + other))
    return best

sites = ["Oslo", "Paris", "Rome", "Sofia", "Turin", "Vienna"]
links = [[0, 1, 40], [0, 2, 10], [1, 2, 25], [1, 3, 15], [2, 3, 30], [2, 4, 35], [3, 5, 20], [4, 5, 12], [1, 4, 18]]
prev = [-1] * 6
best = widest(len(sites), links, 0, prev)
for t in range(1, len(sites)):
    path = [sites[t]]
    u = t
    while prev[u] >= 0:
        u = prev[u]
        path.append(sites[u])
    path.reverse()
    print(f"{sites[t]:<7} {best[t]:>3} Gbps via {' > '.join(path)}")
