def pl(H, R, how):
    F = H[:]; L = []; X = []
    for r in R:
        pk = -1
        for i, h in enumerate(F):
            if h < r: continue
            if pk < 0 or (how == "best" and h < F[pk]) or (how == "worst" and h > F[pk]): pk = i
            if how == "first": break
        if pk < 0: X.append(r)
        else: L.append(f"{r}->{pk + 1}"); F[pk] -= r
    return L, X
for how in ["first", "best", "worst"]:
    L, X = pl([100, 500, 200, 300, 600], [212, 417, 112, 426], how)
    print(f"{how:<5} fit: {' '.join(L)}; unplaced {', '.join(map(str, X)) if X else 'none'}")
