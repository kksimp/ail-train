for t in [[3, 4, 5], [2, 2, 2], [5, 5, 8], [7, 10, 5], [1, 2, 3], [0, 4, 4], [6, 6, 1]]:
    label = "-".join(map(str, t))
    s = sorted(t)
    if not (s[0] > 0 and s[0] + s[1] > s[2]):
        print(f"{label}: not a triangle")
        continue
    a, b, c = t
    k = "equilateral" if a == b == c else "isosceles" if a == b or b == c or a == c else "scalene"
    l, r = s[0] ** 2 + s[1] ** 2, s[2] ** 2
    ang = "right" if l == r else "acute" if l > r else "obtuse"
    print(f"{label}: {k}, {ang}")
