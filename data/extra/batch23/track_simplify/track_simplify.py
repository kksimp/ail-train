def simplify(pts, first, last, tol, keep):
    if last <= first + 1:
        return
    ax = pts[first][0]
    ay = pts[first][1]
    dx = pts[last][0] - ax
    dy = pts[last][1] - ay
    len2 = dx * dx + dy * dy
    far = -1
    far_cross = -1
    for i in range(first + 1, last):
        c = abs(dx * (pts[i][1] - ay) - dy * (pts[i][0] - ax))
        if c > far_cross:
            far_cross = c
            far = i
    if far_cross * far_cross > tol * tol * len2:
        keep[far] = True
        simplify(pts, first, far, tol, keep)
        simplify(pts, far, last, tol, keep)

def run(pts, tol):
    keep = [False for p in pts]
    keep[0] = True
    keep[len(pts) - 1] = True
    simplify(pts, 0, len(pts) - 1, tol, keep)
    return [i for i in range(len(pts)) if keep[i]]

track = [[0, 0], [2, 1], [4, 0], [6, 3], [8, 2], [10, 8], [12, 9], [14, 7], [16, 10], [18, 9], [20, 15], [22, 14], [24, 16]]
print(f"track of {len(track)} points")
for tol in [0, 1, 2, 4, 8]:
    kept = run(track, tol)
    shown = "".join([f" ({track[i][0]},{track[i][1]})" for i in kept])
    print(f"tolerance {tol}: {len(kept):>2} points{shown}")
