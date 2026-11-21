def profit(vals, pa, pb, pab):
    total = 0
    for v in vals:
        best = -1
        gain = 0
        for surplus, margin in [(v[0] + v[1] - pab, pab - 40), (v[0] - pa, pa - 20), (v[1] - pb, pb - 20)]:
            if surplus > best:
                best = surplus
                gain = margin
        if best >= 0:
            total += gain
    return total

vals = [[100, 10], [70, 50], [50, 70], [10, 100]]
singles = [10, 50, 70, 100, 1000]
pairs = [110, 120, 1000]
sep = 0
sep_price = 0
for p in singles:
    got = profit(vals, p, p, 1000)
    if got > sep:
        sep, sep_price = got, p
print(f"separate only: price {sep_price} each, profit {sep}")
pure = 0
for q in pairs:
    pure = max(pure, profit(vals, 1000, 1000, q))
print(f"pair only: profit {pure}")
best = 0
plan = ""
for a in singles:
    for b in singles:
        for q in pairs:
            got = profit(vals, a, b, q)
            if got > best:
                best = got
                plan = f"game {a}, film {b}, pair {q}"
print(f"mixed: {plan}, profit {best}")
