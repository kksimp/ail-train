def far(start, adj, wt):
    dist = [-1] * len(adj)
    dist[start] = 0
    queue = [start]
    head = 0
    while head < len(queue):
        u = queue[head]
        head += 1
        for k in range(len(adj[u])):
            v = adj[u][k]
            if dist[v] < 0:
                dist[v] = dist[u] + wt[u][k]
                queue.append(v)
    return dist

def argmax(xs):
    best = 0
    for i in range(len(xs)):
        if xs[i] > xs[best]:
            best = i
    return best

names = ["Lobby", "Sales", "Ops", "Lab", "Print", "Server", "Archive", "Roof"]
links = [[0, 1, 30], [0, 2, 20], [2, 3, 45], [2, 4, 15], [3, 5, 25], [1, 6, 50], [4, 7, 10]]
adj = [[] for _ in names]
wt = [[] for _ in names]
for l in links:
    adj[l[0]].append(l[1]); wt[l[0]].append(l[2])
    adj[l[1]].append(l[0]); wt[l[1]].append(l[2])
first = far(0, adj, wt)
a = argmax(first)
second = far(a, adj, wt)
b = argmax(second)
print(f"farthest from {names[0]}: {names[a]} at {first[a]} m")
print(f"farthest from {names[a]}: {names[b]} at {second[b]} m")
print(f"longest cable run: {names[a]} to {names[b]}, {second[b]} m")
for i in range(len(names)):
    ecc = max(far(i, adj, wt))
    print(f"{names[i]:<8} reaches every office within {ecc} m")
