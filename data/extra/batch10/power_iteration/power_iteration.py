import math

def dot(a, b):
    s = 0.0
    for i in range(len(a)):
        s += a[i] * b[i]
    return s

def mat_vec(m, v):
    return [dot(m[i], v) for i in range(len(v))]

def normalised(v):
    n = math.sqrt(dot(v, v))
    return [x / n for x in v]

def dominant(m):
    v = normalised([1.0] * len(m))
    lam = 0.0
    steps = 0
    while steps < 500:
        w = mat_vec(m, v)
        nxt = dot(v, w)
        v = normalised(w)
        steps += 1
        if abs(nxt - lam) < 0.000000000001:
            lam = nxt
            break
        lam = nxt
    return [lam, float(steps)] + v

mats = [[[2.0, 1.0, 0.0], [1.0, 3.0, 1.0], [0.0, 1.0, 4.0]], [[4.0, 1.0, 1.0], [1.0, 4.0, 1.0], [1.0, 1.0, 4.0]], [[6.0, 2.0, 1.0], [2.0, 3.0, 1.0], [1.0, 1.0, 1.0]]]
for m in mats:
    r = dominant(m)
    print(f"eigenvalue {r[0]:.6f} after {int(r[1])} steps, vector [{r[2]:.4f}, {r[3]:.4f}, {r[4]:.4f}]")
    mv = mat_vec(m, r[2:])
    gap = 0.0
    for i in range(3):
        gap = max(gap, abs(mv[i] - r[0] * r[2 + i]))
    print(f"    |Av - lambda v| below 1e-5: {str(gap < 0.00001).lower()}")
