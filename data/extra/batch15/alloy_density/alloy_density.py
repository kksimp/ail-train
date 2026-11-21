def alloy_density(parts, metals):
    inv = 0.0
    for name, w in parts:
        inv += w / metals[name]
    return 1.0 / inv
metals = {"Cu": 8.96, "Zn": 7.14, "Sn": 7.29, "Pb": 11.34, "Ag": 10.49}
alloys = [("brass", [("Cu", 0.65), ("Zn", 0.35)]), ("bronze", [("Cu", 0.88), ("Sn", 0.12)]), ("solder", [("Sn", 0.6), ("Pb", 0.4)]), ("sterling", [("Ag", 0.925), ("Cu", 0.075)])]
found = {}
for name, parts in alloys:
    rho = alloy_density(parts, metals)
    found[name] = rho
    naive = 0.0
    for p in parts: naive = naive + p[1] * metals[p[0]]
    print(f"{name:<9} {rho:.3f} g/cm3 (weighted average would say {naive:.3f})")
grams = 84.3; cm3 = 10.0
measured = grams / cm3
best = ""; gap = 100.0
for name, rho in found.items():
    if abs(rho - measured) < gap:
        gap = abs(rho - measured); best = name
print(f"casting {grams:.1f} g in {cm3:.1f} cm3 = {measured:.2f} g/cm3, closest to {best}")
