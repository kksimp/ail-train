def lc(a, b):
    g = [[0] * (len(b) + 1) for _ in range(len(a) + 1)]
    best = ea = eb = 0
    for i in range(1, len(a) + 1):
        for j in range(1, len(b) + 1):
            if a[i - 1] == b[j - 1]:
                g[i][j] = g[i - 1][j - 1] + 1
                if g[i][j] > best: best, ea, eb = g[i][j], i, j
    return a[ea - best:ea], ea - best, eb - best
for x, y in [("photograph", "tomography"), ("abcdef", "zcdemn"), ("same", "same"), ("abc", "xyz"), ("", "abc")]:
    s, i, j = lc(x, y)
    print(f"{x} / {y}: '{s}' at {i} and {j}")
