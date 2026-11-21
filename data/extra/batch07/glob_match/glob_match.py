def ma(p, s):
    ok = [[False] * (len(s) + 1) for _ in range(len(p) + 1)]; ok[0][0] = True
    for i in range(1, len(p) + 1):
        if p[i - 1] == "*": ok[i][0] = ok[i - 1][0]
    for i in range(1, len(p) + 1):
        for j in range(1, len(s) + 1):
            if p[i - 1] == "*": ok[i][j] = ok[i - 1][j] or ok[i][j - 1]
            elif p[i - 1] == "?" or p[i - 1] == s[j - 1]: ok[i][j] = ok[i - 1][j - 1]
    return ok[len(p)][len(s)]
F = ["report.txt", "report.pdf", "photo1.jpg", "photo12.jpg", "notes", "data.tar.gz", "readme.md"]
for pt in ["*.txt", "photo?.jpg", "photo*.jpg", "*.*.*", "re*", "*", "????s"]:
    h = [f for f in F if ma(pt, f)]; print(f"{pt}: {' '.join(h) if h else 'nothing'}")
