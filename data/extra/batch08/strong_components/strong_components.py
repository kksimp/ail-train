names = ["Abbey", "Bridge", "Castle", "Dock", "Exchange", "Fountain", "Gate", "Harbour"]
streets = [[0, 1], [1, 2], [2, 0], [2, 3], [3, 4], [4, 5], [5, 3], [6, 5], [6, 7], [7, 6]]
n = 8; adj = [[] for i in range(n)]; radj = [[] for i in range(n)]
for a, b in streets: adj[a].append(b); radj[b].append(a)
seen = [False] * n; order = []
def od(v):
    seen[v] = True
    for w in adj[v]:
        if not seen[w]: od(w)
    order.append(v)
for v in range(n):
    if not seen[v]: od(v)
again = [False] * n
def col(v, g):
    again[v] = True; g.append(v)
    for w in radj[v]:
        if not again[w]: col(w, g)
cnt = 0
for v in reversed(order):
    if not again[v]:
        g = []; col(v, g); cnt += 1; print(f"group {cnt}: {', '.join(names[x] for x in sorted(g))}")
