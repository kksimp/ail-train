def flows(face, coupon, years):
    out = []
    for t in range(1, years + 1):
        extra = face if t == years else 0.0
        out.append(face * coupon + extra)
    return out
def price(cfs, y):
    total = 0.0
    for i, cf in enumerate(cfs):
        base = 1.0 + y
        total += cf / base ** float(i + 1)
    return total
def macaulay(cfs, y):
    weighted = 0.0
    for i, cf in enumerate(cfs):
        base = 1.0 + y
        weighted += float(i + 1) * cf / base ** float(i + 1)
    return weighted / price(cfs, y)
y = 0.05
for coupon, years in [(0.05, 2), (0.05, 10), (0.0, 10), (0.08, 30)]:
    cfs = flows(100.0, coupon, years)
    p = price(cfs, y)
    d = macaulay(cfs, y)
    modified = d / (1.0 + y)
    guess = 0.0 - modified
    real = (price(cfs, y + 0.01) - p) / p * 100.0
    print(f"{coupon * 100.0:.1f}% {years:>2}y: price {p:>6.2f}, duration {d:>5.2f}, estimate {guess:.2f}%, actual {real:.2f}%")
