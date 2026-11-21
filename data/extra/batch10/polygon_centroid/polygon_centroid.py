def area(xs, ys):
    s = 0.0
    n = len(xs)
    for i in range(n):
        j = (i + 1) % n
        s += xs[i] * ys[j] - xs[j] * ys[i]
    return s / 2.0

def centroid(xs, ys):
    cx = cy = 0.0
    n = len(xs)
    for i in range(n):
        j = (i + 1) % n
        cross = xs[i] * ys[j] - xs[j] * ys[i]
        cx += (xs[i] + xs[j]) * cross
        cy += (ys[i] + ys[j]) * cross
    a = area(xs, ys)
    return [cx / (6.0 * a), cy / (6.0 * a)]

def total(xs):
    s = 0.0
    for v in xs:
        s += v
    return s

plates = [("L-shape", [0.0, 6.0, 6.0, 2.0, 2.0, 0.0], [0.0, 0.0, 2.0, 2.0, 7.0, 7.0]), ("triangle", [0.0, 9.0, 3.0], [0.0, 0.0, 6.0]), ("kite", [0.0, 4.0, 0.0, -1.0], [0.0, 3.0, 7.0, 3.0]), ("trapezium", [0.0, 10.0, 7.0, 1.0], [0.0, 0.0, 4.0, 4.0])]
for name, xs, ys in plates:
    c = centroid(xs, ys)
    n = float(len(xs))
    ax = total(xs) / n
    ay = total(ys) / n
    print(f"{name:<9} area {area(xs, ys):>5.1f}, centroid ({c[0]:.3f}, {c[1]:.3f}), corner average ({ax:.3f}, {ay:.3f})")
bottom = 12.0
side = 10.0
mx = (bottom * 3.0 + side * 1.0) / (bottom + side)
my = (bottom * 1.0 + side * 4.5) / (bottom + side)
print(f"L-shape as two rectangles: ({mx:.3f}, {my:.3f})")
