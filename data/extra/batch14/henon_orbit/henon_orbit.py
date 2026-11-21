x = y = 0.0
for i in range(1, 6):
    nx = 1.0 - 1.4 * x * x + y
    y = 0.3 * x
    x = nx
    print(f"step {i}: ({x:.4f}, {y:.4f})")
lo_x, hi_x, lo_y, hi_y = 10.0, -10.0, 10.0, -10.0
for i in range(5000):
    nx = 1.0 - 1.4 * x * x + y
    y = 0.3 * x
    x = nx
    lo_x, hi_x, lo_y, hi_y = min(lo_x, x), max(hi_x, x), min(lo_y, y), max(hi_y, y)
print(f"after 5000 more steps the orbit stayed in x {lo_x:.2f}..{hi_x:.2f}, y {lo_y:.2f}..{hi_y:.2f}")
ax, ay, bx, by = 0.5, 0.1, 0.500000001, 0.1
apart = -1
for i in range(1, 201):
    nax = 1.0 - 1.4 * ax * ax + ay
    ay = 0.3 * ax
    ax = nax
    nbx = 1.0 - 1.4 * bx * bx + by
    by = 0.3 * bx
    bx = nbx
    if apart < 0 and abs(ax - bx) > 0.5:
        apart = i
print(f"starts 0.5 and 0.500000001 differ by more than 0.5 after {apart} steps")
