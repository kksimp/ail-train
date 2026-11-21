class Drone:
    def __init__(self, x, y, z, r):
        self.x, self.y, self.z, self.r = x, y, z, r
    def reaches(self, x, y, z):
        return abs(self.x - x) + abs(self.y - y) + abs(self.z - z) <= self.r

def parse(line):
    a, b = line.split(" r=")
    p = [int(v) for v in a.split(",")]
    return Drone(p[0], p[1], p[2], int(b))

lines = ["0,0,0 r=4", "1,0,0 r=1", "4,0,0 r=3", "0,2,0 r=1", "0,5,0 r=3", "0,0,3 r=1", "1,1,2 r=1", "6,6,6 r=2", "3,3,3 r=5"]
drones = [parse(l) for l in lines]
strong = drones[0]
for d in drones:
    if d.r > strong.r: strong = d
inside = sum(1 for d in drones if strong.reaches(d.x, d.y, d.z))
print(f"strongest drone at {strong.x},{strong.y},{strong.z} with radius {strong.r}")
print(f"part 1: {inside} drones are within its range")
best = -1; spot = [0, 0, 0]
for x in range(7):
    for y in range(7):
        for z in range(7):
            n = sum(1 for d in drones if d.reaches(x, y, z))
            closer = x + y + z < sum(spot)
            if n > best or (n == best and closer):
                best = n; spot = [x, y, z]
print(f"part 2: {spot[0]},{spot[1]},{spot[2]} hears {best} drones, {sum(spot)} from the base")
