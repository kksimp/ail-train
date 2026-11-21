import math
def accel(x, y):
    r2 = x * x + y * y
    r3 = r2 * math.sqrt(r2)
    return [-x / r3, -y / r3]
dt = 0.05
ex, ey, evx, evy = 1.0, 0.0, 0.0, 1.0
lx, ly, lvx, lvy = 1.0, 0.0, 0.0, 1.0
for step in range(1, 1001):
    a = accel(ex, ey)
    ex += evx * dt; ey += evy * dt
    evx += a[0] * dt; evy += a[1] * dt
    b = accel(lx, ly)
    lvx += b[0] * dt / 2.0; lvy += b[1] * dt / 2.0
    lx += lvx * dt; ly += lvy * dt
    c = accel(lx, ly)
    lvx += c[0] * dt / 2.0; lvy += c[1] * dt / 2.0
    if step % 200 == 0:
        er = math.sqrt(ex * ex + ey * ey)
        lr = math.sqrt(lx * lx + ly * ly)
        print(f"t {step // 20:>2}: Euler radius {er:.4f}, leapfrog radius {lr:.4f}")
