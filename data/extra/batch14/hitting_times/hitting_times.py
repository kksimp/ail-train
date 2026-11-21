n = 9
target = 8
a = []
for v in range(n):
    row = [0.0] * (n + 1)
    row[v] = 1.0
    if v != target:
        r, c = v // 3, v % 3
        nbrs = []
        if r > 0: nbrs.append(v - 3)
        if r < 2: nbrs.append(v + 3)
        if c > 0: nbrs.append(v - 1)
        if c < 2: nbrs.append(v + 1)
        share = 1.0 / float(len(nbrs))
        for w in nbrs:
            row[w] -= share
        row[n] = 1.0
    a.append(row)
for col in range(n):
    piv = col
    for r in range(col + 1, n):
        if abs(a[r][col]) > abs(a[piv][col]):
            piv = r
    a[col], a[piv] = a[piv], a[col]
    for r in range(n):
        if r != col:
            f = a[r][col] / a[col][col]
            for k in range(col, n + 1):
                a[r][k] -= f * a[col][k]
for r in range(3):
    print("".join(f"{a[r * 3 + c][n] / a[r * 3 + c][r * 3 + c]:>7.2f}" for c in range(3)))
print(f"cheese in the bottom-right room; from the far corner it takes about {a[0][n] / a[0][0]:.1f} minutes")
