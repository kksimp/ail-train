def sign(v):
    return 1 if v > 0 else (-1 if v < 0 else 0)

def overlaps(lines, diagonals):
    hits = {}
    for l in lines:
        dx = sign(l[2] - l[0]); dy = sign(l[3] - l[1])
        if dx != 0 and dy != 0 and not diagonals:
            continue
        steps = max(abs(l[2] - l[0]), abs(l[3] - l[1]))
        for i in range(steps + 1):
            k = (l[0] + i * dx) * 100 + l[1] + i * dy
            hits[k] = hits.get(k, 0) + 1
    return sum(1 for n in hits.values() if n >= 2)

text = ["1,1 -> 1,7", "0,4 -> 6,4", "2,2 -> 7,7", "7,1 -> 2,6", "5,0 -> 5,8", "3,8 -> 8,8", "0,7 -> 4,3", "6,6 -> 6,2"]
lines = [[int(v) for v in t.replace(" -> ", ",").split(",")] for t in text]
straight = sum(1 for l in lines if l[0] == l[2] or l[1] == l[3])
print(f"{len(lines)} vent lines, {straight} straight")
print(f"part 1: {overlaps(lines, False)} points where straight lines overlap")
print(f"part 2: {overlaps(lines, True)} points with diagonals too")
