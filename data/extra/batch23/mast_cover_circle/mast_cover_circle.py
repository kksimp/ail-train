import math

class Circle:
    def __init__(self, x, y, r):
        self.x = x
        self.y = y
        self.r = r

    def holds(self, p):
        dx = p[0] - self.x
        dy = p[1] - self.y
        return math.sqrt(dx * dx + dy * dy) <= self.r + 0.000000001

def through_two(a, b):
    dx = a[0] - b[0]
    dy = a[1] - b[1]
    return Circle((a[0] + b[0]) / 2.0, (a[1] + b[1]) / 2.0, math.sqrt(dx * dx + dy * dy) / 2.0)

def through_three(a, b, c):
    d = 2.0 * (a[0] * (b[1] - c[1]) + b[0] * (c[1] - a[1]) + c[0] * (a[1] - b[1]))
    sa = a[0] * a[0] + a[1] * a[1]
    sb = b[0] * b[0] + b[1] * b[1]
    sc = c[0] * c[0] + c[1] * c[1]
    ux = (sa * (b[1] - c[1]) + sb * (c[1] - a[1]) + sc * (a[1] - b[1])) / d
    uy = (sa * (c[0] - b[0]) + sb * (a[0] - c[0]) + sc * (b[0] - a[0])) / d
    dx = a[0] - ux
    dy = a[1] - uy
    return Circle(ux, uy, math.sqrt(dx * dx + dy * dy))

def enclose(points, seed):
    ps = [[float(p[0]), float(p[1])] for p in points]
    s = seed
    i = len(ps) - 1
    while i > 0:
        s = (s * 1103515245 + 12345) % 2147483648
        j = s // 65536 % (i + 1)
        ps[i], ps[j] = ps[j], ps[i]
        i -= 1
    c = Circle(ps[0][0], ps[0][1], 0.0)
    for a in range(1, len(ps)):
        if not c.holds(ps[a]):
            c = Circle(ps[a][0], ps[a][1], 0.0)
            for b in range(a):
                if not c.holds(ps[b]):
                    c = through_two(ps[a], ps[b])
                    for k in range(b):
                        if not c.holds(ps[k]):
                            c = through_three(ps[a], ps[b], ps[k])
    return c

houses = [[2, 3], [9, 1], [5, 8], [12, 6], [7, 4], [3, 9], [10, 10], [6, 0], [1, 6]]
for seed in [1, 7, 42]:
    c = enclose(houses, seed)
    print(f"seed {seed:>2}: mast at ({c.x:.3f}, {c.y:.3f}), range {c.r:.3f}")
tri = enclose([[0, 0], [6, 0], [0, 8]], 3)
print(f"right triangle 6-8-10: range {tri.r}, centre ({tri.x}, {tri.y})")
