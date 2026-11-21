import math
T = 0
for n, w, l, h, d, wi in [("kitchen", 3.2, 4.1, 2.4, 1, 1), ("bedroom", 3.8, 3.6, 2.5, 1, 2), ("hall", 1.2, 5.6, 2.4, 3, 0), ("lounge", 5.1, 4.4, 2.6, 2, 3)]:
    a = 2.0 * (w + l) * h - (d * 1.9 + wi * 1.4); li = a * 2.0 / 10.0; k = math.ceil(li / 2.5); T += k
    print(f"{n:<8} {a:>6.2f} m2, {li:>5.2f} l, {k} tin(s)")
print(f"{T} tins in all")
