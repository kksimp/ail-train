def proj9(n):
    nn = sum(x * x for x in n)
    return [[(nn if i == j else 0) - n[i] * n[j] for j in range(3)] for i in range(3)]
def mat_vec(m, v):
    return [m[i][0] * v[0] + m[i][1] * v[1] + m[i][2] * v[2] for i in range(3)]
def fl(xs):
    return "[" + ", ".join(map(str, xs)) + "]"
n = [1, 2, 2]
nn = 9
p = proj9(n)
print(f"9 P = [{', '.join(fl(r) for r in p)}]")
pp = [[sum(p[i][k] * p[k][j] for k in range(3)) // nn for j in range(3)] for i in range(3)]
print(f"P P = P: {'true' if pp == p else 'false'}")
for x in [[9, 0, 0], [3, 3, 3], [2, -1, 0], [0, 9, -9]]:
    img = mat_vec(p, x)
    shown = [v / 9.0 for v in img]
    dot = n[0] * x[0] + n[1] * x[1] + n[2] * x[2]
    dist = abs(dot) / 3.0
    print(f"{fl(x)} -> ({', '.join(f'{v:.3f}' for v in shown)}), distance to the plane {dist:.3f}")
print(f"normal {fl(n)} -> {fl(mat_vec(p, n))}: it collapses to the origin")
