cells = [("AA alkaline", 1.52, 0.1, 1.4, 0.5), ("Li-ion 18650", 4.1, 0.5, 3.95, 3.5), ("car battery", 12.6, 5.0, 10.4, 200.0)]
for name, v1, i1, v2, i2 in cells:
    r = (v1 - v2) / (i2 - i1)
    e = v1 + i1 * r
    short = e / r
    maxp = e * e / (4.0 * r)
    print(f"{name}: EMF {e:.3f} V, r {r * 1000.0:.1f} mohm, short circuit {short:.1f} A, best load power {maxp:.1f} W")
    for load in [10.0, 1.0, 0.1]:
        print(f"  into {load} ohm: {e * load / (load + r):.3f} V")
