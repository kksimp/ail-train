def cl(a, b, c):
    x, y, z = sorted([a, b, c])
    if x <= 0 or x + y <= z: return "invalid"
    s = "equilateral" if x == z else "isosceles" if x == y or y == z else "scalene"
    l = x * x + y * y; r = z * z
    return f"{s}, {'right' if l == r else 'acute' if l > r else 'obtuse'}"
for t in [(3, 4, 5), (2, 2, 2), (5, 5, 8), (1, 2, 3), (7, 8, 9), (6, 6, 1), (5, 12, 13), (0, 1, 1)]: print(f"{t[0]} {t[1]} {t[2]}: {cl(*t)}")
