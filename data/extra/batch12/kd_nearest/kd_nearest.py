def build(ns, pts, axis):
    if len(pts) == 0:
        return -1
    if axis == 0:
        sp = sorted(pts, key=lambda p: (p[0], p[1]))
    else:
        sp = sorted(pts, key=lambda p: (p[1], p[0]))
    mid = len(sp) // 2
    m = sp[mid]
    l = build(ns, sp[0:mid], 1 - axis)
    r = build(ns, sp[mid + 1:], 1 - axis)
    ns.append([m[0], m[1], m[2], axis, l, r])
    return len(ns) - 1

def near(ns, i, qx, qy, best):
    if i < 0:
        return
    best[2] += 1
    x, y, name, axis, left, right = ns[i]
    d = (x - qx) * (x - qx) + (y - qy) * (y - qy)
    if best[0] < 0 or d < best[1]:
        best[0] = i
        best[1] = d
    diff = qx - x if axis == 0 else qy - y
    first = left if diff < 0 else right
    second = right if diff < 0 else left
    near(ns, first, qx, qy, best)
    if diff * diff < best[1]:
        near(ns, second, qx, qy, best)

cafes = [(2, 3, "Bean"), (5, 4, "Brew"), (9, 6, "Cup"), (4, 7, "Drip"), (8, 1, "Espresso"), (7, 2, "Froth"), (1, 9, "Grind"), (6, 8, "Hops"), (3, 5, "Java")]
ns = []
root = build(ns, cafes, 0)
print(f"root splits at {ns[root][2]} ({ns[root][0]}, {ns[root][1]})")
for q in [[9, 2], [3, 3], [5, 9], [0, 0]]:
    best = [-1, 0, 0]
    near(ns, root, q[0], q[1], best)
    print(f"({q[0]}, {q[1]}): nearest {ns[best[0]][2]}, squared distance {best[1]}, {best[2]} of {len(ns)} visited")
