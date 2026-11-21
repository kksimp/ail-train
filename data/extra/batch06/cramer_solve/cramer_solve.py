from math import gcd
def d3(m): return m[0][0] * (m[1][1] * m[2][2] - m[1][2] * m[2][1]) - m[0][1] * (m[1][0] * m[2][2] - m[1][2] * m[2][0]) + m[0][2] * (m[1][0] * m[2][1] - m[1][1] * m[2][0])
def fr(n, d):
    g = gcd(n, d); a = n // g; b = d // g
    if b < 0: a = -a; b = -b
    return f"{a}" if b == 1 else f"{a}/{b}"
for A, R in [([[2, 1, -1], [-3, -1, 2], [-2, 1, 2]], [8, -11, -3]), ([[1, 1, 1], [0, 2, 5], [2, 5, -1]], [6, -4, 27]), ([[1, 2, 3], [2, 4, 6], [1, 0, 1]], [1, 2, 3]), ([[3, 0, 2], [1, 4, 0], [0, 2, 5]], [7, 1, 2])]:
    d = d3(A)
    if d == 0: print("determinant 0: no single solution"); continue
    P = []
    for c in range(3):
        m = [row[:] for row in A]
        for r in range(3): m[r][c] = R[r]
        P.append(fr(d3(m), d))
    print(f"det {d}: x = {P[0]}, y = {P[1]}, z = {P[2]}")
