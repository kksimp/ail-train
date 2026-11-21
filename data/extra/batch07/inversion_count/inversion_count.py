def sc(X):
    if len(X) <= 1: return X, 0
    m = len(X) // 2; L, a = sc(X[:m]); R, b = sc(X[m:]); o = []; i = j = 0; c = a + b
    while i < len(L) and j < len(R):
        if L[i] <= R[j]: o.append(L[i]); i += 1
        else: o.append(R[j]); c += len(L) - i; j += 1
    return o + L[i:] + R[j:], c
def br(X): return sum(1 for i in range(len(X)) for j in range(i + 1, len(X)) if X[i] > X[j])
for X in [[2, 4, 1, 3, 5], [5, 4, 3, 2, 1], [1, 2, 3, 4, 5], [3, 1, 2, 5, 4, 8, 6, 7], [9, 1, 8, 2, 7, 3, 6, 4, 5]]:
    r = sc(X); n = len(X); print(f"[{' '.join(map(str, X))}]: {r[1]} inversions of {n * (n - 1) // 2} pairs, brute force agrees {'true' if r[1] == br(X) else 'false'}")
