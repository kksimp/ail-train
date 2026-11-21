def decompose(a):
    n = len(a)
    l = [[0.0] * n for _ in range(n)]
    u = [[0.0] * n for _ in range(n)]
    for i in range(n):
        for k in range(i, n):
            s = 0.0
            for j in range(i):
                s += l[i][j] * u[j][k]
            u[i][k] = a[i][k] - s
        l[i][i] = 1.0
        for k in range(i + 1, n):
            s = 0.0
            for j in range(i):
                s += l[k][j] * u[j][i]
            l[k][i] = (a[k][i] - s) / u[i][i]
    return [l, u]

def solve(l, u, b):
    n = len(b)
    y = [0.0] * n
    for i in range(n):
        s = b[i]
        for j in range(i):
            s -= l[i][j] * y[j]
        y[i] = s
    x = [0.0] * n
    i = n - 1
    while i >= 0:
        s = y[i]
        for j in range(i + 1, n):
            s -= u[i][j] * x[j]
        x[i] = s / u[i][i]
        i -= 1
    return x

def show(name, m):
    for row in m:
        print(f"{name} | {' '.join(f'{v:>8.3f}' for v in row)}")

a = [[4.0, 3.0, 2.0], [8.0, 7.0, 9.0], [4.0, 6.0, 25.0]]
l, u = decompose(a)
show("L", l)
show("U", u)
det = 1.0
for i in range(3):
    det *= u[i][i]
print(f"determinant {det:.3f}")
for b in [[9.0, 24.0, 35.0], [2.0, 1.0, 3.0]]:
    x = solve(l, u, b)
    print(f"b = {b}: x = [{x[0]:.5f}, {x[1]:.5f}, {x[2]:.5f}]")
