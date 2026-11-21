def sylvester(n):
    h = [[1]]
    while len(h) < n:
        h = [r + r for r in h] + [r + [-v for v in r] for r in h]
    return h
def fwht(v):
    a = list(v)
    l = 1
    while l < len(a):
        for i in range(0, len(a), 2 * l):
            for j in range(i, i + l):
                x, y = a[j], a[j + l]
                a[j], a[j + l] = x + y, x - y
        l *= 2
    return a
def fl(xs):
    return "[" + ", ".join(map(str, xs)) + "]"
h = sylvester(8)
for row in h:
    print("".join("+" if v > 0 else "-" for v in row))
ortho = True
min_diff = 8
for i in range(8):
    for j in range(8):
        dot = sum(h[i][k] * h[j][k] for k in range(8))
        diff = sum(1 for k in range(8) if h[i][k] != h[j][k])
        if dot != (8 if i == j else 0):
            ortho = False
        if i != j:
            min_diff = min(min_diff, diff)
print(f"H H^T = 8 I: {'true' if ortho else 'false'}; rows differ in at least {min_diff} places")
v = [3, 1, 4, 1, 5, 9, 2, 6]
print(f"H v = {fl([sum(h[i][k] * v[k] for k in range(8)) for i in range(8)])}")
print(f"fast Walsh transform = {fl(fwht(v))}")
