import math
PI = 3.141592653589793
K = 8987551792.0

def field(charges, px, py):
    ex = 0.0
    ey = 0.0
    v = 0.0
    for cx, cy, q in charges:
        dx = px - cx
        dy = py - cy
        r2 = dx * dx + dy * dy
        r = math.sqrt(r2)
        e = K * q / r2
        ex += e * dx / r
        ey += e * dy / r
        v += K * q / r
    return [ex, ey, v]

micro = 0.000001
dipole = [(-0.1, 0.0, 2.0 * micro), (0.1, 0.0, -2.0 * micro)]
for px, py in [(0.0, 0.05), (0.05, 0.1), (-0.2, 0.1), (0.3, -0.2), (0.0, 0.4)]:
    f = field(dipole, px, py)
    mag = math.sqrt(f[0] * f[0] + f[1] * f[1]) / 1000.0
    angle = math.atan2(f[1], f[0]) * 180.0 / PI
    volts = f[2] / 1000.0
    print(f"({px:>5.2f}, {py:>5.2f}) m: E {mag:>8.1f} kN/C at {angle:>6.1f} deg, V {volts:>7.2f} kV")
