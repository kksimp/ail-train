def sound_speed(c): return 331.3 + 0.606 * c
def harmonic(kind, length, n, v):
    if kind == "Open":
        return float(n) * v / (2.0 * length)
    return float(2 * n - 1) * v / (4.0 * length)
v = sound_speed(20.0)
print(f"speed of sound at 20 C: {v:.2f} m/s")
for kind, length in [("Open", 2.44), ("Stopped", 1.22)]:
    parts = []
    for n in range(1, 5):
        f = harmonic(kind, length, n, v)
        parts.append(f"{f:.1f}")
    print(f"PipeKind.{kind} {length:.2f} m: {', '.join(parts)} Hz")
for t in [10.0, 20.0, 30.0]:
    f = harmonic("Open", 2.44, 1, sound_speed(t))
    print(f"open 2.44 m pipe at {t:.0f} C: {f:.2f} Hz")
