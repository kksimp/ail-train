def net_forces(xs):
    pts = [0.0] + xs + [10.0]
    out = []
    for i in range(1, len(pts) - 1):
        f = 0.0
        for j in range(len(pts)):
            if j != i:
                d = pts[i] - pts[j]
                if d > 0.0: f += 1.0 / (d * d)
                else: f -= 1.0 / (d * d)
        out.append(f)
    return out
def limit(m):
    if m > 0.2: return 0.2
    if m < -0.2: return -0.2
    return m
xs = [0.8, 1.6, 2.4, 3.2, 4.0]
for step in range(1, 401):
    f = net_forces(xs)
    for i in range(5): xs[i] += limit(0.5 * f[i])
    if step == 1 or step == 10 or step == 50 or step % 200 == 0:
        print(f"step {step:>3}: {' '.join(f'{v:.3f}' for v in xs)}")
gaps = [xs[0], xs[1] - xs[0], xs[2] - xs[1], xs[3] - xs[2], xs[4] - xs[3], 10.0 - xs[4]]
print(f"gaps {' '.join(f'{g:.3f}' for g in gaps)}")
