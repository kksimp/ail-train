import math
def sa(p):
    n = len(p); return sum(p[i][0] * p[(i + 1) % n][1] - p[(i + 1) % n][0] * p[i][1] for i in range(n)) / 2.0
def pe(p):
    n = len(p); return sum(math.hypot(p[(i + 1) % n][0] - p[i][0], p[(i + 1) % n][1] - p[i][1]) for i in range(n))
for nm, p in [("square", [(0.0, 0.0), (4.0, 0.0), (4.0, 4.0), (0.0, 4.0)]), ("triangle", [(0.0, 0.0), (0.0, 3.0), (4.0, 0.0)]), ("L-shape", [(0.0, 0.0), (6.0, 0.0), (6.0, 2.0), (2.0, 2.0), (2.0, 5.0), (0.0, 5.0)]), ("kite", [(0.0, 0.0), (2.0, 1.5), (0.0, 5.0), (-2.0, 1.5)])]:
    a = sa(p)
    print(f"{nm:<8} area {abs(a):.2f}, perimeter {pe(p):.3f}, {'anticlockwise' if a >= 0 else 'clockwise'}")
