def sh(D, G):
    X = D[:]; m = 0
    for g in G:
        for i in range(g, len(X)):
            v = X[i]; j = i
            while j >= g and X[j - g] > v: X[j] = X[j - g]; j -= g; m += 1
            X[j] = v
    return X, m
D = [62, 83, 18, 53, 7, 17, 95, 86, 47, 69, 25, 28, 3, 74, 41, 99, 12, 58, 36, 90]; H = []; g = len(D) // 2
while g > 0: H.append(g); g //= 2
for n, G in [("halving", H), ("Knuth", [13, 4, 1])]:
    r = sh(D, G); print(f"{n} gaps {','.join(map(str, G))}: {r[1]} moves, sorted {'true' if r[0] == sorted(D) else 'false'}")
