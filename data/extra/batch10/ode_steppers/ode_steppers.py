import math

def step(method, y, h):
    if method == 0:
        return y + h * y
    if method == 1:
        k1 = y
        k2 = y + h * k1
        return y + h * (k1 + k2) / 2.0
    k1 = y
    k2 = y + h / 2.0 * k1
    k3 = y + h / 2.0 * k2
    k4 = y + h * k3
    return y + h * (k1 + 2.0 * k2 + 2.0 * k3 + k4) / 6.0

def solve(method, n):
    h = 1.0 / float(n)
    y = 1.0
    for _ in range(n):
        y = step(method, y, h)
    return y

e = math.exp(1.0)
names = ["Euler", "Heun", "RK4"]
for m in range(3):
    prev = 0.0
    for n in [10, 20, 40, 80]:
        err = abs(solve(m, n) - e)
        ratio = prev / err if prev > 0.0 else 0.0
        note = f"  error ratio {ratio:.2f}" if prev > 0.0 else ""
        print(f"{names[m]:<5} {n:>2} steps: y(1) = {solve(m, n):.10f}, error {err:.10f}{note}")
        prev = err
print(f"exact e = {e:.10f}")
