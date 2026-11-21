def fr(r):
    t = []; i = 0; s = 0
    for _ in range(10):
        if r[i] == 10: s += 10 + r[i + 1] + r[i + 2]; i += 1
        elif r[i] + r[i + 1] == 10: s += 10 + r[i + 2]; i += 2
        else: s += r[i] + r[i + 1]; i += 2
        t.append(s)
    return t
for g in [[10] * 12, [9, 1] * 10 + [9], [10, 7, 3, 9, 0, 10, 0, 8, 8, 2, 0, 6, 10, 10, 10, 8, 1], [3, 4] * 10]:
    t = fr(g); print(" ".join(map(str, t)) + f" => {t[9]}")
