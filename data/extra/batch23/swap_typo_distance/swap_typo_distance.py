def distance(a, b, swaps):
    xs = list(a)
    ys = list(b)
    n = len(xs)
    m = len(ys)
    d = []
    for i in range(n + 1):
        row = []
        for j in range(m + 1):
            first = j if i == 0 else (i if j == 0 else 0)
            row.append(first)
        d.append(row)
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            cost = 0 if xs[i - 1] == ys[j - 1] else 1
            best = min(min(d[i - 1][j] + 1, d[i][j - 1] + 1), d[i - 1][j - 1] + cost)
            if swaps and i > 1 and j > 1 and xs[i - 1] == ys[j - 2] and xs[i - 2] == ys[j - 1]:
                best = min(best, d[i - 2][j - 2] + 1)
            d[i][j] = best
    return d[n][m]

pairs = [("form", "from"), ("recieve", "receive"), ("teh", "the"), ("acress", "caress"), ("kitten", "sitting"), ("abcdef", "badcfe"), ("ca", "abc")]
saved = 0
for a, b in pairs:
    lev = distance(a, b, False)
    osa = distance(a, b, True)
    saved += lev - osa
    print(f"{a:<8} {b:<8} levenshtein {lev}  with swaps {osa}")
print(f"swaps saved {saved} edits in total")
