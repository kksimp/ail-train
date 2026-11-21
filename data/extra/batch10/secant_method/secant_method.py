import math

def kepler(e, m, big):
    return big - e * math.sin(big) - m

def secant(e, m):
    a = m
    b = m + 0.1
    steps = 0
    while steps < 100:
        fa = kepler(e, m, a)
        fb = kepler(e, m, b)
        if fb == fa:
            break
        c = b - fb * (b - a) / (fb - fa)
        a = b
        b = c
        steps += 1
        if abs(b - a) < 0.000000000001:
            break
    return [b, float(steps)]

pi = 3.141592653589793
for e in [0.0167, 0.2056, 0.6, 0.9]:
    cells = []
    for deg in [30.0, 90.0, 150.0]:
        m = deg * pi / 180.0
        r = secant(e, m)
        ea = r[0] * 180.0 / pi
        cells.append(f"M {deg:.0f}: E {ea:>8.4f} ({int(r[1])} steps)")
    print(f"e {e:.4f}: {', '.join(cells)}")
