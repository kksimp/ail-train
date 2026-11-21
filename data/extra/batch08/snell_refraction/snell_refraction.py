import math
for n, n1, n2 in [("air to water", 1.0, 1.333), ("air to glass", 1.0, 1.5), ("water to air", 1.333, 1.0), ("glass to air", 1.5, 1.0)]:
    parts = []
    for a in [20.0, 40.0, 60.0]:
        s = n1 * math.sin(a * 3.141592653589793 / 180.0) / n2
        if s > 1.0: parts.append(f"{a:.0f} -> reflects")
        else: parts.append(f"{a:.0f} -> {math.atan2(s, math.sqrt(1.0 - s * s)) * 180.0 / 3.141592653589793:.1f}")
    print(f"{n:<13} {', '.join(parts)}")
    if n1 > n2:
        x = n2 / n1; print(f"  critical angle {math.atan2(x, math.sqrt(1.0 - x * x)) * 180.0 / 3.141592653589793:.1f} degrees")
