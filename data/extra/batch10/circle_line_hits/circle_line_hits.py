import math

def hits(c, px, py, dx, dy):
    fx = px - c[0]
    fy = py - c[1]
    a = dx * dx + dy * dy
    b = 2.0 * (fx * dx + fy * dy)
    k = fx * fx + fy * fy - c[2] * c[2]
    disc = b * b - 4.0 * a * k
    if disc < 0.0:
        return []
    if disc == 0.0:
        t = -b / (2.0 * a)
        return [[px + t * dx, py + t * dy]]
    s = math.sqrt(disc)
    return [[px + t * dx, py + t * dy] for t in [(-b - s) / (2.0 * a), (-b + s) / (2.0 * a)]]

c = (2.0, 1.0, 5.0)
lines = [[-6.0, 1.0, 1.0, 0.0], [-3.0, 6.0, 1.0, 0.0], [-4.0, 9.0, 1.0, 0.0], [0.0, -7.0, 1.0, 2.0], [7.0, -3.0, -1.0, 3.0]]
for l in lines:
    pts = hits(c, l[0], l[1], l[2], l[3])
    start = f"through ({l[0]}, {l[1]}) along ({l[2]}, {l[3]})"
    if len(pts) == 0:
        print(f"{start}: misses")
    elif len(pts) == 1:
        print(f"{start}: tangent at ({pts[0][0]:.3f}, {pts[0][1]:.3f})")
    else:
        chord = math.sqrt((pts[1][0] - pts[0][0]) * (pts[1][0] - pts[0][0]) + (pts[1][1] - pts[0][1]) * (pts[1][1] - pts[0][1]))
        print(f"{start}: ({pts[0][0]:.3f}, {pts[0][1]:.3f}) and ({pts[1][0]:.3f}, {pts[1][1]:.3f}), chord {chord:.3f}")
