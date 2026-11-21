import math
R = 8.314

def vapour(dh, boil, t):
    return 101.325 * math.exp(-dh / R * (1.0 / t - 1.0 / boil))

def boils_at(dh, boil, kpa):
    return 1.0 / (1.0 / boil - R * math.log(kpa / 101.325) / dh)

water = ("water", 40660.0, 373.15)
ethanol = ("ethanol", 38560.0, 351.4)
for name, dh, boil in [water, ethanol]:
    parts = [f"{c:.0f} C {vapour(dh, boil, c + 273.15):.1f} kPa" for c in [20.0, 50.0, 80.0]]
    print(f"{name}: {', '.join(parts)}")
for name, kpa in [("Everest summit", 33.7), ("La Paz", 66.0), ("Denver", 83.4), ("pressure cooker", 200.0)]:
    print(f"{name:<16} {kpa:>6.1f} kPa: water boils at {boils_at(40660.0, 373.15, kpa) - 273.15:.1f} C")
