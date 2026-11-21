def sh(d): h = len(d) // 2; return [x for i in range(h) for x in (d[i], d[h + i])]
for n in [2, 4, 8, 10, 12, 20, 52]:
    s = list(range(n)); d = sh(s); c = 1
    while d != s: d = sh(d); c += 1
    print(f"{n} cards: {c} shuffles")
