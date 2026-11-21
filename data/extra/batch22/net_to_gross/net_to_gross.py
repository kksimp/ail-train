def net(g):
    social = max(g - 50000, 0) * 8 // 100
    band1 = max(min(g, 400000) - 100000, 0)
    band2 = max(g - 400000, 0)
    tax = band1 * 20 // 100 + band2 * 40 // 100
    return g - social - tax

def gross_for(target):
    lo, hi = target, target * 3
    while lo < hi:
        mid = (lo + hi) // 2
        if net(mid) >= target:
            hi = mid
        else:
            lo = mid + 1
    return lo

def money(c):
    return f"{c // 100}.{c % 100:02d}"

for target in [80000, 250000, 500000, 900000]:
    g = gross_for(target)
    cost = g - net(g)
    pct = cost * 1000 // g
    print(f"net {money(target):>7} needs gross {money(g):>8} (deductions {money(cost)}, {pct // 10}.{pct % 10}%)")
