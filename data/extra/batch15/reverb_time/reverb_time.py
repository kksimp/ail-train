def absorption(parts):
    acc = 0.0
    for s in parts:
        acc = acc + s[1] * s[2]
    return acc
def rt60(v, parts):
    return 0.161 * v / absorption(parts)
volume = 9.0 * 7.0 * 3.0
parts = [("floor", 63.0, 0.03), ("ceiling", 63.0, 0.05), ("walls", 96.0, 0.04), ("windows", 12.0, 0.18)]
print(f"room volume {volume:.0f} m3")
for p in parts:
    a = p[1] * p[2]
    print(f"{p[0]:<8} {p[1]:>5.1f} m2 x {p[2]:.2f} = {a:.3f} sabins")
panels = 0
t = rt60(volume, parts)
print(f"bare room: RT60 {t:.2f} s")
while t > 0.8:
    parts.append(("panel", 2.4, 0.9))
    panels += 1
    t = rt60(volume, parts)
    if panels % 4 == 0:
        print(f"{panels:>2} panels: RT60 {t:.2f} s")
total = absorption(parts)
print(f"{panels} panels reach RT60 {t:.2f} s with {total:.2f} sabins")
