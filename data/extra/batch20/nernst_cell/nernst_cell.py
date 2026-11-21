import math
R = 8.314
F = 96485.0

def cell(e0, n, q, t):
    return e0 - R * t / (float(n) * F) * math.log(q)

t = 298.15
e0 = 1.10
for zn, cu in [(1.0, 1.0), (0.01, 1.0), (1.0, 0.01), (0.1, 0.001), (2.0, 0.0001)]:
    e = cell(e0, 2, zn / cu, t)
    dg = -2.0 * F * e / 1000.0
    print(f"[Zn2+] {zn}, [Cu2+] {cu}: E {e:.4f} V, dG {dg:.1f} kJ/mol")
logk = 2.0 * F * e0 / (R * t * 2.302585092994046)
print(f"equilibrium constant K = 10^{logk:.1f}")
conc = cell(0.0, 2, 0.001 / 1.0, t)
print(f"copper concentration cell, 0.001 against 1 mol/L: {conc * 1000.0:.1f} mV")
