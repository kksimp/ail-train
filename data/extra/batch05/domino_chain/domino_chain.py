def ex(T, u, e, ch):
    if len(ch) == len(T): return ch
    for i, t in enumerate(T):
        if u[i]: continue
        u2 = u[:]; u2[i] = True
        if t[0] == e:
            r = ex(T, u2, t[1], ch + [t])
            if r: return r
        if t[1] == e and t[0] != t[1]:
            r = ex(T, u2, t[0], ch + [(t[1], t[0])])
            if r: return r
    return None
for T in [[(1, 2), (2, 3), (3, 1), (1, 4), (4, 4)], [(5, 6), (6, 2), (2, 2), (2, 5)], [(1, 2), (3, 4)]]:
    f = False
    for s in range(len(T)):
        u = [False] * len(T); u[s] = True; c = ex(T, u, T[s][1], [T[s]])
        if c: print("".join(f"[{a}|{b}]" for a, b in c)); f = True; break
    if not f: print("no chain")
