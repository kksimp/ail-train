class Bot:
    def __init__(self, px, py, vx, vy):
        self.px, self.py, self.vx, self.vy = px, py, vx, vy
    def at(self, t):
        return [((self.px + t * self.vx) % 11 + 11) % 11, ((self.py + t * self.vy) % 7 + 7) % 7]

def parse(line):
    a, b = line.split(" ")
    p = a[2:].split(","); v = b[2:].split(",")
    return Bot(int(p[0]), int(p[1]), int(v[0]), int(v[1]))

lines = ["p=1,2 v=3,-2", "p=8,0 v=-1,4", "p=5,5 v=2,2", "p=0,6 v=-3,-1", "p=10,3 v=1,1", "p=4,1 v=-2,3", "p=7,4 v=4,-3", "p=2,0 v=1,5", "p=6,6 v=-4,2", "p=9,1 v=2,-1"]
bots = [parse(l) for l in lines]
quads = [0, 0, 0, 0]
for b in bots:
    q = b.at(100)
    if q[0] != 5 and q[1] != 3:
        quads[(0 if q[0] < 5 else 1) + (0 if q[1] < 3 else 2)] += 1
print(f"quadrants after 100 s: {quads}")
print(f"part 1: safety factor {quads[0] * quads[1] * quads[2] * quads[3]}")
t = 1; tile = -1
while tile < 0 and t < 77:
    seen = set()
    for b in bots:
        q = b.at(t); k = q[0] * 10 + q[1]
        if k in seen:
            tile = k; break
        seen.add(k)
    t += 1
print(f"part 2: two robots first meet after {t - 1} seconds at {tile // 10},{tile % 10}")
