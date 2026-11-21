def mt(g, d, r):
    b = 0; m = 0
    while b < g: b += b * r // 120000; b += d; m += 1
    return m
for g in [100000, 500000, 1000000, 2500000]: print(f"goal {g // 100:>6}: {mt(g, 25000, 0):>3} months without interest, {mt(g, 25000, 480):>3} with 4.8%")
