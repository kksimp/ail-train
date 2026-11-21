def payback(outlay, flows, rate):
    left = outlay
    for i, f in enumerate(flows):
        base = 1.0 + rate
        value = f / base ** float(i + 1)
        if value >= left:
            return float(i) + left / value
        left -= value
    return None
def show(x):
    if x is not None:
        return f"{x:.2f} years"
    return "never"
projects = [("solar roof", 12000.0, [1500.0, 1500.0, 1600.0, 1600.0, 1700.0, 1700.0, 1800.0, 1800.0, 1900.0, 1900.0]), ("new oven", 8000.0, [3000.0, 3000.0, 2500.0, 2000.0]), ("delivery van", 30000.0, [9000.0, 9000.0, 8000.0, 4000.0]), ("led lighting", 2000.0, [900.0, 900.0, 900.0])]
for name, outlay, flows in projects:
    simple = show(payback(outlay, flows, 0.0))
    disc = show(payback(outlay, flows, 0.08))
    print(f"{name:<13} outlay {outlay}: payback {simple}, discounted {disc}")
