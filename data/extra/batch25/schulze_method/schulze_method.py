names = ["A", "B", "C", "D", "E"]
groups = [(5, "ACBED"), (5, "ADECB"), (8, "BEDAC"), (3, "CABED"), (7, "CAEBD"), (2, "CBADE"), (7, "DCEBA"), (8, "EBADC")]
n = len(names)
d = [[0] * n for _ in range(n)]
for count, order in groups:
    pos = [ord(c) - 65 for c in order]
    for x in range(n):
        for y in range(x + 1, n):
            d[pos[x]][pos[y]] += count
p = [[0] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if i != j and d[i][j] > d[j][i]:
            p[i][j] = d[i][j]
for k in range(n):
    for i in range(n):
        for j in range(n):
            if i != j and i != k and j != k:
                p[i][j] = max(p[i][j], min(p[i][k], p[k][j]))

def show(xs):
    return "[" + ", ".join(str(x) for x in xs) + "]"

for i in range(n):
    print(f"{names[i]}  d {show(d[i])}  p {show(p[i])}")
wins = [len([j for j in range(n) if j != i and p[i][j] > p[j][i]]) for i in range(n)]
ranking = [names[i] for i in sorted(range(n), key=lambda i: -wins[i])]
print(f"ranking: {' > '.join(ranking)}")
