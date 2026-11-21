def inside(p, side):
    if side == 0: return p[0] >= 0.0
    if side == 1: return p[0] <= 10.0
    if side == 2: return p[1] >= 0.0
    return p[1] <= 8.0

def cut(a, b, side):
    if side < 2:
        c = 0.0 if side == 0 else 10.0
        t = (c - a[0]) / (b[0] - a[0])
        return (c, a[1] + t * (b[1] - a[1]))
    c = 0.0 if side == 2 else 8.0
    t = (c - a[1]) / (b[1] - a[1])
    return (a[0] + t * (b[0] - a[0]), c)

def clip(poly, side):
    out = []
    for i in range(len(poly)):
        cur = poly[i]
        prev = poly[(i + len(poly) - 1) % len(poly)]
        if inside(cur, side):
            if not inside(prev, side):
                out.append(cut(prev, cur, side))
            out.append(cur)
        elif inside(prev, side):
            out.append(cut(prev, cur, side))
    return out

def area(poly):
    s = 0.0
    for i in range(len(poly)):
        a = poly[i]
        b = poly[(i + 1) % len(poly)]
        s += a[0] * b[1] - b[0] * a[1]
    return abs(s) / 2.0

poly = [(-2.0, 1.0), (5.0, 13.0), (12.0, 3.0), (4.0, -3.0)]
print(f"shape area {area(poly):.2f}")
for side in range(4):
    poly = clip(poly, side)
    print(f"after border {side}: {len(poly)} corners, area {area(poly):.2f}")
for p in poly:
    print(f"  ({p[0]:.2f}, {p[1]:.2f})")
