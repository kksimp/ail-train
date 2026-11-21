from math import gcd

def on_edge(x1, y1, x2, y2, px, py):
    cross = (x2 - x1) * (py - y1) - (y2 - y1) * (px - x1)
    return cross == 0 and min(x1, x2) <= px <= max(x1, x2) and min(y1, y2) <= py <= max(y1, y2)

def inside(xs, ys, px, py):
    n = len(xs)
    odd = False
    for i in range(n):
        j = (i + 1) % n
        if (ys[i] > py) != (ys[j] > py):
            num = (py - ys[i]) * (xs[j] - xs[i])
            den = ys[j] - ys[i]
            left = px * den < xs[i] * den + num if den > 0 else px * den > xs[i] * den + num
            if left:
                odd = not odd
    return odd

shapes = [[[0, 4, 4, 0], [0, 0, 3, 3]], [[0, 5, 2], [0, 1, 4]], [[1, 7, 8, 4, 0], [0, 1, 5, 7, 3]], [[0, 6, 6, 3, 0], [0, 0, 6, 2, 6]]]
for xs, ys in shapes:
    n = len(xs)
    twice = 0
    boundary = 0
    for i in range(n):
        j = (i + 1) % n
        twice += xs[i] * ys[j] - xs[j] * ys[i]
        boundary += gcd(abs(xs[j] - xs[i]), abs(ys[j] - ys[i]))
    twice = abs(twice)
    interior = (twice - boundary + 2) // 2
    counted = 0
    for px in range(min(xs), max(xs) + 1):
        for py in range(min(ys), max(ys) + 1):
            edge = any(on_edge(xs[i], ys[i], xs[(i + 1) % n], ys[(i + 1) % n], px, py) for i in range(n))
            if not edge and inside(xs, ys, px, py):
                counted += 1
    half = ".5" if twice % 2 == 1 else ""
    print(f"corners x {xs} y {ys}: area {twice // 2}{half}, B = {boundary}, I by Pick {interior}, counted {counted}")
