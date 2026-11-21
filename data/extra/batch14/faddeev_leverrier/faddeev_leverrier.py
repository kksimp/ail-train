def matmul(a, b):
    n = len(a)
    return [[sum(a[i][k] * b[k][j] for k in range(n)) for j in range(n)] for i in range(n)]
def char_poly(a):
    n = len(a)
    c = [1]
    m = [[0] * n for _ in range(n)]
    for k in range(1, n + 1):
        nx = matmul(a, m)
        for i in range(n):
            nx[i][i] += c[k - 1]
        m = nx
        am = matmul(a, m)
        tr = sum(am[i][i] for i in range(n))
        q = abs(tr) // k
        c.append(-q if tr > 0 else q)
    return c
def fl(xs):
    return "[" + ", ".join(map(str, xs)) + "]"
mats = [[[2, 1], [1, 3]], [[1, 2, 0], [0, 1, 3], [4, 0, 1]], [[2, 0, 0, 1], [1, 3, 0, 0], [0, 1, 1, 2], [0, 0, 1, 4]]]
for a in mats:
    c = char_poly(a)
    n = len(a)
    sign = 1 if n % 2 == 0 else -1
    print(f"A = [{', '.join(fl(r) for r in a)}]")
    check = [[0] * n for _ in range(n)]
    power = [[1 if i == j else 0 for j in range(n)] for i in range(n)]
    for k in range(n + 1):
        coef = c[n - k]
        for i in range(n):
            for j in range(n):
                check[i][j] += coef * power[i][j]
        power = matmul(power, a)
    zero = all(v == 0 for row in check for v in row)
    print(f"    coefficients {fl(c)}, det {sign * c[n]}, p(A) = 0: {'true' if zero else 'false'}")
