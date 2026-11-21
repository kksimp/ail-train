import math
alphas = [("OpenSea", 0.11), ("Grassland", 0.16), ("Woodland", 0.25), ("City", 0.4)]
def at_height(v10, h, a): return math.pow(h / 10.0, a) * v10
v10 = 6.0
print(f"mast reading {v10:.1f} m/s at 10 m")
for name, a in alphas:
    cells = []
    for h in [50.0, 80.0, 120.0]:
        v = at_height(v10, h, a)
        cells.append(f"{h:.0f} m {v:.2f}")
    print(f"{name:<9} {', '.join(cells)}")
sea = at_height(v10, 100.0, 0.11)
land = at_height(v10, 100.0, 0.25)
ratio = (sea / land) * (sea / land) * (sea / land)
print(f"at 100 m a sea turbine gets {ratio:.2f} times the power of one over woodland")
