import math

def sub(a, b):
    return (a[0] - b[0], a[1] - b[1], a[2] - b[2])

def cross(a, b):
    return (a[1] * b[2] - a[2] * b[1], a[2] * b[0] - a[0] * b[2], a[0] * b[1] - a[1] * b[0])

def dot(a, b):
    return a[0] * b[0] + a[1] * b[1] + a[2] * b[2]

def six_volume(p):
    return dot(sub(p[1], p[0]), cross(sub(p[2], p[0]), sub(p[3], p[0])))

solids = [[(0, 0, 0), (1, 0, 0), (0, 1, 0), (0, 0, 1)], [(1, 2, 3), (4, 0, 1), (2, 5, 0), (3, 3, 6)], [(0, 0, 0), (2, 2, 2), (1, 3, 5), (3, 1, -1)], [(2, 0, 0), (0, 3, 0), (0, 0, 4), (0, 0, 0)]]
for i, p in enumerate(solids):
    six = six_volume(p)
    vol = float(abs(six)) / 6.0
    note = "coplanar" if six == 0 else ("right-handed" if six > 0 else "left-handed")
    print(f"solid {i + 1}: triple product {six}, volume {vol:.4f} ({note})")
n = cross((1, 2, 3), (4, 5, 6))
area = math.sqrt(float(dot(n, n))) / 2.0
print(f"triangle (0,0,0) (1,2,3) (4,5,6): normal {n[0]} {n[1]} {n[2]}, area {area:.4f}")
