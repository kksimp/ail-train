def cross(o, a, b):
    return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])

def inside(p, a, b, c):
    return cross(a, b, p) >= 0 and cross(b, c, p) >= 0 and cross(c, a, p) >= 0

def triangulate(poly):
    idx = list(range(len(poly)))
    tris = []
    while len(idx) > 3:
        n = len(idx)
        cut = -1
        for k in range(n):
            a = poly[idx[(k + n - 1) % n]]
            b = poly[idx[k]]
            c = poly[idx[(k + 1) % n]]
            if cut < 0 and cross(a, b, c) > 0:
                clear = True
                for other in idx:
                    p = poly[other]
                    if p != a and p != b and p != c and inside(p, a, b, c):
                        clear = False
                if clear:
                    cut = k
        tris.append([idx[(cut + n - 1) % n], idx[cut], idx[(cut + 1) % n]])
        idx.pop(cut)
    tris.append([idx[0], idx[1], idx[2]])
    return tris

poly = [[0, 0], [8, 0], [8, 6], [5, 3], [4, 7], [2, 4], [0, 6]]
twice = 0
for i in range(len(poly)):
    j = (i + 1) % len(poly)
    twice += poly[i][0] * poly[j][1] - poly[j][0] * poly[i][1]
tris = triangulate(poly)
sum2 = 0
for t in tris:
    a2 = cross(poly[t[0]], poly[t[1]], poly[t[2]])
    sum2 += a2
    print(f"triangle {t[0]}-{t[1]}-{t[2]}: doubled area {a2}")
print(f"{len(tris)} triangles for {len(poly)} corners")
print(f"doubled areas: triangles {sum2}, shoelace {twice}")
