import math

def cholesky(a):
    n = len(a)
    l = [[0.0] * n for _ in range(n)]
    for i in range(n):
        for j in range(i + 1):
            s = a[i][j]
            for k in range(j):
                s -= l[i][k] * l[j][k]
            if i == j:
                if s <= 0.0:
                    return None, f"not positive definite (pivot {s:.3f} at row {i + 1})"
                l[i][i] = math.sqrt(s)
            else:
                l[i][j] = s / l[j][j]
    return l, None

def row_text(row):
    return " ".join(f"{v:>8.4f}" for v in row)

mats = [[[4.0, 12.0, -16.0], [12.0, 37.0, -43.0], [-16.0, -43.0, 98.0]], [[25.0, 15.0, -5.0], [15.0, 18.0, 0.0], [-5.0, 0.0, 11.0]], [[2.0, 3.0, 1.0], [3.0, 2.0, 1.0], [1.0, 1.0, 5.0]]]
for a in mats:
    l, err = cholesky(a)
    if err is None:
        print(f"L for {a}:")
        for row in l:
            print(f"    {row_text(row)}")
        det = 1.0
        for i in range(3):
            det *= l[i][i] * l[i][i]
        print(f"    determinant {det:.3f}")
    else:
        print(f"{a}: {err}")
