def reynolds(f, v, d): return f[1] * v * d / f[2]
def regime(re):
    if re < 2300.0: return "Laminar"
    if re <= 4000.0: return "Transitional"
    return "Turbulent"
water = ("water", 998.0, 0.001002)
oil = ("engine oil", 870.0, 0.1)
air = ("air", 1.2, 0.0000181)
cases = [(water, 0.02, 0.015), (water, 1.5, 0.015), (water, 0.1, 0.025), (oil, 2.0, 0.05), (oil, 0.6, 0.01), (air, 0.3, 0.1), (air, 5.0, 0.3)]
counts = {}
for f, v, d in cases:
    re = reynolds(f, v, d)
    r = regime(re)
    counts[r] = counts.get(r, 0) + 1
    mm = d * 1000.0
    print(f"{f[0]:<10} {v:>4.2f} m/s in {mm:>3.0f} mm pipe: Re {re:>8.0f} -> Regime.{r}")
for name, n in counts.items():
    print(f"{name}: {n}")
