import math

def simulate(m, rgb):
    out = []
    for row in m:
        x = row[0] * float(rgb[0]) + row[1] * float(rgb[1]) + row[2] * float(rgb[2])
        out.append(int(math.floor(x + 0.5)))
    return out

def dist2(a, b):
    return sum((a[i] - b[i]) * (a[i] - b[i]) for i in range(3))

names = ["red", "green", "blue", "orange", "purple", "brown"]
palette = [[214, 39, 40], [44, 160, 44], [31, 119, 180], [255, 127, 14], [148, 103, 189], [140, 86, 75]]
visions = [("protanopia", [[0.567, 0.433, 0.0], [0.558, 0.442, 0.0], [0.0, 0.242, 0.758]]), ("deuteranopia", [[0.625, 0.375, 0.0], [0.7, 0.3, 0.0], [0.0, 0.3, 0.7]]), ("tritanopia", [[0.95, 0.05, 0.0], [0.0, 0.433, 0.567], [0.0, 0.475, 0.525]])]
for vname, m in visions:
    sim = [simulate(m, c) for c in palette]
    clashes = []
    for i in range(len(sim)):
        for j in range(i + 1, len(sim)):
            if dist2(sim[i], sim[j]) < 1600:
                clashes.append(f"{names[i]}/{names[j]}")
    shown = "none" if not clashes else ", ".join(clashes)
    red = "[" + ", ".join(str(x) for x in sim[0]) + "]"
    print(f"{vname:<13} red looks {red}, clashes: {shown}")
