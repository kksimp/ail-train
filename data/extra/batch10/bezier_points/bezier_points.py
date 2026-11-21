import math

def casteljau(xs, t):
    p = xs[:]
    n = len(p)
    while n > 1:
        for i in range(n - 1):
            p[i] = (1.0 - t) * p[i] + t * p[i + 1]
        n -= 1
    return p[0]

def bernstein(xs, t):
    s = 1.0 - t
    return s * s * s * xs[0] + 3.0 * s * s * t * xs[1] + 3.0 * s * t * t * xs[2] + t * t * t * xs[3]

xs = [0.0, 1.0, 4.0, 6.0]
ys = [0.0, 3.0, 4.0, 1.0]
for i in range(6):
    t = float(i) / 5.0
    x = casteljau(xs, t)
    y = casteljau(ys, t)
    same = abs(x - bernstein(xs, t)) < 0.000000001 and abs(y - bernstein(ys, t)) < 0.000000001
    print(f"t {t:.1f}: ({x:.3f}, {y:.3f}) matches Bernstein form: {str(same).lower()}")
for steps in [4, 16, 256]:
    length = 0.0
    px, py = xs[0], ys[0]
    for i in range(1, steps + 1):
        t = float(i) / float(steps)
        x = casteljau(xs, t)
        y = casteljau(ys, t)
        length += math.sqrt((x - px) * (x - px) + (y - py) * (y - py))
        px, py = x, y
    print(f"length with {steps:>3} chords: {length:.5f}")
