def fair(v):
    r = {0}
    for x in v: r |= {s + x for s in r}
    t = sum(v); b = max(s for s in r if s * 2 <= t)
    return b, t - b
for p in [[3, 1, 4, 2, 2], [10, 20, 15, 5, 25], [1, 2, 3, 9], [7], [], [8, 8, 8, 8]]:
    a, b = fair(p)
    print(f"{','.join(map(str, p))}: {a} vs {b}, gap {b - a}")
