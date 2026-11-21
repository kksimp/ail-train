INF = 999
names = ["A", "B", "C", "D", "E"]
n = len(names)
link = [[0 if i == j else INF for j in range(n)] for i in range(n)]
for e in [[0, 1, 2], [1, 2, 3], [0, 3, 7], [2, 3, 1], [3, 4, 2], [2, 4, 6]]:
    link[e[0]][e[1]] = e[2]
    link[e[1]][e[0]] = e[2]
dist = [list(r) for r in link]
hop = [list(range(n)) for _ in range(n)]
rnd = 0
changed = True
while changed:
    changed = False
    rnd += 1
    old = [list(r) for r in dist]
    for i in range(n):
        for d in range(n):
            for k in range(n):
                if k != i and link[i][k] < INF and link[i][k] + old[k][d] < dist[i][d]:
                    dist[i][d] = link[i][k] + old[k][d]
                    hop[i][d] = k
                    changed = True
    a_row = " ".join(str(c) for c in dist[0])
    print(f"round {rnd}: A sees {a_row}")
for d in range(1, n):
    print(f"A to {names[d]}: cost {dist[0][d]} via {names[hop[0][d]]}")
