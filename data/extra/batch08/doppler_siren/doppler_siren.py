def heard(f, s, l, closing): return f * (343.0 + l) / (343.0 - s) if closing else f * (343.0 - l) / (343.0 + s)
for k in [30.0, 60.0, 100.0, 140.0]:
    sp = k / 3.6; up = heard(700.0, sp, 0.0, True); dn = heard(700.0, sp, 0.0, False)
    print(f"ambulance at {k:>5.0f} km/h: {up:.1f} Hz coming, {dn:.1f} Hz going, drop {up - dn:.1f} Hz")
print(f"both driving at each other at 90 km/h: {heard(700.0, 25.0, 25.0, True):.1f} Hz")
