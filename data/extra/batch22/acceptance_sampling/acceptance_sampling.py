def accept_chance(n, c, p):
    q = 1.0 - p
    term = 1.0
    for _ in range(n):
        term *= q
    total = term
    for k in range(c):
        term = term * float(n - k) / float(k + 1) * p / q
        total += term
    return total

print("rate   n=50,c=2   n=80,c=3   outgoing")
for pct in [1, 2, 3, 4, 6, 8, 10]:
    p = float(pct) / 100.0
    a = accept_chance(50, 2, p)
    b = accept_chance(80, 3, p)
    aoq = p * a * 100.0
    print(f"{pct:>3}%   {a:>8.4f}   {b:>8.4f}   {aoq:>6.3f}%")
