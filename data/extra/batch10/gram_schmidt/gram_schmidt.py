import math

def dot(a, b):
    return a[0] * b[0] + a[1] * b[1] + a[2] * b[2]

def orthonormal(vs):
    basis = []
    for v in vs:
        w = v[:]
        for e in basis:
            p = dot(v, e)
            for i in range(3):
                w[i] -= p * e[i]
        n = math.sqrt(dot(w, w))
        basis.append([x / n for x in w])
    return basis

def show(v):
    return f"[{v[0]:>7.4f}, {v[1]:>7.4f}, {v[2]:>7.4f}]"

vs = [[3.0, 1.0, 2.0], [1.0, 2.0, 1.0], [2.0, 1.0, 4.0]]
basis = orthonormal(vs)
for i in range(3):
    print(f"v{i + 1} = {show(vs[i])} -> e{i + 1} = {show(basis[i])}")
worst = 0.0
for i in range(3):
    for j in range(3):
        target = 1.0 if i == j else 0.0
        off = abs(dot(basis[i], basis[j]) - target)
        if off > worst:
            worst = off
print(f"all dot products within 1e-12 of the identity: {str(worst < 0.000000000001).lower()}")
w = [1.0, 5.0, -2.0]
coords = [dot(w, e) for e in basis]
back = [0.0, 0.0, 0.0]
for k in range(3):
    for i in range(3):
        back[i] += coords[k] * basis[k][i]
print(f"[1, 5, -2] in the new basis: {show(coords)}, rebuilt {show(back)}")
