import math

def nearest(ax, ay, bx, by, h):
    dx = bx - ax
    dy = by - ay
    raw = ((h[1] - ax) * dx + (h[2] - ay) * dy) / (dx * dx + dy * dy)
    t = 0.0 if raw < 0.0 else (1.0 if raw > 1.0 else raw)
    px = ax + t * dx
    py = ay + t * dy
    d = math.sqrt((h[1] - px) * (h[1] - px) + (h[2] - py) * (h[2] - py))
    return [t, px, py, d]

houses = [("mill", 3.0, 7.0), ("farm", 9.0, 1.0), ("chapel", -4.0, 2.0), ("inn", 14.0, 9.0), ("forge", 6.0, 4.0)]
for h in houses:
    r = nearest(0.0, 1.0, 12.0, 6.0, h)
    where = "start of road" if r[0] == 0.0 else ("end of road" if r[0] == 1.0 else "along the road")
    print(f"{h[0]:<7} -> ({r[1]:.3f}, {r[2]:.3f}) {where}, distance {r[3]:.3f}")
closest = min(houses, key=lambda h: int(nearest(0.0, 1.0, 12.0, 6.0, h)[3] * 1000.0))
print(f"closest to the road: {closest[0]}")
