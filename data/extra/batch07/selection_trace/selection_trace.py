X = [29, 10, 14, 37, 13, 5, 41, 22]; c = s = 0
for i in range(len(X) - 1):
    lo = i
    for j in range(i + 1, len(X)):
        c += 1
        if X[j] < X[lo]: lo = j
    if lo != i: X[i], X[lo] = X[lo], X[i]; s += 1; print(f"pass {i + 1}: {' '.join(map(str, X))}")
print(f"{c} comparisons, {s} swaps")
