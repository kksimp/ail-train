import math

def isqrt(v):
    y = int(math.sqrt(float(v)))
    while (y + 1) * (y + 1) <= v:
        y += 1
    while y * y > v:
        y -= 1
    return y

def lattice_count(r):
    return sum(2 * isqrt(r * r - x * x) + 1 for x in range(-r, r + 1))

pi = 3.141592653589793
print("radius   points        area    error  error/r")
for r in [1, 2, 5, 10, 20, 50, 100, 300]:
    n = lattice_count(r)
    rf = float(r)
    area = pi * rf * rf
    err = float(n) - area
    print(f"{r:>6} {n:>8} {area:>11.2f} {err:>8.2f} {err / rf:>8.3f}")
