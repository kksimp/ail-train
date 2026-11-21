import math
def sv(a, b, c):
    d = b * b - 4 * a * c
    if d > 0: r = math.sqrt(d); return f"two roots {(-b + r) / (2 * a):.3f} and {(-b - r) / (2 * a):.3f}"
    if d == 0: return f"one root {-b / (2 * a):.3f}"
    return f"complex {-b / (2 * a):.3f} +/- {math.sqrt(-d) / (2 * a):.3f}i"
for q in [(1.0, -3.0, 2.0), (1.0, 2.0, 1.0), (1.0, 2.0, 5.0), (2.0, -7.0, 3.0), (1.0, 1.0, -1.0), (3.0, 2.0, 5.0)]: print(f"{q[0]}x^2 + {q[1]}x + {q[2]}: {sv(*q)}")
