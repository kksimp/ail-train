def det(m):
    n = len(m)
    sign = 1
    prev = 1
    for k in range(n - 1):
        if m[k][k] == 0:
            pick = -1
            for r in range(k + 1, n):
                if m[r][k] != 0 and pick < 0:
                    pick = r
            if pick < 0:
                return 0
            m[k], m[pick] = m[pick], m[k]
            sign = -sign
        for i in range(k + 1, n):
            for j in range(k + 1, n):
                v = m[i][j] * m[k][k] - m[i][k] * m[k][j]
                q = abs(v) // abs(prev)
                m[i][j] = q if (v >= 0) == (prev > 0) else -q
        prev = m[k][k]
    return sign * m[n - 1][n - 1]

def trees(n, edges):
    lap = [[0] * n for _ in range(n)]
    for a, b in edges:
        lap[a][a] += 1
        lap[b][b] += 1
        lap[a][b] -= 1
        lap[b][a] -= 1
    minor = [lap[i][1:] for i in range(1, n)]
    return det(minor)

def complete(n):
    return [[i, j] for i in range(n) for j in range(i + 1, n)]

for n in range(3, 8):
    k = trees(n, complete(n))
    cayley = n ** (n - 2)
    print(f"K{n}: {k} spanning trees, n^(n-2) = {cayley}")
cycle = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 0]]
print(f"cycle of 5: {trees(5, cycle)}")
wheel = [[0, 1], [0, 2], [0, 3], [0, 4], [1, 2], [2, 3], [3, 4], [4, 1]]
print(f"wheel with 4 spokes: {trees(5, wheel)}")
office = [[0, 1], [0, 2], [1, 2], [1, 3], [2, 3], [3, 4], [4, 5], [3, 5]]
print(f"office network: {trees(6, office)} ways to keep it connected with 5 cables")
