def energy(bodies):
    t = 0.0
    for kg, v in bodies:
        t = t + 0.5 * kg * v * v
    return t
def elastic(a, b):
    total = a[0] + b[0]
    va = ((a[0] - b[0]) * a[1] + 2.0 * b[0] * b[1]) / total
    vb = ((b[0] - a[0]) * b[1] + 2.0 * a[0] * a[1]) / total
    return [(a[0], va), (b[0], vb)]
for name, a, b in [("snooker balls", (0.17, 2.0), (0.17, 0.0)), ("ball hits bowling ball", (0.5, 4.0), (7.0, 0.0)), ("truck meets car", (3000.0, 10.0), (1000.0, -15.0))]:
    after = elastic(a, b)
    shared = (a[0] * a[1] + b[0] * b[1]) / (a[0] + b[0])
    before_e = energy([a, b])
    stuck_e = energy([(a[0] + b[0], shared)])
    lost = (1.0 - stuck_e / before_e) * 100.0
    print(f"{name}: elastic {after[0][1]:.2f} and {after[1][1]:.2f} m/s; stuck together {shared:.2f} m/s, losing {lost:.1f}% of the energy")
