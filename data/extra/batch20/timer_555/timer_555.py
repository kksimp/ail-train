def high(r1, r2, c):
    return 0.693 * (r1 + r2) * c

def low(r1, r2, c):
    return 0.693 * r2 * c

def hz(r1, r2, c):
    return 1.44 / ((r1 + 2.0 * r2) * c)

def r2_for(f, r1, c):
    return (1.44 / (f * c) - r1) / 2.0

builds = [(1000.0, 68000.0, 0.00001), (10000.0, 10000.0, 0.0000001), (1000.0, 1000.0, 0.00000001), (47000.0, 1000.0, 0.000001)]
for r1, r2, c in builds:
    h = high(r1, r2, c)
    l = low(r1, r2, c)
    duty = h / (h + l) * 100.0
    print(f"R1 {r1 / 1000.0}k R2 {r2 / 1000.0}k C {c * 1000000.0:.2f} uF: {hz(r1, r2, c):.2f} Hz, high {h * 1000.0:.3f} ms, low {l * 1000.0:.3f} ms, duty {duty:.1f}%")
for target in [1.0, 2.0, 440.0]:
    c = 0.0000001 if target > 100.0 else 0.00001
    r2 = r2_for(target, 1000.0, c)
    print(f"for {target} Hz with R1 1k and C {c * 1000000.0:.2f} uF use R2 {r2 / 1000.0:.2f}k")
