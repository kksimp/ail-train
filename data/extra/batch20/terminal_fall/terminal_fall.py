import math

def terminal(m, c):
    return math.sqrt(m * 9.81 / c)

def steps_to(m, c, frac):
    vt = terminal(m, c)
    dt = 0.1
    v = 0.0
    x = 0.0
    n = 0
    while v < frac * vt:
        acc = 9.81 - c * v * v / m
        x += v * dt
        v += acc * dt
        n += 1
    return [float(n) * dt, x]

m = 80.0
for name, area in [("belly to earth", 0.7), ("head down", 0.18), ("canopy open", 25.0)]:
    c = 0.5 * 1.225 * 1.0 * area
    vt = terminal(m, c)
    kmh = vt * 3.6
    r = steps_to(m, c, 0.95)
    print(f"{name:<15} terminal {vt:>6.1f} m/s ({kmh:>5.0f} km/h), 95% after {r[0]:.1f} s and {r[1]:.0f} m")
