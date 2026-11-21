P = [(3, 1200, "P7"), (1, 800, "P2"), (2, 2500, "P9"), (1, 800, "P1"), (3, 300, "P4"), (2, 150, "P5")]
for z, g, i in sorted(P): print(f"zone {z}: {i} ({g} g)")
print(f"heaviest {max(P, key=lambda p: p[1])[2]}")
