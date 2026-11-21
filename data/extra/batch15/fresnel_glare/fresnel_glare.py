import math
def reflectance(n1, n2):
    r = (n1 - n2) / (n1 + n2)
    return r * r
def brewster(n1, n2):
    pi = 3.141592653589793
    return math.atan(n2 / n1) * 180.0 / pi
stuff = [("water", 1.333), ("glass", 1.52), ("acrylic", 1.49), ("diamond", 2.42)]
for name, n in stuff:
    r = reflectance(1.0, n) * 100.0
    through = 1.0 - reflectance(1.0, n)
    pane = through * through * 100.0
    b = brewster(1.0, n)
    print(f"{name:<8} n={n:.3f}: reflects {r:.2f}%, pane passes {pane:.1f}%, Brewster {b:.1f} deg")
s = sorted(stuff, key=lambda m: -int(m[1] * 1000.0))
print(f"most glare: {s[0][0]}")
under = reflectance(1.333, 1.52) * 100.0
print(f"glass under water reflects {under:.2f}%")
