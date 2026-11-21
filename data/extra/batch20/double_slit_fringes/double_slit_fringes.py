import math
PI = 3.141592653589793

def intensity(y, lam, l, d):
    c = math.cos(PI * d * y / (lam * l))
    return c * c

lam = 0.000000633
l = 2.0
d = 0.00025
spacing = lam * l / d
print(f"He-Ne laser, slits 0.25 mm apart, screen 2 m away: fringes every {spacing * 1000.0:.2f} mm")
for step in range(9):
    y = float(step) * 0.0007
    i = intensity(y, lam, l, d)
    bar = "#" * int(round(i * 30.0))
    print(f"{y * 1000.0:>4.1f} mm {i:.3f} {bar}")
measured = 0.00432
guess = measured * d / l * 1000000000.0
print(f"a fringe spacing of 4.32 mm means {guess:.0f} nm light")
