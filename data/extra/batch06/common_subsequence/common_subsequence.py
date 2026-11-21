def lc(a, b):
    T = [[0] * (len(b) + 1) for _ in range(len(a) + 1)]
    for i in range(1, len(a) + 1):
        for j in range(1, len(b) + 1):
            T[i][j] = T[i - 1][j - 1] + 1 if a[i - 1] == b[j - 1] else T[i - 1][j] if T[i - 1][j] >= T[i][j - 1] else T[i][j - 1]
    o = []; i = len(a); j = len(b)
    while i > 0 and j > 0:
        if a[i - 1] == b[j - 1]: o.append(a[i - 1]); i -= 1; j -= 1
        elif T[i - 1][j] >= T[i][j - 1]: i -= 1
        else: j -= 1
    return "".join(reversed(o))
for x, y in [("ABCBDAB", "BDCABA"), ("AGGTAB", "GXTXAYB"), ("kitten", "sitting"), ("abc", "xyz"), ("dynamic", "programming")]:
    s = lc(x, y); print(f'{x} / {y}: "{s}" ({len(s)})')
