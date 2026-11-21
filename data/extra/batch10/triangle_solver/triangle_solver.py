import math

def rad(d):
    return d * 3.141592653589793 / 180.0

def deg(r):
    return r * 180.0 / 3.141592653589793

def arccos(x):
    return math.atan2(math.sqrt(1.0 - x * x), x)

def solve(g):
    kind = g[0]
    if kind == "sss":
        _, a, b, c = g
        ca = arccos((b * b + c * c - a * a) / (2.0 * b * c))
        cb = arccos((a * a + c * c - b * b) / (2.0 * a * c))
        return [a, b, c, deg(ca), deg(cb), 180.0 - deg(ca) - deg(cb)]
    if kind == "sas":
        _, a, angle_c, b = g
        c = math.sqrt(a * a + b * b - 2.0 * a * b * math.cos(rad(angle_c)))
        ca = arccos((b * b + c * c - a * a) / (2.0 * b * c))
        return [a, b, c, deg(ca), 180.0 - deg(ca) - angle_c, angle_c]
    _, angle_a, c, angle_b = g
    angle_c = 180.0 - angle_a - angle_b
    k = c / math.sin(rad(angle_c))
    return [k * math.sin(rad(angle_a)), k * math.sin(rad(angle_b)), c, angle_a, angle_b, angle_c]

cases = [("sss", 3.0, 4.0, 5.0), ("sss", 7.0, 8.0, 9.0), ("sas", 10.0, 40.0, 7.0), ("asa", 35.0, 12.0, 80.0)]
for g in cases:
    t = solve(g)
    s = (t[0] + t[1] + t[2]) / 2.0
    area = math.sqrt(s * (s - t[0]) * (s - t[1]) * (s - t[2]))
    print(f"sides {t[0]:.3f}, {t[1]:.3f}, {t[2]:.3f}; angles {t[3]:.2f}, {t[4]:.2f}, {t[5]:.2f}; area {area:.3f}")
