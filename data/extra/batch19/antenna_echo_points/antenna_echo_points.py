def gcd(a, b):
    while b != 0:
        a, b = b, int(a - b * int(a / b))
    return abs(a)

rows = ["..........", "...a......", "......B...", ".....a....", "..........", "....B.....", "........a.", "..........", "..B.......", ".........."]
h = len(rows); w = len(rows[0])
by_freq = {}
for r, row in enumerate(rows):
    for c, ch in enumerate(row):
        if ch != '.':
            by_freq.setdefault(ch, []).append([r, c])
near = set(); line = set()
for f, pts in by_freq.items():
    print(f"channel {f}: {len(pts)} beacons")
    for i in range(len(pts)):
        for j in range(len(pts)):
            if i == j: continue
            a = pts[i]; b = pts[j]
            er = 2 * b[0] - a[0]; ec = 2 * b[1] - a[1]
            if 0 <= er < h and 0 <= ec < w:
                near.add(er * 100 + ec)
            g = gcd(b[0] - a[0], b[1] - a[1])
            sr = int((b[0] - a[0]) / g); sc = int((b[1] - a[1]) / g)
            r, c = a[0], a[1]
            while 0 <= r < h and 0 <= c < w:
                line.add(r * 100 + c); r += sr; c += sc
print(f"part 1: {len(near)} echo points")
print(f"part 2: {len(line)} points in line with a pair")
