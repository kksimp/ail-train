import math
PI = 3.141592653589793
G = 9.81

def accel(d, mk):
    a = d * PI / 180.0
    return G * (math.sin(a) - mk * math.cos(a))

def slips(d, ms):
    a = d * PI / 180.0
    return math.tan(a) > ms

surfaces = [("wood on wood", 0.5, 0.3), ("steel on ice", 0.1, 0.05), ("rubber on concrete", 0.9, 0.7)]
for name, ms, mk in surfaces:
    tip = math.atan(ms) * 180.0 / PI
    print(f"{name}: starts sliding above {tip:.1f} degrees")
    for ang in [10, 25, 40]:
        angle = float(ang)
        if slips(angle, ms):
            acc = accel(angle, mk)
            t = math.sqrt(2.0 * 3.0 / acc)
            print(f"  {ang} deg: slides, a = {acc:.2f} m/s2, 3 m in {t:.2f} s")
        else:
            print(f"  {ang} deg: holds")
