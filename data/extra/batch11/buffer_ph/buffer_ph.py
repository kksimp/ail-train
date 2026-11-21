import math
def ph(pka, base_mol, acid_mol):
    ratio = base_mol / acid_mol
    return pka + math.log10(ratio)
pka = 4.76
for b, a in [(0.1, 0.1), (0.2, 0.1), (0.1, 0.2), (0.05, 0.5)]:
    print(f"acetate {b} mol, acetic acid {a} mol: pH {ph(pka, b, a):.2f}")
base_mol = 0.1
acid_mol = 0.1
for step in range(1, 5):
    base_mol -= 0.02
    acid_mol += 0.02
    added = 0.02 * float(step)
    print(f"after {added:.2f} mol HCl: pH {ph(pka, base_mol, acid_mol):.2f}")
water_ph = 0.0 - math.log10(0.08 / 1.0)
print(f"the same 0.08 mol in 1 L of plain water: pH {water_ph:.2f}")
