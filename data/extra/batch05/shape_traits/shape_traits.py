import math
S = [("circle", math.pi * 2.25, 2 * math.pi * 1.5), ("square", 6.25, 10.0), ("triangle", 6.0, 12.0), ("circle", math.pi * 0.64, 2 * math.pi * 0.8), ("triangle", 12.0, 16.0)]
for n, a, p in sorted(S, key=lambda s: s[1]): print(f"{n:<8} area {a:>6.2f} perimeter {p:>6.2f}")
print(f"total area {sum(s[1] for s in S):.2f}")
