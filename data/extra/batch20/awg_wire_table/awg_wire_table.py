import math
PI = 3.141592653589793

def diameter_mm(g):
    return 0.127 * math.pow(92.0, float(36 - g) / 39.0)

def area_mm2(g):
    d = diameter_mm(g)
    return PI * d * d / 4.0

for g in [0, 4, 10, 12, 14, 18, 22, 26, 30]:
    d = diameter_mm(g)
    a = area_mm2(g)
    ohm = 17.2 / a
    print(f"AWG {g:>2}: {d:>6.3f} mm, {a:>7.3f} mm2, {ohm:>8.2f} ohm/km")
ratio = area_mm2(12) / area_mm2(15)
print(f"3 gauges thinner: area ratio {ratio:.3f}")
drop = 15.0 * 2.0 * 20.0 * 17.2 / area_mm2(14) / 1000.0
print(f"15 A over a 20 m run of AWG 14 (both ways) drops {drop:.2f} V")
