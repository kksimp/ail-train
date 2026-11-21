def key(x, y, z):
    return (x + 1) * 10000 + (y + 1) * 100 + z + 1

text = "1,2,2 3,2,2 2,1,2 2,3,2 2,2,1 2,2,3 3,3,2 4,2,2 1,1,1 5,5,5 4,3,2"
cubes = set(); pts = []
for t in text.split(" "):
    p = [int(v) for v in t.split(",")]
    pts.append(p); cubes.add(key(*p))
dirs = [[1, 0, 0], [-1, 0, 0], [0, 1, 0], [0, -1, 0], [0, 0, 1], [0, 0, -1]]
open_ = 0
for p in pts:
    for d in dirs:
        if key(p[0] + d[0], p[1] + d[1], p[2] + d[2]) not in cubes:
            open_ += 1
print(f"{len(pts)} cubes")
print(f"part 1: {open_} faces touch air")
outside = {key(-1, -1, -1)}
queue = [[-1, -1, -1]]
while queue:
    q = queue.pop()
    for d in dirs:
        nx, ny, nz = q[0] + d[0], q[1] + d[1], q[2] + d[2]
        inside = -1 <= nx <= 7 and -1 <= ny <= 7 and -1 <= nz <= 7
        k = key(nx, ny, nz)
        if inside and k not in cubes and k not in outside:
            outside.add(k); queue.append([nx, ny, nz])
outer = 0
for p in pts:
    for d in dirs:
        if key(p[0] + d[0], p[1] + d[1], p[2] + d[2]) in outside:
            outer += 1
print(f"part 2: {outer} faces touch outside air")
print(f"{open_ - outer} faces look into sealed pockets")
