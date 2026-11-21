names = ["reservoir", "A", "B", "C", "D", "town"]
cap = [[0, 16, 13, 0, 0, 0], [0, 0, 10, 12, 0, 0], [0, 4, 0, 0, 14, 0], [0, 0, 9, 0, 0, 20], [0, 0, 0, 7, 0, 4], [0, 0, 0, 0, 0, 0]]
n = 6; s = 0; t = 5; total = 0
while True:
    par = [-1] * n; par[s] = s; q = [s]; h = 0
    while h < len(q) and par[t] == -1:
        u = q[h]; h += 1
        for v in range(n):
            if par[v] == -1 and cap[u][v] > 0: par[v] = u; q.append(v)
    if par[t] == -1: break
    push = 1000000; v = t; route = []
    while v != s:
        u = par[v]; push = min(push, cap[u][v]); route.insert(0, names[v]); v = u
    route.insert(0, names[s]); v = t
    while v != s: u = par[v]; cap[u][v] -= push; cap[v][u] += push; v = u
    total += push; print(f"push {push:>2}: {' > '.join(route)}")
print(f"maximum flow {total} litres a second")
