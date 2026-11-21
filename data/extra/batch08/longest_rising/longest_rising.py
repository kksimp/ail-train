def rising(xs):
    n = len(xs); best = []; back = []
    for i in range(n):
        best.append(1); back.append(-1)
        for j in range(i):
            if xs[j] < xs[i] and best[j] + 1 > best[i]: best[i] = best[j] + 1; back[i] = j
    end = 0
    for i in range(n):
        if best[i] > best[end]: end = i
    out = []; k = end
    while k >= 0: out.append(xs[k]); k = back[k]
    return out[::-1]
for w in [[5200, 6100, 4800, 7000, 6500, 8200, 7900, 9100], [9000, 8500, 8000, 7500], [3000, 3500, 3200, 4100, 3900, 4400, 5000, 4700, 5600]]:
    r = rising(w); print(f"{len(r)} rising: {' < '.join(str(x) for x in r)}")
