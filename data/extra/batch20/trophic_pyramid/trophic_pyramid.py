import math
sunlight_crop = 20000.0
area = 10000.0
levels = [("grasshoppers", 0.1, 200.0), ("shrews", 0.12, 5000.0), ("owls", 0.05, 40000.0)]
energy = sunlight_crop * area
print(f"plants fix {sunlight_crop:.0f} kcal per m2 a year over {area:.0f} m2: {energy / 1000000.0:.1f} Mkcal")
for name, eff, need in levels:
    energy = energy * eff
    animals = int(math.floor(energy / need))
    print(f"{name:<12} take in {energy:>12.0f} kcal a year, enough for {animals} animals")
person = 900000.0
grain = 3000.0 * 10000.0
as_grain = int(math.floor((grain * 0.9) / person))
as_beef = int(math.floor((grain * 0.1 * 0.9) / person))
print(f"a hectare of grain feeds {as_grain} people directly, {as_beef} through cattle")
