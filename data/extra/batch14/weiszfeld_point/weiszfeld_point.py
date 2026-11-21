import math
def cost(x, y, pts):
    t = 0.0
    for p in pts:
        dx, dy = x - p[0], y - p[1]
        t += p[2] * math.sqrt(dx * dx + dy * dy)
    return t
shops = [[0.0, 0.0, 5.0], [10.0, 0.0, 1.0], [10.0, 8.0, 1.0], [2.0, 9.0, 2.0], [9.0, 4.0, 1.0]]
wsum = x = y = 0.0
for p in shops:
    wsum += p[2]
    x += p[2] * p[0]
    y += p[2] * p[1]
x /= wsum
y /= wsum
print(f"weighted centre of mass ({x:.3f}, {y:.3f}): total distance {cost(x, y, shops):.3f}")
for it in range(1, 61):
    nx = ny = den = 0.0
    for p in shops:
        dx, dy = x - p[0], y - p[1]
        d = math.sqrt(dx * dx + dy * dy)
        nx += p[2] * p[0] / d
        ny += p[2] * p[1] / d
        den += p[2] / d
    x, y = nx / den, ny / den
    if it <= 3 or it == 10 or it == 60:
        print(f"step {it}: ({x:.3f}, {y:.3f}), total distance {cost(x, y, shops):.3f}")
