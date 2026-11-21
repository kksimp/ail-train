import math
def ang(a, b):
    d = a[0] * b[0] + a[1] * b[1]; x = abs(a[0] * b[1] - a[1] * b[0])
    if d == 0.0: return 90.0
    t = math.atan(x / abs(d)) * 180.0 / 3.141592653589793
    return t if d > 0 else 180.0 - t
def turn(a, b):
    x = a[0] * b[1] - a[1] * b[0]
    return "left" if x > 0 else "right" if x < 0 else "straight"
for a, b in [((1.0, 0.0), (0.0, 1.0)), ((1.0, 0.0), (1.0, 1.0)), ((1.0, 1.0), (1.0, -1.0)), ((2.0, 0.0), (-3.0, 0.0)), ((3.0, 4.0), (4.0, 3.0)), ((1.0, 2.0), (2.0, 4.0))]:
    print(f"{a} to {b}: {ang(a, b):.2f} degrees, {turn(a, b)}")
