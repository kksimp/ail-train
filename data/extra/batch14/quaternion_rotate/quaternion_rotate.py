import math
class Q:
    def __init__(s, w, x, y, z):
        s.w, s.x, s.y, s.z = w, x, y, z
    def __mul__(s, o):
        return Q(s.w * o.w - s.x * o.x - s.y * o.y - s.z * o.z, s.w * o.x + s.x * o.w + s.y * o.z - s.z * o.y, s.w * o.y - s.x * o.z + s.y * o.w + s.z * o.x, s.w * o.z + s.x * o.y - s.y * o.x + s.z * o.w)
    def conj(s):
        return Q(s.w, -s.x, -s.y, -s.z)
def turn(ax, ay, az, deg):
    ln = math.sqrt(ax * ax + ay * ay + az * az)
    half = deg * 3.141592653589793 / 360.0
    s = math.sin(half) / ln
    return Q(math.cos(half), ax * s, ay * s, az * s)
def tidy(v):
    return 0.0 if abs(v) < 0.0005 else v
def show(q):
    return f"({tidy(q.w):.3f}, {tidy(q.x):.3f}, {tidy(q.y):.3f}, {tidy(q.z):.3f})"
def rotate(q, x, y, z):
    r = q * Q(0.0, x, y, z) * q.conj()
    return f"({tidy(r.x):.3f}, {tidy(r.y):.3f}, {tidy(r.z):.3f})"
i = Q(0.0, 1.0, 0.0, 0.0)
j = Q(0.0, 0.0, 1.0, 0.0)
print(f"i j = {show(i * j)}")
print(f"j i = {show(j * i)}")
qz = turn(0.0, 0.0, 1.0, 90.0)
qx = turn(1.0, 0.0, 0.0, 90.0)
print(f"90 deg about z: q = {show(qz)}, x axis goes to {rotate(qz, 1.0, 0.0, 0.0)}")
print(f"z then x: {rotate(qx * qz, 1.0, 0.0, 0.0)}")
print(f"x then z: {rotate(qz * qx, 1.0, 0.0, 0.0)}")
diag = turn(1.0, 1.0, 1.0, 120.0)
print(f"120 deg about (1,1,1): x -> {rotate(diag, 1.0, 0.0, 0.0)}, y -> {rotate(diag, 0.0, 1.0, 0.0)}")
print(f"vector (2, 3, 4) after the z turn: {rotate(qz, 2.0, 3.0, 4.0)}")
