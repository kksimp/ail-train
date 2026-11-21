import sys
names = ["Hub", "North", "South", "Depot", "Lab", "Store", "Annex"]
links = [[0, 1], [1, 2], [2, 0], [1, 3], [3, 4], [4, 5], [5, 3], [4, 6]]
adj = [[] for n in names]; disc = [0] * 7; low = [0] * 7; clock = [0]; out = []
for a, b in links: adj[a].append(b); adj[b].append(a)
def dfs(v, frm):
    clock[0] += 1; disc[v] = low[v] = clock[0]
    for w in adj[v]:
        if disc[w] == 0:
            dfs(w, v); low[v] = min(low[v], low[w])
            if low[w] > disc[v]: out.append(f"{names[v]}-{names[w]}")
        elif w != frm: low[v] = min(low[v], disc[w])
dfs(0, -1)
print(f"critical links: {', '.join(out)}")
print(f"{len(out)} of {len(links)} links are critical")
