def side(a, b, p):
    return (b[0] - a[0]) * (p[1] - a[1]) - (p[0] - a[0]) * (b[1] - a[1])

def winding(path, p):
    wn = 0
    for i in range(len(path)):
        a = path[i]
        b = path[(i + 1) % len(path)]
        if a[1] <= p[1]:
            if b[1] > p[1] and side(a, b, p) > 0:
                wn += 1
        elif b[1] <= p[1] and side(a, b, p) < 0:
            wn -= 1
    return wn

def crossings(path, p):
    count = 0
    for i in range(len(path)):
        a = path[i]
        b = path[(i + 1) % len(path)]
        if (a[1] > p[1]) != (b[1] > p[1]):
            s = side(a, b, p)
            if (s > 0) == (b[1] > a[1]):
                count += 1
    return count

star = [[0, 10], [-6, -8], [10, 4], [-10, 4], [6, -8]]
beacons = [[0, 0], [0, 7], [5, 3], [-7, 3], [12, 0], [0, -6]]
print("flight path: a five-pointed star drawn in one stroke")
for b in beacons:
    w = winding(star, b)
    parity = "inside" if crossings(star, b) % 2 == 1 else "outside"
    print(f"beacon ({b[0]:>3}, {b[1]:>2}): circled {w} times, even-odd says {parity}")
