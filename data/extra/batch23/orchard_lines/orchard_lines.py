def gcd(a, b):
    while b != 0:
        a, b = b, int(a - b * int(a / b))
    return abs(a)

def best_line(pts):
    best = 0
    pair = [0, 0]
    for i in range(len(pts)):
        dirs = {}
        first = {}
        same = 0
        for j in range(len(pts)):
            if j != i:
                dx = pts[j][0] - pts[i][0]
                dy = pts[j][1] - pts[i][1]
                if dx == 0 and dy == 0:
                    same += 1
                else:
                    g = gcd(dx, dy)
                    dx = int(dx / g)
                    dy = int(dy / g)
                    if dx < 0 or (dx == 0 and dy < 0):
                        dx = -dx
                        dy = -dy
                    key = f"{dx},{dy}"
                    dirs[key] = dirs.get(key, 0) + 1
                    if key not in first:
                        first[key] = j
        for key, count in dirs.items():
            if count + same + 1 > best:
                best = count + same + 1
                pair = [i, first[key]]
        if same + 1 > best:
            best = same + 1
            pair = [i, i]
    return [best, pair[0], pair[1]]

trees = [[1, 1], [3, 2], [5, 3], [4, 1], [2, 3], [1, 4], [7, 4], [6, 6], [9, 5], [0, 5]]
b = best_line(trees)
p = trees[b[1]]
q = trees[b[2]]
print(f"{len(trees)} trees; the best line holds {b[0]} of them")
print(f"it runs through ({p[0]}, {p[1]}) and ({q[0]}, {q[1]})")
on = []
for t in trees:
    if (q[0] - p[0]) * (t[1] - p[1]) == (q[1] - p[1]) * (t[0] - p[0]):
        on.append(f"({t[0]}, {t[1]})")
shown = " ".join(on)
print(f"trees on it: {shown}")
