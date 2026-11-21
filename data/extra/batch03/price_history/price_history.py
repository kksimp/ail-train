p = [1040, 1012, 998, 1065, 1101, 1087, 1150, 1020, 1009, 1190, 1175, 1210]
lo = 0; best = (0, 0, 0)
for d in range(1, len(p)):
    if p[d] < p[lo]: lo = d
    elif p[d] - p[lo] > best[2]: best = (lo, d, p[d] - p[lo])
b, s, g = best
print(f"buy day {b + 1} at {p[b]}, sell day {s + 1} at {p[s]}, gain {g}")
dr = [p[i - 1] - p[i] for i in range(1, len(p))]
print(f"largest drop: {max(dr)} on day {dr.index(max(dr)) + 2}")
h = p[0]; hs = []
for d in range(1, len(p)):
    if p[d] > h: h = p[d]; hs.append(d + 1)
print(f"new highs on days {hs}")
