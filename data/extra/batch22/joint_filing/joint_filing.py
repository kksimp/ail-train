def tax(income, limits):
    rates = [10, 12, 22, 24, 32]
    owed = 0
    lower = 0
    for i in range(4):
        top = limits[i]
        if income > lower:
            owed += (min(income, top) - lower) * rates[i] // 100
        lower = top
    if income > lower:
        owed += (income - lower) * rates[4] // 100
    return owed

single = [11000, 44725, 95375, 182100]
joint = [22000, 89450, 190750, 300000]
for a, b in [(64725, 64725), (120000, 0), (90000, 30000), (200000, 190000)]:
    apart = tax(a, single) + tax(b, single)
    together = tax(a + b, joint)
    diff = apart - together
    verdict = f"bonus {diff}" if diff > 0 else (f"penalty {-diff}" if diff < 0 else "no difference")
    print(f"{a:>6} + {b:>6}: separate {apart:>6}, joint {together:>6}, {verdict}")
