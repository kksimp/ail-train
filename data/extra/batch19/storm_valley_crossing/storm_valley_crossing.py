class Gust:
    def __init__(self, r, c, dr, dc):
        self.r, self.c, self.dr, self.dc = r, c, dr, dc

def busy(gusts, h, w, t):
    s = set()
    for g in gusts:
        r = ((g.r + t * g.dr) % h + h) % h
        c = ((g.c + t * g.dc) % w + w) % w
        s.add(r * 100 + c)
    return s

def cross(gusts, h, w, frm, to, t0):
    t = t0
    here = {frm[0] * 100 + frm[1]}
    while to[0] * 100 + to[1] not in here:
        t += 1
        blocked = busy(gusts, h, w, t)
        nxt = set()
        for p in here:
            r = p // 100 - 1; c = p % 100
            for d in [[0, 0], [1, 0], [-1, 0], [0, 1], [0, -1]]:
                nr = r + d[0]; nc = c + d[1]
                ok = (0 <= nr < h and 0 <= nc < w) or (nr == frm[0] - 1 and nc == frm[1]) or (nr == to[0] - 1 and nc == to[1])
                if ok and nr * 100 + nc not in blocked:
                    nxt.add((nr + 1) * 100 + nc)
        here = nxt
    return t

valley = [">.<.v.", ".^..>.", "<..v..", "..>..^"]
gusts = []
moves = {'>': (0, 1), '<': (0, -1), '^': (-1, 0), 'v': (1, 0)}
for r, line in enumerate(valley):
    for c, ch in enumerate(line):
        if ch in moves:
            gusts.append(Gust(r, c, moves[ch][0], moves[ch][1]))
h = len(valley); w = len(valley[0])
start = [0, 0]; goal = [h + 1, w - 1]
print(f"{len(gusts)} gusts in a {h} by {w} valley")
t1 = cross(gusts, h, w, start, goal, 0)
print(f"part 1: across in {t1} minutes")
t2 = cross(gusts, h, w, goal, start, t1)
t3 = cross(gusts, h, w, start, goal, t2)
print(f"back at the start at minute {t2}")
print(f"part 2: across again by minute {t3}")
