import math
PI = 3.141592653589793
NA = 602214076000000000000000.0
ATOMS = {"Simple": 1, "BodyCentred": 2, "FaceCentred": 4}

def edge(c, r):
    if c == "Simple":
        return 2.0 * r
    if c == "BodyCentred":
        return 4.0 * r / math.sqrt(3.0)
    return 2.0 * math.sqrt(2.0) * r

def fill(c):
    a = edge(c, 1.0)
    return float(ATOMS[c]) * 4.0 / 3.0 * PI / (a * a * a)

for c in ["Simple", "BodyCentred", "FaceCentred"]:
    print(f"Cell.{c}: {ATOMS[c]} atoms per cell, packing {fill(c) * 100.0:.1f}%")
for name, c, r, molar, known in [("polonium", "Simple", 0.167, 209.0, 9.2), ("iron", "BodyCentred", 0.1241, 55.85, 7.87), ("tungsten", "BodyCentred", 0.1371, 183.84, 19.3), ("copper", "FaceCentred", 0.1278, 63.55, 8.96), ("aluminium", "FaceCentred", 0.1432, 26.98, 2.70)]:
    a_cm = edge(c, r) / 10000000.0
    rho = float(ATOMS[c]) * molar / (NA * a_cm * a_cm * a_cm)
    print(f"{name:<9} a {edge(c, r):.4f} nm, density {rho:.2f} g/cm3 (measured {known})")
