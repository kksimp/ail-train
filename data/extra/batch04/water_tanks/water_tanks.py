def settle(l):
    t = list(l); st = 0
    while True:
        mv = False
        for i in range(len(t) - 1):
            if t[i] - t[i + 1] > 1: t[i] -= 1; t[i + 1] += 1; mv = True
            elif t[i + 1] - t[i] > 1: t[i + 1] -= 1; t[i] += 1; mv = True
        if not mv: break
        st += 1
    return t, st
for s in [[9, 1, 1, 1], [0, 0, 12, 0, 0], [4, 4, 4], [10, 0, 10, 0]]:
    r, st = settle(s); print(f"{s} -> {r} after {st} sweeps, total kept true")
