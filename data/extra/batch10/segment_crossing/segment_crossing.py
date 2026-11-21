from math import gcd as mgcd

def turn(ax, ay, bx, by, cx, cy):
    v = (bx - ax) * (cy - ay) - (by - ay) * (cx - ax)
    return "L" if v > 0 else ("R" if v < 0 else "S")

def on_segment(ax, ay, bx, by, px, py):
    return min(ax, bx) <= px <= max(ax, bx) and min(ay, by) <= py <= max(ay, by)

def frac(n, d):
    g = mgcd(n, d)
    sn = -n // g if d < 0 else n // g
    sd = -d // g if d < 0 else d // g
    return f"{sn}" if sd == 1 else f"{sn}/{sd}"

def classify(s):
    d1 = turn(s[4], s[5], s[6], s[7], s[0], s[1])
    d2 = turn(s[4], s[5], s[6], s[7], s[2], s[3])
    d3 = turn(s[0], s[1], s[2], s[3], s[4], s[5])
    d4 = turn(s[0], s[1], s[2], s[3], s[6], s[7])
    if d1 != d2 and d3 != d4 and "S" not in (d1, d2, d3, d4):
        rx, ry = s[2] - s[0], s[3] - s[1]
        qx, qy = s[6] - s[4], s[7] - s[5]
        den = rx * qy - ry * qx
        tn = (s[4] - s[0]) * qy - (s[5] - s[1]) * qx
        return f"cross at ({frac(s[0] * den + tn * rx, den)}, {frac(s[1] * den + tn * ry, den)})"
    if d1 == "S" and d2 == "S":
        if on_segment(s[0], s[1], s[2], s[3], s[4], s[5]) or on_segment(s[0], s[1], s[2], s[3], s[6], s[7]) or on_segment(s[4], s[5], s[6], s[7], s[0], s[1]):
            return "overlap on one line"
        return "same line, apart"
    if (d1 == "S" and on_segment(s[4], s[5], s[6], s[7], s[0], s[1])) or (d2 == "S" and on_segment(s[4], s[5], s[6], s[7], s[2], s[3])) or (d3 == "S" and on_segment(s[0], s[1], s[2], s[3], s[4], s[5])) or (d4 == "S" and on_segment(s[0], s[1], s[2], s[3], s[6], s[7])):
        return "touch at an end"
    return "no contact"

cases = [[0, 0, 4, 4, 0, 4, 4, 0], [0, 0, 5, 1, 1, 3, 4, -2], [0, 0, 2, 2, 2, 2, 5, 0], [0, 0, 4, 0, 2, 0, 6, 0], [0, 0, 1, 0, 2, 0, 3, 0], [0, 0, 3, 3, 4, 0, 5, 2], [1, 1, 7, 2, 3, 0, 3, 5]]
for s in cases:
    print(f"({s[0]},{s[1]})-({s[2]},{s[3]}) with ({s[4]},{s[5]})-({s[6]},{s[7]}): {classify(s)}")
