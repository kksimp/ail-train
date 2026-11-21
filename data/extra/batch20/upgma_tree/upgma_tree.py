names = ["human", "chimp", "gorilla", "orangutan", "gibbon"]
d = [[0.0, 1.5, 1.9, 3.3, 4.6], [1.5, 0.0, 2.0, 3.3, 4.7], [1.9, 2.0, 0.0, 3.4, 4.5], [3.3, 3.3, 3.4, 0.0, 4.8], [4.6, 4.7, 4.5, 4.8, 0.0]]
cl = [[n, 1, 0.0] for n in names]
while len(cl) > 1:
    bi, bj = 0, 1
    for i in range(len(cl)):
        for j in range(i + 1, len(cl)):
            if d[i][j] < d[bi][bj]:
                bi, bj = i, j
    h = d[bi][bj] / 2.0
    a = cl[bi]
    b = cl[bj]
    print(f"join {a[0]} and {b[0]} at height {h:.3f}")
    joined = [f"({a[0]},{b[0]})", a[1] + b[1], h]
    row = []
    for k in range(len(cl)):
        if k != bi and k != bj:
            row.append((d[bi][k] * float(a[1]) + d[bj][k] * float(b[1])) / float(a[1] + b[1]))
    nd = []
    ncl = []
    r = 0
    for k in range(len(cl)):
        if k != bi and k != bj:
            line = [d[k][l] for l in range(len(cl)) if l != bi and l != bj]
            line.append(row[r])
            nd.append(line)
            ncl.append(cl[k])
            r += 1
    row.append(0.0)
    nd.append(row)
    ncl.append(joined)
    d = nd
    cl = ncl
print(f"tree: {cl[0][0]};")
