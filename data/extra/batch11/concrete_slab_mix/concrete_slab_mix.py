import math
slabs = [("shed base", 3.0, 2.4, 100.0), ("patio", 5.0, 4.0, 75.0), ("garage floor", 6.0, 3.5, 150.0)]
bags_total = 0
for name, l, w, d in slabs:
    wet = l * w * d / 1000.0
    dry = wet * 1.54
    cement = dry / 7.0
    sand = dry * 2.0 / 7.0
    gravel = dry * 4.0 / 7.0
    kg = cement * 1440.0
    bags = int(math.ceil(kg / 25.0))
    water = kg * 0.5
    bags_total += bags
    print(f"{name:<12} {wet:.3f} m3 wet: {bags} bags cement, {sand:.2f} m3 sand, {gravel:.2f} m3 gravel, {water:.1f} L water")
print(f"order {bags_total} bags in all")
