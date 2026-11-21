import math
for ap, fo in [(80.0, 920.0), (200.0, 1000.0)]:
    grasp = ap * ap / 49.0
    print(f"{ap:.0f} mm f/{fo / ap:.1f}: Dawes {116.0 / ap:.2f} arcsec, grasp {grasp:.0f}x eye, magnitude {2.0 + 5.0 * math.log10(ap):.1f}")
    fits = []
    for e in [32.0, 25.0, 10.0, 6.0, 4.0]:
        p = fo / e
        if p <= 2.0 * ap:
            fits.append(f"{p:.0f}x")
        else:
            fits.append(f"({p:.0f}x too high)")
    print(f"  eyepieces: {' '.join(fits)}")
