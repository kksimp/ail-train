INF = 1000000000

def gcd(a, b):
    return a if b == 0 else gcd(b, a % b)

def min_mean(n, edges):
    d = [[0] * n]
    for k in range(1, n + 1):
        row = [INF] * n
        for e in edges:
            before = d[k - 1][e[0]]
            if before < INF and before + e[2] < row[e[1]]:
                row[e[1]] = before + e[2]
        d.append(row)
    best_num = 0
    best_den = 0
    for v in range(n):
        if d[n][v] < INF:
            wn = 0
            wd = 0
            for k in range(n):
                if d[k][v] < INF:
                    num = d[n][v] - d[k][v]
                    den = n - k
                    if wd == 0 or num * wd > wn * den:
                        wn = num
                        wd = den
            if wd > 0 and (best_den == 0 or wn * best_den < best_num * wd):
                best_num = wn
                best_den = wd
    if best_den == 0:
        return [0, 0]
    g = gcd(best_num, best_den)
    return [best_num // g, best_den // g]

graphs = [("depot loops", 5, [[0, 1, 4], [1, 2, 2], [2, 0, 3], [2, 3, 1], [3, 4, 2], [4, 2, 4], [1, 3, 5]]), ("ferry ring", 4, [[0, 1, 1], [1, 0, 5], [1, 2, 2], [2, 1, 2], [2, 3, 6], [3, 2, 4]]), ("one-way chain", 4, [[0, 1, 3], [1, 2, 3], [2, 3, 3]])]
for name, n, edges in graphs:
    m = min_mean(n, edges)
    if m[1] == 0:
        print(f"{name}: no loop at all")
    else:
        avg = m[0] / m[1]
        print(f"{name}: cheapest loop averages {m[0]}/{m[1]} = {avg:.3f} per leg")
