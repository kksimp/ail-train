import math
def friction(re, rel):
    if re < 2300.0:
        return 64.0 / re
    x = math.log10(rel / 3.7 + 5.74 / math.pow(re, 0.9))
    return 0.25 / (x * x)
pipes = [("copper 15 mm", 0.015, 0.0000015, 20.0), ("steel 50 mm", 0.05, 0.000045, 100.0), ("old iron 50 mm", 0.05, 0.0005, 100.0), ("PVC 100 mm", 0.1, 0.0000015, 500.0)]
nu = 0.000001004
for name, d, rough, length in pipes:
    for v in [0.1, 1.5]:
        re = v * d / nu
        f = friction(re, rough / d)
        h = f * (length / d) * v * v / (2.0 * 9.81)
        kpa = h * 998.0 * 9.81 / 1000.0
        print(f"{name:<15} {v:.1f} m/s: Re {re:>7.0f}, f {f:.4f}, loss {h:>6.3f} m ({kpa:.2f} kPa)")
