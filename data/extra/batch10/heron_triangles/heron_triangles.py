import math

def isqrt(v):
    y = int(math.sqrt(float(v)))
    while (y + 1) * (y + 1) <= v:
        y += 1
    while y * y > v:
        y -= 1
    return y

def area(a, b, c):
    p = (a + b + c) * (-a + b + c) * (a - b + c) * (a + b - c)
    if p <= 0:
        return None
    r = isqrt(p)
    if r * r != p or r % 4 != 0:
        return None
    return r // 4

found = []
for c in range(1, 31):
    for b in range(1, c + 1):
        for a in range(1, b + 1):
            ar = area(a, b, c)
            if ar is not None:
                found.append([a, b, c, ar])
by_perimeter = sorted(found, key=lambda t: (t[0] + t[1] + t[2], t[2]))
print(f"{len(found)} Heronian triangles with sides up to 30; smallest perimeters:")
for t in by_perimeter[:8]:
    right = " (right)" if t[0] * t[0] + t[1] * t[1] == t[2] * t[2] else ""
    print(f"    {t[0]}, {t[1]}, {t[2]}: perimeter {t[0] + t[1] + t[2]}, area {t[3]}{right}")
same = [t for t in found if t[3] == t[0] + t[1] + t[2]]
print(f"area equal to perimeter: {[t[:3] for t in same]}")
