def ex(a, b): return 1.0 / (1.0 + 10.0 ** ((b - a) / 400.0))
R = {"Ana": 1500.0, "Bo": 1500.0, "Cy": 1620.0, "Di": 1380.0}
for a, b, s in [("Ana", "Bo", 1.0), ("Cy", "Di", 0.0), ("Ana", "Cy", 0.5), ("Bo", "Di", 1.0), ("Di", "Ana", 0.0), ("Cy", "Bo", 1.0)]:
    e = ex(R[a], R[b]); d = 32.0 * (s - e); R[a] += d; R[b] -= d; print(f"{a} v {b} ({s:.1f}): expected {e:.3f}, {a} {d:+.2f}")
for n in sorted(R, key=lambda k: (-R[k], k)): print(f"{n:<4} {R[n]:.1f}")
