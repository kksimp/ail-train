import math
def gcd(a, b):
    while b: a, b = b, a % b
    return a
found = []
for m in range(2, 9):
    for n in range(1, m):
        if (m - n) % 2 == 1 and gcd(m, n) == 1:
            a0 = m * m - n * n; b0 = 2 * m * n; c = m * m + n * n
            if c <= 60: found.append([c, min(a0, b0), max(a0, b0)])
for t in sorted(found, key=lambda t: (t[0], t[1])): print(f"{t[1]}, {t[2]}, {t[0]}")
cnt = 0
for a in range(1, 60):
    for b in range(a, 60):
        c2 = a * a + b * b; c = int(math.sqrt(c2))
        if c * c == c2 and c <= 60: cnt += 1
print(f"{len(found)} primitive, {cnt} in all with hypotenuse up to 60")
