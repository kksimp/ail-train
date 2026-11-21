class Target:
    def __init__(self, name, x, y, r):
        self.name = name
        self.x = x
        self.y = y
        self.r = r

def hits(ax, ay, bx, by, t):
    dx = bx - ax
    dy = by - ay
    len2 = dx * dx + dy * dy
    px = t.x - ax
    py = t.y - ay
    dot = px * dx + py * dy
    if dot <= 0:
        return px * px + py * py <= t.r * t.r
    if dot >= len2:
        qx = t.x - bx
        qy = t.y - by
        return qx * qx + qy * qy <= t.r * t.r
    c = px * dy - py * dx
    return c * c <= t.r * t.r * len2

def along(ax, ay, bx, by, t):
    return (t.x - ax) * (bx - ax) + (t.y - ay) * (by - ay)

targets = [Target("red", 5, 3, 2), Target("blue", 9, 9, 1), Target("green", 14, 6, 3), Target("gold", 3, 8, 2), Target("grey", 20, 12, 2)]
for beam in [[0, 0, 16, 8], [0, 0, 10, 10], [2, 10, 18, 2]]:
    struck = [t for t in targets if hits(beam[0], beam[1], beam[2], beam[3], t)]
    struck = sorted(struck, key=lambda t: along(beam[0], beam[1], beam[2], beam[3], t))
    names = [t.name for t in struck]
    shown = "nothing" if len(names) == 0 else ", ".join(names)
    print(f"beam ({beam[0]},{beam[1]})->({beam[2]},{beam[3]}): hits {shown}")
