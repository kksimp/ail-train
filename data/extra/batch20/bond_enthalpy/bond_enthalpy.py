def energy(bonds, lst):
    return sum(bonds[n] * c for n, c in lst)

bonds = {"C-H": 413, "O=O": 498, "C=O": 799, "O-H": 463, "C-C": 348, "H-H": 436, "N#N": 945, "N-H": 391, "Cl-Cl": 242, "H-Cl": 431}
reactions = [("CH4 + 2 O2 -> CO2 + 2 H2O", [("C-H", 4), ("O=O", 2)], [("C=O", 2), ("O-H", 4)], -802), ("N2 + 3 H2 -> 2 NH3", [("N#N", 1), ("H-H", 3)], [("N-H", 6)], -92), ("H2 + Cl2 -> 2 HCl", [("H-H", 1), ("Cl-Cl", 1)], [("H-Cl", 2)], -185), ("2 C2H6 + 7 O2 -> 4 CO2 + 6 H2O", [("C-C", 2), ("C-H", 12), ("O=O", 7)], [("C=O", 8), ("O-H", 12)], -2856)]
for eq, broken, formed, measured in reactions:
    b = energy(bonds, broken)
    f = energy(bonds, formed)
    dh = b - f
    off = dh - measured
    print(f"{eq}: break {b}, form {f}, estimate {dh} kJ (measured {measured}, off by {off})")
