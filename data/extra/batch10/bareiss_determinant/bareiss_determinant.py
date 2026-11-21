def bareiss(m0):
    m = [row[:] for row in m0]
    n = len(m)
    sign = 1
    prev = 1
    for k in range(n - 1):
        if m[k][k] == 0:
            swap = -1
            for r in range(k + 1, n):
                if swap < 0 and m[r][k] != 0:
                    swap = r
            if swap < 0:
                return 0
            m[k], m[swap] = m[swap], m[k]
            sign = -sign
        for i in range(k + 1, n):
            for j in range(k + 1, n):
                v = m[i][j] * m[k][k] - m[i][k] * m[k][j]
                m[i][j] = abs(v) // abs(prev) * (1 if (v >= 0) == (prev > 0) else -1)
        prev = m[k][k]
    return sign * m[n - 1][n - 1]

def cofactor(m):
    n = len(m)
    if n == 1:
        return m[0][0]
    total = 0
    for c in range(n):
        minor = [[m[r][j] for j in range(n) if j != c] for r in range(1, n)]
        term = m[0][c] * cofactor(minor)
        total += term if c % 2 == 0 else -term
    return total

mats = [[[2, -1, 0, 3], [1, 4, -2, 1], [0, 3, 5, -1], [2, 0, 1, 6]], [[0, 2, 1, 4], [3, 0, 2, 1], [1, 1, 0, 2], [2, 3, 1, 0]], [[1, 2, 3, 4], [2, 4, 6, 8], [0, 1, 0, 1], [5, 3, 2, 1]], [[7, 1, 3, 2], [4, 9, 1, 5], [2, 6, 8, 1], [3, 2, 4, 10]]]
for m in mats:
    print(f"{m}: Bareiss {bareiss(m)}, cofactors {cofactor(m)}")
h = [[i + j + 1 for j in range(5)] for i in range(5)]
print(f"5x5 with rows i + j + 1: {bareiss(h)} (rows are dependent)")
