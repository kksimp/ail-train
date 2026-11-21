import math
PI = 3.141592653589793
MU0 = 0.0000012566370614

def depth_mm(rho, mur, hz):
    return math.sqrt(rho / (PI * hz * MU0 * mur)) * 1000.0

def ac_factor(r, d):
    return 1.0 if d >= r else r / (2.0 * d)

metals = [("copper", 0.0000000168, 1.0), ("aluminium", 0.0000000265, 1.0), ("mild steel", 0.00000015, 100.0)]
freqs = [50.0, 1000.0, 100000.0, 10000000.0]
for name, rho, mur in metals:
    cells = [f"{depth_mm(rho, mur, f):.3f}" for f in freqs]
    print(f"{name:<10} depth mm at 50 Hz, 1 kHz, 100 kHz, 10 MHz: {' / '.join(cells)}")
radius = 1.0
for f in freqs:
    d = depth_mm(0.0000000168, 1.0, f)
    print(f"2 mm copper wire at {f:>10.0f} Hz: AC resistance x {ac_factor(radius, d):.2f}")
