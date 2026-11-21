def plan(demand, setup, hold):
    n = len(demand)
    best = [0]
    start = [0]
    for t in range(1, n + 1):
        cost = -1
        frm = 0
        for j in range(1, t + 1):
            c = best[j - 1] + setup
            for k in range(j, t + 1):
                c += (k - j) * hold * demand[k - 1]
            if cost < 0 or c < cost:
                cost = c
                frm = j
        best.append(cost)
        start.append(frm)
    lots = [0] * n
    t = n
    while t > 0:
        j = start[t]
        lots[j - 1] = sum(demand[j - 1:t])
        t = j - 1
    return lots + [best[n]]

demand = [60, 100, 10, 200, 120, 15]
out = plan(demand, 150, 1)
n = len(demand)
for i in range(n):
    if out[i] > 0:
        print(f"period {i + 1}: make {out[i]}")
print(f"best cost {out[n]}, against {150 * n} for a batch every period")
