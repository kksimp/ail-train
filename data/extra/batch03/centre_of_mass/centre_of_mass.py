import math
M = [(1.0, 1.0, 2.0), (4.0, 1.0, 1.0), (2.0, 5.0, 3.0), (6.0, 6.0, 0.5)]
t = sum(m[2] for m in M); cx = sum(m[0] * m[2] for m in M) / t; cy = sum(m[1] * m[2] for m in M) / t
print(f"total mass {t}")
print(f"centre of mass ({cx:.3f}, {cy:.3f})")
print(f"plain centroid ({sum(m[0] for m in M) / 4:.3f}, {sum(m[1] for m in M) / 4:.3f})")
for x, y, w in M: print(f"  mass {w} at ({x}, {y}): {math.hypot(x - cx, y - cy):.3f} away")
