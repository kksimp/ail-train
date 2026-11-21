names = ["Alpha", "Bravo", "Charlie", "Delta", "Echo", "Foxtrot"]
relays = [[0, 1], [1, 2], [2, 0], [2, 3], [3, 4], [5, 4], [4, 3]]
n = len(names)
r = [[i == j for j in range(n)] for i in range(n)]
for e in relays:
    r[e[0]][e[1]] = True
for k in range(n):
    for i in range(n):
        for j in range(n):
            if r[i][k] and r[k][j]:
                r[i][j] = True
for i in range(n):
    cells = " ".join("1" if b else "0" for b in r[i])
    print(f"{names[i]:<8} {cells}")
for i in range(n):
    reach = sum(1 for b in r[i] if b) - 1
    heard = len([j for j in range(n) if r[j][i] and j != i])
    print(f"{names[i]} reaches {reach}, heard by {heard}")
