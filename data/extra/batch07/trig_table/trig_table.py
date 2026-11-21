import math
print("deg     sin     cos      tan")
for d in [0, 15, 30, 45, 60, 75, 90]:
    r = d * 3.141592653589793 / 180.0; s = math.sin(r); c = math.cos(r); t = "inf" if d == 90 else f"{s / c:.4f}"
    print(f"{d:>3} {s:>7.4f} {c:>7.4f} {t:>8} {'true' if abs(s * s + c * c - 1.0) < 0.000000001 else 'false'}")
