def dpmo(defects, units, chances):
    return float(defects) * 1000000.0 / float(units * chances)

def level_for(d):
    for level, limit in [(6, 3.4), (5, 233.0), (4, 6210.0), (3, 66807.0), (2, 308538.0)]:
        if d <= limit:
            return level
    return 1

for name, defects, units, chances in [("invoices", 12, 4000, 5), ("welding", 85, 1200, 8), ("assembly", 3, 25000, 40), ("call centre", 420, 3000, 4), ("shipping", 900, 2000, 3)]:
    d = dpmo(defects, units, chances)
    good = 100.0 - d / 10000.0
    print(f"{name:<11} {d:>9.1f} DPMO, {good:.3f}% right first time, about {level_for(d)} sigma")
