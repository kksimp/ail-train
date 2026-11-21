def parse(line):
    a, b = line.split(" ")
    lo = []; hi = []
    for part in b.split(","):
        e = part.split("=")[1].split("..")
        lo.append(int(e[0])); hi.append(int(e[1]))
    return (lo, hi, 1 if a == "on" else -1)

def volume(p):
    lo, hi, s = p
    return s * (hi[0] - lo[0] + 1) * (hi[1] - lo[1] + 1) * (hi[2] - lo[2] + 1)

steps = ["on x=-8..2,y=-3..6,z=-4..4", "on x=-2..9,y=0..10,z=-6..1", "off x=-4..4,y=-4..4,z=-4..4", "on x=1..12,y=-12..-2,z=3..8", "off x=6..7,y=-10..10,z=-10..10", "on x=-1..1,y=-1..1,z=-1..1"]
boxes = [parse(s) for s in steps]
core = 0
for x in range(-5, 6):
    for y in range(-5, 6):
        for z in range(-5, 6):
            lit = False
            for lo, hi, s in boxes:
                if lo[0] <= x <= hi[0] and lo[1] <= y <= hi[1] and lo[2] <= z <= hi[2]:
                    lit = s > 0
            if lit: core += 1
print(f"part 1: {core} cells lit in the core")
parts = []
for b in boxes:
    added = []
    for p in parts:
        lo = [max(p[0][i], b[0][i]) for i in range(3)]
        hi = [min(p[1][i], b[1][i]) for i in range(3)]
        if lo[0] <= hi[0] and lo[1] <= hi[1] and lo[2] <= hi[2]:
            added.append((lo, hi, -p[2]))
    if b[2] > 0:
        added.append(b)
    parts.extend(added)
print(f"{len(parts)} signed cuboids kept")
print(f"part 2: {sum(volume(p) for p in parts)} cells lit in all")
