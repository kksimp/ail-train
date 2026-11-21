import math
L = 200.0
W = 15.0

def pull(sag):
    return W * L * L / (8.0 * sag)

def peak(sag):
    h = pull(sag)
    v = W * L / 2.0
    return math.sqrt(h * h + v * v)

def cable(sag):
    return L + 8.0 * sag * sag / (3.0 * L)

def sag_for(c):
    return math.sqrt(3.0 * L * (c - L) / 8.0)

for sag in [1.0, 2.0, 4.0, 8.0, 16.0]:
    print(f"sag {sag:>4.0f} m: pull {pull(sag) / 1000.0:>6.2f} kN, at the towers {peak(sag) / 1000.0:>6.2f} kN, cable {cable(sag):.3f} m")
cold = cable(4.0)
for warm in [10.0, 30.0, 50.0]:
    stretched = cold * (1.0 + 0.000023 * warm)
    print(f"{warm:.0f} C warmer: cable grows to {stretched:.3f} m and sags {sag_for(stretched):.2f} m")
