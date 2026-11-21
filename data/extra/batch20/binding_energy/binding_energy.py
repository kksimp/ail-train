import math

def binding(a, z):
    af = float(a)
    zf = float(z)
    n = a - z
    third = math.cbrt(af)
    b = 15.8 * af - 18.3 * third * third - 0.714 * zf * (zf - 1.0) / third - 23.2 * (af - 2.0 * zf) * (af - 2.0 * zf) / af
    pair = 12.0 / math.sqrt(af)
    if z % 2 == 0 and n % 2 == 0:
        b += pair
    elif z % 2 == 1 and n % 2 == 1:
        b -= pair
    return b

def best_z(a):
    best = 1
    for z in range(1, a):
        if binding(a, z) > binding(a, best):
            best = z
    return best

for name, a, z in [("He-4", 4, 2), ("C-12", 12, 6), ("O-16", 16, 8), ("Fe-56", 56, 26), ("Ni-62", 62, 28), ("Sn-120", 120, 50), ("Pb-208", 208, 82), ("U-238", 238, 92)]:
    b = binding(a, z)
    print(f"{name:<7} B {b:>7.1f} MeV, {b / float(a):.3f} MeV per nucleon")
for a in [16, 56, 120, 208]:
    print(f"mass {a}: most bound with {best_z(a)} protons")
