def f(x, y):
    return (x - 3.0) * (x - 3.0) + 10.0 * (y + 1.0) * (y + 1.0)
for s in [0.01, 0.05, 0.09, 0.11]:
    x = y = 0.0
    marks = []
    for k in range(1, 31):
        gx = 2.0 * (x - 3.0)
        gy = 20.0 * (y + 1.0)
        x -= s * gx
        y -= s * gy
        if k % 10 == 0:
            marks.append(f"{f(x, y):.4f}")
    print(f"step {s}: f after 10, 20, 30 steps = {', '.join(marks)}; now at ({x:.3f}, {y:.3f})")
print("the minimum is f(3, -1) = 0")
