import math
tau = 10000.0 * 0.0001; print(f"time constant {tau:.1f} s")
for k in [0.5, 1.0, 2.0, 3.0, 4.0, 5.0]:
    t = k * tau; v = 9.0 * (1.0 - math.exp(-t / tau)); print(f"t = {t:.1f} s: {v:.3f} V ({v / 9.0 * 100.0:.1f}%)")
print(f"reaches {5.0:.1f} V after {-tau * math.log(1.0 - 5.0 / 9.0):.3f} s")
