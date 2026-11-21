def payoffs(x):
    hawk = x * (4.0 - 6.0) / 2.0 + (1.0 - x) * 4.0
    dove = x * 0.0 + (1.0 - x) * 2.0
    return [hawk, dove]
for start in [0.05, 0.5, 0.95]:
    x = start
    trail = []
    for step in range(201):
        if step % 40 == 0:
            trail.append(f"{x:.4f}")
        p = payoffs(x)
        x = x + 0.1 * x * (1.0 - x) * (p[0] - p[1])
    print(f"start {start}: {' -> '.join(trail)}")
p = payoffs(2.0 / 3.0)
print(f"at 2/3 hawks: hawk earns {p[0]:.4f}, dove earns {p[1]:.4f}, so nobody gains by switching")
