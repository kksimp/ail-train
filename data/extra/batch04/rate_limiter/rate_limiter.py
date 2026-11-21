W = {}; rf = 0
for t, w in [(1, "ann"), (2, "ann"), (3, "bob"), (4, "ann"), (5, "ann"), (9, "bob"), (11, "ann"), (12, "ann"), (13, "ann"), (14, "bob"), (15, "ann"), (25, "ann")]:
    rc = [x for x in W.get(w, []) if x > t - 10]
    if len(rc) >= 3: rf += 1; print(f"t={t:>2} {w}: refused ({len(rc)} in window)"); W[w] = rc; continue
    W[w] = rc + [t]; print(f"t={t:>2} {w}: ok")
print(f"{rf} refused")
