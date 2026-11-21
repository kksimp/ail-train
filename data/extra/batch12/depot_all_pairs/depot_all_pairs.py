INF = 1000000

def route(nxt, a, b, names):
    parts = [names[a]]
    u = a
    while u != b:
        u = nxt[u][b]
        parts.append(names[u])
    return " > ".join(parts)

names = ["Ash", "Birch", "Cedar", "Dale", "Elm"]
roads = [[0, 1, 7], [0, 2, 3], [2, 1, 2], [1, 3, 4], [2, 3, 9], [3, 4, 2], [2, 4, 12]]
n = len(names)
dist = []
nxt = []
for i in range(n):
    dist.append([0 if i == j else INF for j in range(n)])
    nxt.append(list(range(n)))
for r in roads:
    dist[r[0]][r[1]] = r[2]
    dist[r[1]][r[0]] = r[2]
for k in range(n):
    for i in range(n):
        for j in range(n):
            if dist[i][k] + dist[k][j] < dist[i][j]:
                dist[i][j] = dist[i][k] + dist[k][j]
                nxt[i][j] = nxt[i][k]
for i in range(n):
    cells = "".join(f"{d:>4}" for d in dist[i])
    print(f"{names[i]:<6}{cells}")
print(route(nxt, 0, 4, names))
print(route(nxt, 1, 4, names))
print(route(nxt, 4, 0, names))
