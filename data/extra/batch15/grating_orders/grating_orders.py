import math
def angle_deg(s):
    pi = 3.141592653589793
    return math.atan2(s, math.sqrt(1.0 - s * s)) * 180.0 / pi
lasers = [("violet", 405.0), ("green", 532.0), ("red", 650.0)]
for lines in [600, 1200]:
    d = 1000000.0 / float(lines)
    print(f"{lines} lines/mm, spacing {d:.1f} nm")
    for name, wave in lasers:
        top = int(d / wave)
        angles = []
        for m in range(1, top + 1):
            a = angle_deg(float(m) * wave / d)
            angles.append(f"{a:.1f}")
        print(f"  {name:<6} {wave:.0f} nm: {top} orders at {' '.join(angles)} deg")
