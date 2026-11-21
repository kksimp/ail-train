x = [0.5, 1.3, 2.1, 3.7, 4.4, 5.6]
v = [1.0, -0.8, 1.3, -1.1, 0.6, -1.5]
wall = 8.0; u = -0.02; dt = 0.01
for window in range(6):
    hits = 0
    for step in range(2000):
        wall += u * dt
        for i in range(6):
            x[i] += v[i] * dt
            if x[i] < 0.0:
                x[i] = -x[i]; v[i] = -v[i]
            if x[i] > wall:
                x[i] = 2.0 * wall - x[i]; v[i] = 2.0 * u - v[i]; hits += 1
    speed = 0.0
    for s in v: speed += abs(s)
    speed = speed / 6.0
    print(f"t {(window + 1) * 20:>3} s: piston at {wall:.2f} m, {hits:>3} piston hits, mean speed {speed:.3f}")
