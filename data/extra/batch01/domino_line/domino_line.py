def lay(ts):
    pl = []
    for i, (a, b) in enumerate(ts):
        if pl:
            l = pl[-1][1]
            if l == a: pl.append((a, b))
            elif l == b: pl.append((b, a))
            else: return pl, i
        else:
            pl.append((a, b))
    return pl, None
show = lambda ts: "".join(f"[{a}|{b}]" for a, b in ts)
for r in [[(1, 2), (2, 5), (5, 5), (5, 3)], [(4, 1), (6, 1), (6, 2)], [(3, 3), (2, 4)], []]:
    pl, st = lay(r)
    if st is not None:
        print(f"{show(pl)} stuck at tile {st + 1}")
    else:
        print(f"{show(pl)} complete, {sum(a + b for a, b in pl)} pips")
