import math
n = 9
x = [float(i) for i in range(n)]; y = [0.0] * n
px = list(x); py = list(y)
dt = 0.02
for step in range(1, 401):
    for i in range(1, n):
        vx = (x[i] - px[i]) * 0.99
        vy = (y[i] - py[i]) * 0.99
        px[i] = x[i]; py[i] = y[i]
        x[i] += vx
        y[i] += vy - 9.8 * dt * dt
    for p in range(10):
        for i in range(n - 1):
            dx = x[i + 1] - x[i]; dy = y[i + 1] - y[i]
            d = math.sqrt(dx * dx + dy * dy)
            fix = (d - 1.0) / d / 2.0
            if i > 0:
                x[i] += dx * fix; y[i] += dy * fix
            x[i + 1] -= dx * fix; y[i + 1] -= dy * fix
    if step % 100 == 0:
        end_depth = 0.0 - y[n - 1]
        print(f"step {step}: rope end at depth {end_depth:.3f} m")
length = 0.0
for i in range(n - 1):
    dx = x[i + 1] - x[i]; dy = y[i + 1] - y[i]
    length += math.sqrt(dx * dx + dy * dy)
print(f"depth of each joint: {' '.join(f'{0.0 - v:.2f}' for v in y[1:])}")
print(f"rope length {length:.3f} m (8 m when every link is exact)")
