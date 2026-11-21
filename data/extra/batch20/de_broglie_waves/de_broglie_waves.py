H = 0.000000000000000000000000000000000662607
ME = 0.000000000000000000000000000000910938
QE = 0.0000000000000000001602177

def sci(x):
    e = 0
    m = x
    while m < 1.0:
        m *= 10.0
        e -= 1
    while m >= 10.0:
        m /= 10.0
        e += 1
    return f"{m:.2f} x 10^{e} m"

def electron_nm(v):
    import math
    p = math.sqrt(2.0 * ME * QE * v)
    return H / p * 1000000000.0

import math
for v in [50.0, 150.0, 1000.0, 30000.0]:
    print(f"electron through {v:.0f} V: {electron_nm(v):.4f} nm")
neutron = 0.00000000000000000000000000167493
thermal = math.sqrt(2.0 * neutron * 0.025 * QE)
print(f"thermal neutron (0.025 eV): {H / thermal * 1000000000.0:.4f} nm")
for name, mass, speed in [("baseball at 40 m/s", 0.145, 40.0), ("dust grain at 1 mm/s", 0.000000001, 0.001), ("walker at 1.4 m/s", 70.0, 1.4)]:
    print(f"{name}: {sci(H / (mass * speed))}")
