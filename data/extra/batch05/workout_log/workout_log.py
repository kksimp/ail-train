s = 0.0
for n, S in [("squat", [(5, 100.0), (5, 105.0), (3, 115.0)]), ("bench", [(8, 60.0), (6, 65.0), (4, 70.0)]), ("row", [(10, 50.0), (10, 52.5)])]:
    v = 0.0; b = 0.0
    for r, k in S: v += r * k; b = max(b, k * (1 + r / 30))
    s += v; print(f"{n:<6} {len(S)} sets, volume {v:>7.1f} kg, est 1RM {b:.1f} kg")
print(f"session volume {s:.1f} kg")
