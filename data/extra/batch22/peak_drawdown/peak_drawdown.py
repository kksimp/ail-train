values = [100, 104, 108, 103, 97, 92, 95, 101, 109, 112, 105, 99, 96, 100, 106, 113, 115, 110, 107]
eps = []
peak_day = 0
is_open = False
for day in range(1, len(values)):
    v = values[day]
    if v >= values[peak_day]:
        if is_open:
            eps[-1][4] = day
            is_open = False
        peak_day = day
    elif not is_open:
        eps.append([peak_day, values[peak_day], day, v, -1])
        is_open = True
    elif v < eps[-1][3]:
        eps[-1][3] = v
        eps[-1][2] = day
deepest = 0.0
for pd, pk, td, tr, bk in eps:
    depth = float(pk - tr) * 100.0 / float(pk)
    deepest = max(deepest, depth)
    back = "not yet" if bk < 0 else f"day {bk}"
    print(f"peak {pk} on day {pd}, low {tr} on day {td}: -{depth:.2f}%, regained {back}")
print(f"deepest drawdown {deepest:.2f}%")
