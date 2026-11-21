INF = 1000000

def best_pairing(odd, dist, used):
    first = -1
    for i in range(len(odd)):
        if first < 0 and not used[i]:
            first = i
    if first < 0:
        return 0
    used[first] = True
    best = INF
    for j in range(len(odd)):
        if not used[j]:
            used[j] = True
            cost = dist[odd[first]][odd[j]] + best_pairing(odd, dist, used)
            if cost < best:
                best = cost
            used[j] = False
    used[first] = False
    return best

names = ["A", "B", "C", "D", "E", "F"]
streets = [[0, 1, 4], [0, 2, 3], [1, 2, 2], [1, 3, 5], [2, 4, 6], [3, 4, 1], [3, 5, 4], [4, 5, 3]]
n = len(names)
dist = [[0 if i == j else INF for j in range(n)] for i in range(n)]
degree = [0] * n
total = 0
for a, b, w in streets:
    dist[a][b] = w
    dist[b][a] = w
    degree[a] += 1
    degree[b] += 1
    total += w
for k in range(n):
    for i in range(n):
        for j in range(n):
            if dist[i][k] + dist[k][j] < dist[i][j]:
                dist[i][j] = dist[i][k] + dist[k][j]
odd = [v for v in range(n) if degree[v] % 2 == 1]
shown = " ".join(names[v] for v in odd)
used = [False for v in odd]
extra = best_pairing(odd, dist, used)
print(f"streets: {len(streets)}, total length {total}")
print(f"odd junctions: {shown}")
print(f"cheapest repeat of streets: {extra}")
print(f"shortest sweeping round: {total + extra}")
