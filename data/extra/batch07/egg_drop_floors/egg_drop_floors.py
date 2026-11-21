def fl(dr, eg):
    t = [0] * (eg + 1)
    for d in range(1, dr + 1):
        n = [0] * (eg + 1)
        for e in range(1, eg + 1): n[e] = t[e - 1] + 1 + t[e]
        t = n
    return t[eg]
for e, b in [(1, 10), (2, 10), (2, 36), (2, 100), (3, 100), (4, 1000)]:
    d = 1
    while fl(d, e) < b: d += 1
    print(f"{e} egg(s), {b} floors: {d} drops (covers {fl(d, e)})")
