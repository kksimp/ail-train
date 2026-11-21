import math
def pe(l, g): return 2.0 * 3.141592653589793 * math.sqrt(l / g)
for l in [0.25, 0.5, 1.0, 2.0, 10.0]: print(f"{l:>5.2f} m: Earth {pe(l, 9.81):.3f} s, Moon {pe(l, 1.62):.3f} s")
pi = 3.141592653589793; print(f"seconds pendulum: {9.81 * (2.0 / (2.0 * pi)) * (2.0 / (2.0 * pi)):.4f} m")
