mass = [1.0, 1.0, 2.0, 1.0, 1.0]
x = [0.0, 1.0, 1.5, 2.2, 2.6]
v = [2.0, 0.0, 0.0, 0.0, 0.0]
t = 0.0; count = 0
while count < 12:
    soonest = -1.0; pair = -1
    for i in range(4):
        closing = v[i] - v[i + 1]
        if closing > 0.0:
            dt = (x[i + 1] - x[i]) / closing
            if pair < 0 or dt < soonest:
                soonest = dt; pair = i
    if pair < 0: break
    for i in range(5): x[i] += v[i] * soonest
    t += soonest
    a = pair; b = pair + 1
    m1 = mass[a]; m2 = mass[b]; u1 = v[a]; u2 = v[b]
    v[a] = ((m1 - m2) * u1 + 2.0 * m2 * u2) / (m1 + m2)
    v[b] = ((m2 - m1) * u2 + 2.0 * m1 * u1) / (m1 + m2)
    count += 1
    print(f"t {t:.3f} s: balls {a + 1} and {b + 1} collide")
speeds = ", ".join(f"{s:.3f}" for s in v)
print(f"{count} collisions, then no pair is closing; speeds {speeds}")
ke = 0.0
for i in range(5): ke = ke + 0.5 * mass[i] * v[i] * v[i]
print(f"kinetic energy {ke:.4f} J (2.0000 at the start)")
