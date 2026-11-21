names = ["Quay", "Mill", "Fort", "Gate", "Hall", "Inn", "Keep", "Lane", "Moor"]
links = [[0, 1], [1, 2], [2, 3], [3, 4], [2, 5], [5, 6], [6, 7], [1, 8]]
n = len(names)
adj = [[] for _ in range(n)]
deg = [0] * n
alive = [True] * n
for l in links:
    adj[l[0]].append(l[1])
    adj[l[1]].append(l[0])
    deg[l[0]] += 1
    deg[l[1]] += 1
left = n
rnd = 1
while left > 2:
    leaves = [i for i in range(n) if alive[i] and deg[i] == 1]
    shown = ", ".join(names[i] for i in leaves)
    print(f"round {rnd}: remove {shown}")
    for u in leaves:
        alive[u] = False
        left -= 1
        for v in adj[u]:
            deg[v] -= 1
    rnd += 1
centre = " and ".join(names[i] for i in range(n) if alive[i])
print(f"centre: {centre}")
print(f"radius: {rnd - 1} hops")
