import math
def rs(x, y):
    r = math.floor(math.sqrt(x * x + y * y) / 6.1); return 0 if r >= 10 else 10 - r
t = 0
for i, E in enumerate([[(1.2, -2.0), (5.5, 3.1), (-8.0, 4.4)], [(0.4, 0.9), (-12.5, 7.0), (20.0, -15.0)], [(2.2, 2.2), (-3.0, -4.5), (61.5, 0.0)], [(6.0, 0.5), (0.0, -6.2), (-0.8, 1.1)]]):
    S = sorted((rs(a, b) for a, b in E), reverse=True); et = sum(S); t += et
    print(f"end {i + 1}: {' '.join('M' if s == 0 else str(s) for s in S)} = {et}, running {t}")
