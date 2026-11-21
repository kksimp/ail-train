s = 10.0; r = 28.0; b = 8.0 / 3.0; dt = 0.005; a = [1.0, 1.0, 1.0]; c = [1.000000001, 1.0, 1.0]
for step in range(6001):
    if step % 1000 == 0:
        dx = a[0] - c[0]; dy = a[1] - c[1]; dz = a[2] - c[2]; gap = (dx * dx + dy * dy + dz * dz) ** 0.5
        print(f"t {step * dt:>4.1f}: x {a[0]:>7.2f} y {a[1]:>7.2f} z {a[2]:>6.2f}, gap {gap:.6f}")
    a = [a[0] + s * (a[1] - a[0]) * dt, a[1] + (a[0] * (r - a[2]) - a[1]) * dt, a[2] + (a[0] * a[1] - b * a[2]) * dt]
    c = [c[0] + s * (c[1] - c[0]) * dt, c[1] + (c[0] * (r - c[2]) - c[1]) * dt, c[2] + (c[0] * c[1] - b * c[2]) * dt]
