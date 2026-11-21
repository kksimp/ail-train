import math
b = (0.0, 0.0)
for d in [15.0, 30.0, 40.0, 45.0, 50.0, 60.0, 75.0]:
    a = d * 3.141592653589793 / 180.0; vx = 20.0 * math.cos(a); vy = 20.0 * math.sin(a); t = 2.0 * vy / 9.81; pk = vy * vy / (2.0 * 9.81); r = vx * t
    if r > b[1] + 0.000001: b = (d, r)
    print(f"{d:>4.0f} deg: time {t:.2f} s, peak {pk:.2f} m, range {r:.2f} m")
print(f"longest at {b[0]:.0f} deg")
