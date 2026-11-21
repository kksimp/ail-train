F = {"mm": 0.001, "cm": 0.01, "m": 1.0, "km": 1000.0, "in": 0.0254, "ft": 0.3048, "mi": 1609.344}
for v, f, t in [(5.0, "km", "mi"), (12.0, "in", "cm"), (6.0, "ft", "m"), (1.0, "mi", "ft"), (3.0, "yd", "m"), (250.0, "mm", "in")]:
    if f in F and t in F: print(f"{v} {f} = {v * F[f] / F[t]:.3f} {t}")
    else: print(f"{v} {f}: cannot convert to {t}")
