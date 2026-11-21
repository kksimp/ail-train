import math
PI = 3.141592653589793

def asin(x):
    return math.atan(x / math.sqrt(1.0 - x * x))

def index(nm):
    return 1.5046 + 4200.0 / (nm * nm)

def deviation(n, apex):
    half = apex * PI / 360.0
    return (2.0 * asin(n * math.sin(half)) - 2.0 * half) * 180.0 / PI

devs = []
for nm in [400, 450, 500, 550, 600, 650, 700]:
    n = index(float(nm))
    d = deviation(n, 60.0)
    devs.append(d)
    print(f"{nm} nm: n = {n:.4f}, deviated {d:.2f} degrees")
fan = devs[0] - devs[-1]
print(f"violet to red fan: {fan:.2f} degrees")
flint = 1.62
print(f"flint glass at n {flint}: {deviation(flint, 60.0):.2f} degrees")
