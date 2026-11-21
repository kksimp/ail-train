import math
def pass_through(intensity, angles, i):
    if i >= len(angles):
        return intensity
    pi = 3.141592653589793
    c = math.cos((angles[i] - angles[i - 1]) * pi / 180.0)
    return pass_through(intensity * c * c, angles, i + 1)
def chain(sheets):
    step = 90.0 / float(sheets - 1)
    return [float(k) * step for k in range(sheets)]
print(f"0 and 90 deg: {pass_through(0.5, [0.0, 90.0], 1):.4f}")
print(f"0, 45 and 90 deg: {pass_through(0.5, [0.0, 45.0, 90.0], 1):.4f}")
for n in [3, 4, 5, 7, 11, 21]:
    out = pass_through(0.5, chain(n), 1)
    print(f"{n:>2} sheets from 0 to 90 deg: {out:.4f} of the light")
tilted = pass_through(0.5, [0.0, 30.0], 1)
print(f"two sheets 30 deg apart: {tilted:.4f}")
