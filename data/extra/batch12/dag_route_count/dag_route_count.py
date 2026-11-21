def topo(edges):
    indeg = {}
    places = []
    for e in edges:
        for p in e:
            if p not in indeg:
                indeg[p] = 0
                places.append(p)
        indeg[e[1]] += 1
    ready = [p for p in places if indeg[p] == 0]
    order = []
    while ready:
        u = ready.pop(0)
        order.append(u)
        for e in edges:
            if e[0] == u:
                indeg[e[1]] -= 1
                if indeg[e[1]] == 0:
                    ready.append(e[1])
    return order

trails = [["Summit", "Ridge"], ["Summit", "Col"], ["Ridge", "Tarn"], ["Col", "Tarn"], ["Col", "Forest"], ["Tarn", "Bridge"], ["Forest", "Bridge"], ["Tarn", "Forest"], ["Bridge", "Car park"], ["Forest", "Car park"], ["Ridge", "Bridge"]]
order = topo(trails)
print(f"order: {' > '.join(order)}")
ways = {p: 0 for p in order}
longest = {p: 0 for p in order}
ways[order[0]] = 1
for u in order:
    for e in trails:
        if e[0] == u:
            ways[e[1]] += ways[u]
            longest[e[1]] = max(longest[e[1]], longest[u] + 1)
for p in order:
    print(f"{p:<9} {ways[p]:>2} routes, longest {longest[p]} legs")
