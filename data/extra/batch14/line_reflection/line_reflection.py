import math
def mirror(deg):
    a = 2.0 * deg * 3.141592653589793 / 180.0
    return [math.cos(a), math.sin(a), math.sin(a), -math.cos(a)]
def mul(a, b):
    return [a[0] * b[0] + a[1] * b[2], a[0] * b[1] + a[1] * b[3], a[2] * b[0] + a[3] * b[2], a[2] * b[1] + a[3] * b[3]]
def tidy(v):
    return 0.0 if abs(v) < 0.0005 else v
def show_pt(m, x, y):
    return f"({tidy(m[0] * x + m[1] * y):.3f}, {tidy(m[2] * x + m[3] * y):.3f})"
for deg in [0.0, 45.0, 90.0, 30.0]:
    m = mirror(deg)
    det = m[0] * m[3] - m[1] * m[2]
    print(f"mirror at {deg} deg: (3, 1) -> {show_pt(m, 3.0, 1.0)}, det {det:.3f}")
both = mul(mirror(45.0), mirror(30.0))
turn = math.atan2(both[2], both[0]) * 180.0 / 3.141592653589793
print(f"mirror at 30 then 45: rotation by {turn:.3f} deg, (3, 1) -> {show_pt(both, 3.0, 1.0)}")
other = mul(mirror(30.0), mirror(45.0))
back = math.atan2(other[2], other[0]) * 180.0 / 3.141592653589793
print(f"mirror at 45 then 30: rotation by {back:.3f} deg")
twice = mul(mirror(30.0), mirror(30.0))
print(f"same mirror twice: (3, 1) -> {show_pt(twice, 3.0, 1.0)}")
