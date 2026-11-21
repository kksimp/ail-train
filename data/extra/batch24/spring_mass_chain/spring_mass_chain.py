def forces(x):
    k = 10.0
    left = [0.0, x[0], x[1]]
    right = [x[1], x[2], 4.0]
    return [k * (right[i] - x[i] - 1.0) - k * (x[i] - left[i] - 1.0) for i in range(3)]
def energy(x, v):
    k = 10.0
    e = 0.0
    for s in v: e += 0.5 * s * s
    ends = [0.0, x[0], x[1], x[2], 4.0]
    for i in range(4):
        stretch = ends[i + 1] - ends[i] - 1.0
        e += 0.5 * k * stretch * stretch
    return e
x = [1.5, 2.0, 3.0]; v = [0.0, 0.0, 0.0]
e0 = energy(x, v)
dt = 0.01
for step in range(1, 601):
    f = forces(x)
    for i in range(3):
        v[i] += f[i] * dt
        x[i] += v[i] * dt
    if step % 100 == 0:
        print(f"t {step // 100} s: {x[0]:.3f} {x[1]:.3f} {x[2]:.3f}")
e1 = energy(x, v)
print(f"energy {e0:.4f} J at the start, {e1:.4f} J after 6 s")
