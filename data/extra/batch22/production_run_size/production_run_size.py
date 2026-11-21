import math
products = [("bolts", 12000.0, 48000.0, 200.0, 3.0), ("gears", 5000.0, 8000.0, 450.0, 6.0), ("shafts", 2400.0, 30000.0, 300.0, 10.0)]
for name, d, r, s, h in products:
    q = math.sqrt(d * 2.0 * s / (h * (1.0 - d / r)))
    plain = math.sqrt(2.0 * d * s / h)
    peak = q * (1.0 - d / r)
    run_days = q / r * 250.0
    cycle_days = q / d * 250.0
    cost = d / q * s + h * peak / 2.0
    print(f"{name:<6} run {q:.1f} (plain {plain:.1f}), peak {peak:.1f}, makes for {run_days:.1f} of every {cycle_days:.1f} days, cost {cost:.2f} a year")
