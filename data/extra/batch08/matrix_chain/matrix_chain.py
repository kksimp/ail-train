def brackets(sp, i, j):
    if i == j: return f"M{i + 1}"
    k = sp[i][j]; return f"({brackets(sp, i, k)}{brackets(sp, k + 1, j)})"
def chain_left(d): return sum(d[0] * d[k] * d[k + 1] for k in range(1, len(d) - 1))
def chain(d):
    n = len(d) - 1; cost = [[0] * n for i in range(n)]; sp = [[0] * n for i in range(n)]
    for span in range(2, n + 1):
        for i in range(n - span + 1):
            j = i + span - 1; cost[i][j] = -1
            for k in range(i, j):
                c = cost[i][k] + cost[k + 1][j] + d[i] * d[k + 1] * d[j + 1]
                if cost[i][j] < 0 or c < cost[i][j]: cost[i][j] = c; sp[i][j] = k
    print(f"{brackets(sp, 0, n - 1)}: {cost[0][n - 1]} multiplications (left to right {chain_left(d)})")
for d in [[30, 35, 15, 5, 10, 20, 25], [10, 20, 30], [40, 20, 30, 10, 30], [5, 100, 2, 50, 4]]: chain(d)
