def transmit(a):
    ten = 10.0
    return 100.0 * ten ** (0.0 - a)
conc = [2.0, 4.0, 6.0, 8.0, 10.0]
absorb = [0.105, 0.212, 0.318, 0.42, 0.528]
top = 0.0
bottom = 0.0
for c, a in zip(conc, absorb):
    top += c * a
    bottom += c * c
slope = top / bottom
print(f"calibration slope {slope:.5f} per mg/L")
for a in [0.05, 0.25, 0.475, 0.615]:
    c = a / slope
    note = " (above the standards, dilute and repeat)" if c > 10.0 else ""
    print(f"A {a:.3f}: {c:.2f} mg/L, {transmit(a):.1f}% light through{note}")
