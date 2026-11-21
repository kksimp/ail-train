def solve(w, cost, cut):
    n = len(w)
    for i in range(n):
        cost.append([0] * n)
        cut.append([-1] * n)
    for gap in range(2, n):
        for i in range(0, n - gap):
            j = i + gap
            best = -1
            for k in range(i + 1, j):
                c = cost[i][k] + cost[k][j] + w[i] * w[k] * w[j]
                if best < 0 or c < best:
                    best = c
                    cut[i][j] = k
            cost[i][j] = best

def triangles(cut, i, j, out):
    if j - i < 2:
        return
    k = cut[i][j]
    out.append(f"{i}-{k}-{j}")
    triangles(cut, i, k, out)
    triangles(cut, k, j, out)

for w in [[1, 2, 3], [3, 7, 4, 5], [1, 3, 1, 4, 1, 5], [5, 2, 8, 1, 6, 3, 7]]:
    cost = []
    cut = []
    solve(w, cost, cut)
    out = []
    triangles(cut, 0, len(w) - 1, out)
    shown = " ".join(out)
    print(f"weights {w}: cost {cost[0][len(w) - 1]} using {shown}")
