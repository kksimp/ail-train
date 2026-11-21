solutes = [("table salt", 58.44, 2), ("magnesium chloride", 95.21, 3), ("sugar", 342.3, 1), ("ethylene glycol", 62.07, 1)]
def depression(s, grams):
    molality = grams / s[1]
    return float(s[2]) * 1.86 * molality
for s in solutes:
    dt = depression(s, 100.0)
    rise = dt / 1.86 * 0.512
    print(f"100 g {s[0]} in 1 kg water: freezes at {0.0 - dt:.2f} C, boils at {100.0 + rise:.2f} C")
target = 10.0
for s in solutes:
    need = target / (float(s[2]) * 1.86) * s[1]
    print(f"to reach -10 C: {need:>6.1f} g of {s[0]} per kg")
