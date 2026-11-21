import math
PI = 3.141592653589793
def tidy(v):
    return 0.0 if abs(v) < 0.0005 else v
def holes(n, dia, start):
    r = dia / 2.0
    out = []
    for k in range(n):
        a = (start + 360.0 * float(k) / float(n)) * PI / 180.0
        x = tidy(r * math.cos(a))
        y = tidy(r * math.sin(a))
        out.append(f"({x:.3f}, {y:.3f})")
    return out
for n, dia, start in [(4, 100.0, 45.0), (5, 120.0, 90.0)]:
    half_angle = PI / float(n)
    chord = dia * math.sin(half_angle)
    print(f"{n} holes on {dia} mm from {start} deg, {chord:.3f} mm apart:")
    for h in holes(n, dia, start):
        print(f"  {h}")
