def max_depth(fo2, limit):
    return (limit / fo2 - 1.0) * 10.0
def ead(depth, fo2):
    return (depth + 10.0) * (1.0 - fo2) / 0.79 - 10.0
for pct in [21, 28, 32, 36, 40, 50]:
    fo2 = float(pct) / 100.0
    work = max_depth(fo2, 1.4)
    limit = max_depth(fo2, 1.6)
    print(f"EAN{pct}: max {work:>5.2f} m (contingency {limit:>5.2f} m)")
for pct in [32, 36]:
    fo2 = float(pct) / 100.0
    at = 25.0
    if at <= max_depth(fo2, 1.4):
        print(f"EAN{pct} at {at} m feels like air at {ead(at, fo2):.1f} m, ppO2 {fo2 * (1.0 + at / 10.0):.2f} bar")
