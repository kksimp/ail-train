import math
IS = 0.0000000025
NVT = 0.045

def current(v):
    return IS * (math.exp(v / NVT) - 1.0)

def operating(vs, r):
    lo = 0.0
    hi = vs
    for _ in range(60):
        mid = (lo + hi) / 2.0
        if vs - mid - r * current(mid) > 0.0:
            lo = mid
        else:
            hi = mid
    return (lo + hi) / 2.0

for mv in [450, 500, 550, 600, 650, 700]:
    v = float(mv) / 1000.0
    print(f"{mv} mV: {current(v) * 1000.0:>10.4f} mA")
for vs, r in [(5.0, 1000.0), (12.0, 1000.0), (5.0, 220.0), (3.3, 10000.0)]:
    vd = operating(vs, r)
    print(f"{vs} V through {r:.0f} ohm: diode at {vd:.4f} V, {current(vd) * 1000.0:.3f} mA")
