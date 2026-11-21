def align(a, b):
    xs = list(a)
    ys = list(b)
    n = len(xs)
    m = len(ys)
    t = [[0] * (m + 1) for _ in range(n + 1)]
    for i in range(n + 1):
        t[i][0] = -2 * i
    for j in range(m + 1):
        t[0][j] = -2 * j
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            s = 1 if xs[i - 1] == ys[j - 1] else -1
            t[i][j] = max(max(t[i - 1][j - 1] + s, t[i - 1][j] - 2), t[i][j - 1] - 2)
    top, mid, bot = [], [], []
    i, j = n, m
    while i > 0 or j > 0:
        diag = 1 if i > 0 and j > 0 and xs[i - 1] == ys[j - 1] else -1
        if i > 0 and j > 0 and t[i][j] == t[i - 1][j - 1] + diag:
            top.append(xs[i - 1]); bot.append(ys[j - 1]); mid.append("|" if diag == 1 else ".")
            i -= 1; j -= 1
        elif i > 0 and t[i][j] == t[i - 1][j] - 2:
            top.append(xs[i - 1]); bot.append("-"); mid.append(" ")
            i -= 1
        else:
            top.append("-"); bot.append(ys[j - 1]); mid.append(" ")
            j -= 1
    return ["".join(reversed(top)), "".join(reversed(mid)), "".join(reversed(bot)), str(t[n][m])]

for a, b in [("GATTACA", "GCATGCT"), ("ACGTTGCA", "ACGTGCA"), ("TTAGGCATC", "TAGGTCATTC")]:
    r = align(a, b)
    print(f"score {r[3]}")
    print(f"  {r[0]}")
    print(f"  {r[1]}")
    print(f"  {r[2]}")
