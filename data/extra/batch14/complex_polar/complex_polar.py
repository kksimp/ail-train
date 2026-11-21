import math
def mul(a, b):
    return (a[0] * b[0] - a[1] * b[1], a[0] * b[1] + a[1] * b[0])
def div(a, b):
    d = b[0] * b[0] + b[1] * b[1]
    return ((a[0] * b[0] + a[1] * b[1]) / d, (a[1] * b[0] - a[0] * b[1]) / d)
def size(a):
    return math.sqrt(a[0] * a[0] + a[1] * a[1])
def angle(a):
    return math.atan2(a[1], a[0]) * 180.0 / 3.141592653589793
def tidy(v):
    return 0.0 if abs(v) < 0.0005 else v
def text(a):
    r, i = tidy(a[0]), tidy(a[1])
    if i < 0.0:
        return f"{r:.3f} - {-i:.3f}i"
    return f"{r:.3f} + {i:.3f}i"
def polar(r, deg):
    a = deg * 3.141592653589793 / 180.0
    return (r * math.cos(a), r * math.sin(a))
z = (3.0, 4.0)
w = (1.0, -2.0)
print(f"z = {text(z)}: length {size(z):.3f}, angle {angle(z):.2f} deg")
print(f"w = {text(w)}: length {size(w):.3f}, angle {angle(w):.2f} deg")
print(f"z + w = {text((z[0] + w[0], z[1] + w[1]))}")
zw = mul(z, w)
print(f"z w = {text(zw)}: length {size(zw):.3f} = {size(z) * size(w):.3f}, angle {angle(zw):.2f} = {angle(z) + angle(w):.2f}")
print(f"z / w = {text(div(z, w))}")
p = (1.0, 0.0)
for k in range(8):
    p = mul(p, (1.0, 1.0))
print(f"(1 + i)^8 = {text(p)}")
print(f"2 at 30 deg times 3 at 60 deg = {text(mul(polar(2.0, 30.0), polar(3.0, 60.0)))}")
