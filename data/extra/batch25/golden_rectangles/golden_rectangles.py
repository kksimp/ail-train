import math

def squares(w, h):
    a, b = w, h
    out = []
    while b > 0:
        for i in range(a // b):
            out.append(b)
        r = a % b
        a = b
        b = r
    return out

def show(xs):
    return "[" + ", ".join(str(x) for x in xs) + "]"

phi = (1.0 + math.sqrt(5.0)) / 2.0
print(f"89 x 55 squares: {show(squares(89, 55))}")
print(f"297 x 210 squares: {show(squares(297, 210))}")
pairs = [(3, 2), (5, 3), (8, 5), (13, 8), (21, 13), (34, 21), (55, 34)]
for a, b in pairs:
    r = a / b
    print(f"{a}/{b} = {r:.6f}, off phi by {r - phi:>9.6f}")
main_col = 960.0 / phi
print(f"a 960 px page splits into {main_col:.1f} and {960.0 - main_col:.1f} px")
