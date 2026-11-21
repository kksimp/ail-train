import math
for n, h, g in [("iodine-131", 8.02, 100.0), ("cobalt-60", 1925.3, 50.0), ("carbon-14", 2092135.0, 10.0)]:
    for d in [1.0, 30.0, 365.0, 3650.0]: print(f"{n} after {d:.0f} days: {g * 0.5 ** (d / h):.4f} g")
    print(f"{n} under 1% after {h * math.log(0.01) / math.log(0.5):.0f} days")
