def ot(X):
    n = len(X); o = [1] * n; l = 1
    for i in range(n): o[i] = l; l *= X[i]
    r = 1
    for i in range(n - 1, -1, -1): o[i] *= r; r *= X[i]
    return o
for X in [[1, 2, 3, 4], [2, 5, 7], [3, 0, 4, 2], [0, 0, 5], [-1, 2, -3, 4]]:
    o = ot(X); w = 1
    for x in X: w *= x
    ck = "has zero" if 0 in X else "matches division" if all(w % x == 0 for x in o) else "?"
    print(f"[{' '.join(map(str, X))}] -> [{' '.join(map(str, o))}] ({ck})")
