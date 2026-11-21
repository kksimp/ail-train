import math
def tension(s, scale):
    w = 2.0 * scale * s[1]
    return s[2] * w * w
def pitch(t, mu, scale):
    return math.sqrt(t / mu) / (2.0 * scale)
scale = 0.648
strings = [("E2", 82.41, 0.0062), ("A2", 110.0, 0.0038), ("D3", 146.83, 0.0022), ("G3", 196.0, 0.00118), ("B3", 246.94, 0.00058), ("E4", 329.63, 0.0004)]
total = 0.0
for s in strings:
    t = tension(s, scale)
    total += t
    kgf = t / 9.80665
    print(f"{s[0]} {s[1]:>7.2f} Hz: {t:>6.1f} N ({kgf:.1f} kgf)")
print(f"neck load {total:.0f} N")
slack = tension(strings[0], scale) * 0.9
f = pitch(slack, strings[0][2], scale)
print(f"E2 at 90% tension sounds at {f:.2f} Hz")
