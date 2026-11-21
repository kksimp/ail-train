EMPTY, TREE, FIRE = 0, 1, 2

class Lcg:
    def __init__(self, s):
        self.state = s
    def chance(self, per):
        self.state = (self.state * 1103515245 + 12345) % 2147483648
        return (self.state // 65536) % 1000 < per

def burning_near(g, r, c):
    for dr in range(-1, 2):
        for dc in range(-1, 2):
            rr = r + dr
            cc = c + dc
            if rr >= 0 and rr < len(g) and cc >= 0 and cc < len(g[0]) and g[rr][cc] == FIRE:
                return True
    return False

def step(g, rng):
    out = []
    for r in range(len(g)):
        row = []
        for c in range(len(g[0])):
            x = g[r][c]
            if x == FIRE:
                nxt = EMPTY
            elif x == TREE:
                nxt = FIRE if burning_near(g, r, c) or rng.chance(1) else TREE
            else:
                nxt = TREE if rng.chance(40) else EMPTY
            row.append(nxt)
        out.append(row)
    return out

def count(g, kind):
    return sum(sum(1 for x in row if x == kind) for row in g)

rng = Lcg(42)
g = []
for r in range(8):
    row = []
    for c in range(24):
        row.append(TREE if rng.chance(550) else EMPTY)
    g.append(row)
for t in range(61):
    if t % 10 == 0:
        print(f"step {t:>2}: trees {count(g, TREE):>3}, burning {count(g, FIRE):>2}")
    g = step(g, rng)
for row in g:
    print("".join("T" if x == TREE else ("*" if x == FIRE else ".") for x in row))
