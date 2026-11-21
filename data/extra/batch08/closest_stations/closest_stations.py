import math
names = ["Alder", "Brook", "Crest", "Dune", "Eyre", "Fell"]
xs = [2.0, 14.5, 7.0, 30.0, 14.0, 22.0]; ys = [3.0, 8.0, 21.0, 4.5, 9.5, 18.0]
near = (0, 1, 1000000.0); far = (0, 1, 0.0)
for i in range(6):
    for j in range(i + 1, 6):
        d = math.hypot(xs[i] - xs[j], ys[i] - ys[j])
        if d < near[2]: near = (i, j, d)
        if d > far[2]: far = (i, j, d)
print(f"closest: {names[near[0]]} and {names[near[1]]}, {near[2]:.2f} km")
print(f"furthest: {names[far[0]]} and {names[far[1]]}, {far[2]:.2f} km")
print("15 pairs checked")
