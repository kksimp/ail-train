def fl(p):
    f = [0] * len(p); k = 0
    for i in range(1, len(p)):
        while k > 0 and p[i] != p[k]: k = f[k - 1]
        if p[i] == p[k]: k += 1
        f[i] = k
    return f
for t, p in [("abababcabababcab", "ababc"), ("aaaaaaaaab", "aaab"), ("the cat sat on the mat", "at"), ("mississippi", "issip"), ("abc", "d")]:
    f = fl(p); H = []; k = 0; c = 0
    for i in range(len(t)):
        while k > 0 and t[i] != p[k]: c += 1; k = f[k - 1]
        c += 1
        if t[i] == p[k]: k += 1
        if k == len(p): H.append(i + 1 - k); k = f[k - 1]
    print(f"{p} in {t}: table {''.join(map(str, f))}, at {', '.join(map(str, H)) if H else 'none'}, {c} comparisons")
