def sp(s):
    n = len(s); P = [[False] * n for _ in range(n)]
    for L in range(n):
        for i in range(n - L):
            j = i + L
            if s[i] == s[j] and (L < 2 or P[i + 1][j - 1]): P[i][j] = True
    C = [0] * n; F = [0] * n
    for j in range(n):
        if P[0][j]: C[j] = 0; F[j] = 0; continue
        C[j] = n
        for i in range(1, j + 1):
            if P[i][j] and C[i - 1] + 1 < C[j]: C[j] = C[i - 1] + 1; F[j] = i
    o = []; e = n - 1
    while e >= 0: st = F[e]; o.append(s[st:e + 1]); e = st - 1
    return o[::-1]
for s in ["aab", "racecarannakayak", "banana", "abcde", "noonabbad"]: p = sp(s); print(f"{s}: {len(p) - 1} cut(s), {'|'.join(p)}")
