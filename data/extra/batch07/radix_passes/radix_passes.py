X = [170, 45, 75, 90, 802, 24, 2, 66, 431, 7]; b = max(X); p = 1
while b // p > 0:
    B = [[] for _ in range(10)]
    for x in X: B[(x // p) % 10].append(x)
    X = [x for k in B for x in k]; print(f"by {p}s: {' '.join(map(str, X))}"); p *= 10
print(f"sorted: {'true' if X == sorted(X) else 'false'}")
