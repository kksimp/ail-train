import math

def dist(a, b):
    return math.sqrt((a[0] - b[0]) * (a[0] - b[0]) + (a[1] - b[1]) * (a[1] - b[1]))

def circumcentre(a, b, c):
    d = 2.0 * (a[0] * (b[1] - c[1]) + b[0] * (c[1] - a[1]) + c[0] * (a[1] - b[1]))
    a2 = a[0] * a[0] + a[1] * a[1]
    b2 = b[0] * b[0] + b[1] * b[1]
    c2 = c[0] * c[0] + c[1] * c[1]
    return ((a2 * (b[1] - c[1]) + b2 * (c[1] - a[1]) + c2 * (a[1] - b[1])) / d, (a2 * (c[0] - b[0]) + b2 * (a[0] - c[0]) + c2 * (b[0] - a[0])) / d)

def show(p):
    return f"({p[0]:.3f}, {p[1]:.3f})"

tris = [[(0.0, 0.0), (6.0, 0.0), (1.0, 4.0)], [(0.0, 0.0), (4.0, 0.0), (0.0, 3.0)], [(-2.0, 1.0), (5.0, 2.0), (1.0, 7.0)]]
for a, b, c in tris:
    g = ((a[0] + b[0] + c[0]) / 3.0, (a[1] + b[1] + c[1]) / 3.0)
    o = circumcentre(a, b, c)
    h = (3.0 * g[0] - 2.0 * o[0], 3.0 * g[1] - 2.0 * o[1])
    la, lb, lc = dist(b, c), dist(a, c), dist(a, b)
    per = la + lb + lc
    i = ((la * a[0] + lb * b[0] + lc * c[0]) / per, (la * a[1] + lb * b[1] + lc * c[1]) / per)
    print(f"triangle {show(a)} {show(b)} {show(c)}")
    print(f"    centroid {show(g)}, circumcentre {show(o)} radius {dist(o, a):.3f}")
    print(f"    orthocentre {show(h)}, incentre {show(i)}")
    ab = (b[0] - a[0], b[1] - a[1])
    ch = (h[0] - c[0], h[1] - c[1])
    print(f"    CH is perpendicular to AB: {str(abs(ab[0] * ch[0] + ab[1] * ch[1]) < 0.000000001).lower()}")
