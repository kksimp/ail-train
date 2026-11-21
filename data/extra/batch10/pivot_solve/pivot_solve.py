def solve(a0, b0):
    a = [row[:] for row in a0]
    b = b0[:]
    n = len(b)
    for col in range(n):
        best = col
        for r in range(col + 1, n):
            if abs(a[r][col]) > abs(a[best][col]):
                best = r
        if best != col:
            a[col], a[best] = a[best], a[col]
            b[col], b[best] = b[best], b[col]
        for r in range(col + 1, n):
            f = a[r][col] / a[col][col]
            for c in range(col, n):
                a[r][c] -= f * a[col][c]
            b[r] -= f * b[col]
    x = [0.0] * n
    row = n - 1
    while row >= 0:
        s = b[row]
        for c in range(row + 1, n):
            s -= a[row][c] * x[c]
        x[row] = s / a[row][row]
        row -= 1
    return x

def residual(a, b, x):
    worst = 0.0
    for i in range(len(b)):
        s = 0.0
        for j in range(len(b)):
            s += a[i][j] * x[j]
        if abs(s - b[i]) > worst:
            worst = abs(s - b[i])
    return worst

a = [[0.0, 2.0, 1.0], [1.0, -2.0, -3.0], [-1.0, 1.0, 2.0]]
b = [-8.0, 0.0, 3.0]
x = solve(a, b)
print(f"3x3 with a zero first pivot: x = {x[0]:.4f}, y = {x[1]:.4f}, z = {x[2]:.4f}")
print(f"largest residual below 1e-12: {str(residual(a, b, x) < 0.000000000001).lower()}")
m = [[4.0, -2.0, 1.0, 3.0], [3.0, 6.0, -4.0, 2.0], [2.0, 1.0, 8.0, -5.0], [1.0, 3.0, -2.0, 7.0]]
v = [20.0, -1.0, 10.0, 15.0]
y = solve(m, v)
for i in range(4):
    print(f"x{i + 1} = {y[i]:>9.5f}")
print(f"largest residual below 1e-12: {str(residual(m, v, y) < 0.000000000001).lower()}")
