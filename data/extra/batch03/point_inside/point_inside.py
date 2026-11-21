star = [(0.0, 3.0), (1.0, 1.0), (3.0, 1.0), (1.5, -0.5), (2.0, -3.0), (0.0, -1.5), (-2.0, -3.0), (-1.5, -0.5), (-3.0, 1.0), (-1.0, 1.0)]
def ins(p, poly):
    px, py = p; r = False; j = len(poly) - 1
    for i in range(len(poly)):
        xi, yi = poly[i]; xj, yj = poly[j]
        if (yi > py) != (yj > py):
            if px < (xj - xi) * (py - yi) / (yj - yi) + xi: r = not r
        j = i
    return r
for p in [(0.0, 0.0), (0.0, 2.5), (2.5, 0.8), (2.5, 2.0), (-1.9, -2.7), (0.0, -2.0), (5.0, 0.0)]:
    print(f"{p}: {'inside' if ins(p, star) else 'outside'}")
