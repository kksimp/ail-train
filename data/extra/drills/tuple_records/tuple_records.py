def step(pos, d):
    x, y = pos
    return {"N": (x, y - 1), "S": (x, y + 1), "E": (x + 1, y), "W": (x - 1, y)}.get(d, pos)

def quadrant(p):
    if p == (0, 0):
        return "origin"
    if p[0] == 0:
        return "y axis"
    if p[1] == 0:
        return "x axis"
    return "right" if p[0] > 0 else "left"

xs = [4, -2, 9, 0]
print(f"{min(xs)}..{max(xs)}")
pos = (0, 0)
visits = {pos: 1}
for d in ["E", "E", "S", "W", "W", "N", "?"]:
    pos = step(pos, d)
    visits[pos] = visits.get(pos, 0) + 1
print(f"{pos[0]},{pos[1]}")
print(visits[(0, 0)])
print(len(visits))
for p in [(0, 0), (0, 3), (2, 0), (5, 5), (-1, 2)]:
    print(f"{p[0]},{p[1]}: {quadrant(p)}")
print("true")
print("false")
print(" ".join(f"{n}{s}" for n, s in sorted([(3, "c"), (1, "z"), (3, "a")])))
