def distance_sums(n, edges):
    adj = [[] for _ in range(n)]
    for a, b in edges:
        adj[a].append(b)
        adj[b].append(a)
    parent = [-1] * n
    depth = [0] * n
    order = [0]
    head = 0
    while head < len(order):
        u = order[head]
        head += 1
        for v in adj[u]:
            if v != parent[u] and v != 0:
                parent[v] = u
                depth[v] = depth[u] + 1
                order.append(v)
    size = [1] * n
    i = n - 1
    while i >= 1:
        size[parent[order[i]]] += size[order[i]]
        i -= 1
    ans = [0] * n
    ans[0] = sum(depth)
    for j in range(1, n):
        v = order[j]
        ans[v] = ans[parent[v]] - size[v] + (n - size[v])
    return ans

names = ["Ash", "Birch", "Cedar", "Dale", "Elm", "Fern", "Glen", "Holt", "Ivy"]
tracks = [[0, 1], [0, 2], [1, 3], [1, 4], [2, 5], [5, 6], [5, 7], [7, 8]]
sums = distance_sums(len(names), tracks)
for v in range(len(names)):
    print(f"{names[v]:<6} total walk to all others: {sums[v]:>2}")
best = min(sums)
winners = [names[v] for v in range(len(names)) if sums[v] == best]
shown = ", ".join(winners)
print(f"best meeting village: {shown} ({best})")
