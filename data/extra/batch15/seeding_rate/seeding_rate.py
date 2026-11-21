def seeds_m2(c): return c[1] / (c[3] * c[4])
def kg_ha(c): return seeds_m2(c) * c[2] / 100.0
crops = [("winter wheat", 250.0, 48.0, 0.92, 0.8, 0.62), ("spring barley", 300.0, 44.0, 0.95, 0.9, 0.58), ("oilseed rape", 40.0, 5.2, 0.9, 0.6, 9.5), ("maize", 9.0, 310.0, 0.94, 0.92, 4.1)]
for c in crops:
    seeds = seeds_m2(c); kg = kg_ha(c); cost = kg * c[5]
    print(f"{c[0]:<13} {seeds:>6.1f} seeds/m2, {kg:>6.1f} kg/ha, seed cost {cost:>6.2f}/ha")
p = max(crops, key=lambda c: int(kg_ha(c) * c[5] * 100.0))
print(f"dearest to sow: {p[0]}")
