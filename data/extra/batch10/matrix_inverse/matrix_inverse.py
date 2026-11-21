def invert(a0):
    n = len(a0)
    a = []
    for i in range(n):
        row = a0[i][:]
        for j in range(n):
            row.append(1.0 if i == j else 0.0)
        a.append(row)
    for col in range(n):
        best = col
        for r in range(col + 1, n):
            if abs(a[r][col]) > abs(a[best][col]):
                best = r
        a[col], a[best] = a[best], a[col]
        p = a[col][col]
        for c in range(2 * n):
            a[col][c] = a[col][c] / p
        for r in range(n):
            if r != col:
                f = a[r][col]
                for c in range(2 * n):
                    a[r][c] -= f * a[col][c]
    return [a[i][n:] for i in range(n)]

def det3(m):
    return m[0][0] * (m[1][1] * m[2][2] - m[1][2] * m[2][1]) - m[0][1] * (m[1][0] * m[2][2] - m[1][2] * m[2][0]) + m[0][2] * (m[1][0] * m[2][1] - m[1][1] * m[2][0])

for a in [[[2.0, 1.0, 1.0], [1.0, 3.0, 2.0], [1.0, 0.0, 0.0]], [[0.0, 1.0, 2.0], [1.0, 0.0, 3.0], [4.0, -3.0, 8.0]], [[3.0, 2.0, 0.0], [1.0, -1.0, 0.0], [0.0, 5.0, 1.0]]]:
    inv = invert(a)
    d = det3(a)
    print(f"det {int(round(d))}, det x inverse:")
    for row in inv:
        print(f"    {[int(round(v * d)) for v in row]}")
    worst = 0.0
    for i in range(3):
        for j in range(3):
            s = 0.0
            for k in range(3):
                s += a[i][k] * inv[k][j]
            target = 1.0 if i == j else 0.0
            if abs(s - target) > worst:
                worst = abs(s - target)
    print(f"    A x inverse is the identity: {str(worst < 0.000000001).lower()}")
