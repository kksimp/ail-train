import math
linings = [("concrete", 0.013), ("earth", 0.025), ("grass", 0.035), ("rubble", 0.045)]
width = 1.5
slope = 0.002
def velocity(n, width, depth, slope):
    area = width * depth
    wetted = width + 2.0 * depth
    r = area / wetted
    return r ** (2.0 / 3.0) * math.sqrt(slope) / n
for name, n in linings:
    cells = []
    for depth in [0.25, 0.5, 1.0]:
        q = velocity(n, width, depth, slope) * width * depth
        cells.append(f"{q:.3f}")
    row = " ".join(cells)
    print(f"{name:<9} n {n}: flow at 0.25/0.5/1.0 m deep = {row} m3/s")
depth = 0.01
while velocity(0.025, width, depth, slope) * width * depth < 2.0:
    depth += 0.01
print(f"an earth ditch carries 2 m3/s at about {depth:.2f} m deep")
