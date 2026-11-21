for r in [2.8, 3.2, 3.5, 3.9]:
    x = 0.5
    for k in range(1000): x = r * x * (1.0 - x)
    seen = []
    for k in range(8):
        x = r * x * (1.0 - x); v = f"{x:.3f}"
        if v not in seen: seen.append(v)
    print(f"r {r}: {len(seen)} values: {' '.join(seen)}")
