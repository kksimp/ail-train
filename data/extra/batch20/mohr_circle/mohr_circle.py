import math
PI = 3.141592653589793

def on_plane(sx, sy, txy, deg):
    a = 2.0 * deg * PI / 180.0
    return (sx + sy) / 2.0 + (sx - sy) / 2.0 * math.cos(a) + txy * math.sin(a)

for name, sx, sy, txy in [("shaft surface", 0.0, 0.0, 50.0), ("bolt in tension", 120.0, 0.0, 0.0), ("bracket weld", 80.0, -40.0, 30.0), ("plate corner", -60.0, -20.0, -25.0)]:
    c = (sx + sy) / 2.0
    h = (sx - sy) / 2.0
    r = math.sqrt(h * h + txy * txy)
    angle = math.atan2(2.0 * txy, sx - sy) * 90.0 / PI
    print(f"{name}: s1 {c + r:.1f} MPa, s2 {c - r:.1f} MPa, max shear {r:.1f} MPa, principal plane {angle:.1f} deg")
    print(f"  normal stress on the 30 deg plane {on_plane(sx, sy, txy, 30.0):.1f} MPa")
