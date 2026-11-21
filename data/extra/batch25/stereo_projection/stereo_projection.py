import math

def unit(v):
    n = math.sqrt(v[0] * v[0] + v[1] * v[1] + v[2] * v[2])
    return [c / n for c in v]

def project(p):
    if p[2] > 0.999999:
        return None
    d = 1.0 - p[2]
    return [p[0] / d, p[1] / d]

def back(q):
    r2 = q[0] * q[0] + q[1] * q[1]
    return [2.0 * q[0] / (r2 + 1.0), 2.0 * q[1] / (r2 + 1.0), (r2 - 1.0) / (r2 + 1.0)]

places = [("south pole", [0.0, 0.0, -1.0]), ("on equator", [1.0, 0.0, 0.0]), ("southern", [2.0, 1.0, -2.0]), ("northern", [1.0, -1.0, 1.0]), ("high north", [1.0, 2.0, 8.0]), ("north pole", [0.0, 0.0, 5.0])]
for name, raw in places:
    p = unit(raw)
    q = project(p)
    if q is not None:
        r = math.sqrt(q[0] * q[0] + q[1] * q[1])
        b = back(q)
        err = abs(b[0] - p[0]) + abs(b[1] - p[1]) + abs(b[2] - p[2])
        ok = "round trip ok" if err < 0.000000001 else "round trip off"
        print(f"{name:<11} z {p[2]:>6.3f} -> ({q[0]:>6.3f}, {q[1]:>6.3f}) radius {r:>6.3f}, {ok}")
    else:
        print(f"{name:<11} the north pole has no image")
