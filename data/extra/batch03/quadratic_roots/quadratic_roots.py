import math
def solve(a, b, c):
    d = b * b - 4 * a * c
    if d > 0:
        s = math.sqrt(d); return f"roots {(-b + s) / (2 * a):.4f} and {(-b - s) / (2 * a):.4f}"
    if d == 0: return f"repeated root {-b / (2 * a):.4f}"
    return f"complex {-b / (2 * a):.4f} +/- {math.sqrt(-d) / (2 * a):.4f}i"
for a, b, c in [(1.0, -3.0, 2.0), (1.0, 2.0, 1.0), (1.0, 2.0, 5.0), (2.0, 5.0, -3.0), (1.0, -1.0, -1.0), (4.0, 4.0, 5.0)]:
    print(f"{a}x^2 + {b}x + {c}: {solve(a, b, c)}")
