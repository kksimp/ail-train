class Sensor:
    def __init__(self, x, y, bx, by):
        self.x, self.y, self.bx, self.by = x, y, bx, by
    def radius(self):
        return abs(self.x - self.bx) + abs(self.y - self.by)
    def covers(self, px, py):
        return abs(self.x - px) + abs(self.y - py) <= self.radius()

lines = ["8,1 12,7", "0,5 3,8", "14,5 14,12", "5,16 0,12", "18,5 22,0", "15,16 10,21", "19,18 22,22"]
sensors = []
for l in lines:
    a, b = l.split(" ")
    s = a.split(","); t = b.split(",")
    sensors.append(Sensor(int(s[0]), int(s[1]), int(t[0]), int(t[1])))
for s in sensors:
    print(f"sensor ({s.x},{s.y}) reaches {s.radius()}")
row = 10
ruled = 0
for x in range(-20, 40):
    if any(s.covers(x, row) for s in sensors) and not any(s.bx == x and s.by == row for s in sensors):
        ruled += 1
print(f"part 1: {ruled} cells on row {row} cannot hold a beacon")
gaps = 0
first = ""
for y in range(21):
    for x in range(21):
        if not any(s.covers(x, y) for s in sensors):
            gaps += 1
            if first == "":
                first = f"({x},{y}) tuning {x * 4000 + y}"
print(f"part 2: {gaps} uncovered cells, first at {first}")
