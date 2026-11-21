cost = lambda p, d, c: (p - c) * 450 + (d - c) * 300 + c * 650
for p, d in [(1, 1), (3, 2), (0, 4), (5, 5), (2, 6)]:
    pick, low = 0, cost(p, d, 0)
    for c in range(1, min(p, d) + 1):
        if cost(p, d, c) < low: low = cost(p, d, c); pick = c
    print(f"{p} popcorn, {d} drinks: {pick} combos, {low // 100}.{low % 100:02d} (saves {cost(p, d, 0) - low}c)")
