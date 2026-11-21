from math import gcd
def period(a, c, m):
    first = {}
    x = 0
    step = 0
    while x not in first:
        first[x] = step
        x = (a * x + c) % m
        step += 1
    return step - first[x]
def hull_dobell(a, c, m):
    if gcd(c, m) != 1:
        return False
    rest = m
    f = 2
    while f <= rest:
        if rest % f == 0:
            if (a - 1) % f != 0:
                return False
            while rest % f == 0:
                rest //= f
        f += 1
    if m % 4 == 0 and (a - 1) % 4 != 0:
        return False
    return True
for a, c, m in [[5, 3, 16], [5, 4, 16], [3, 1, 16], [21, 7, 100], [11, 7, 100], [10, 1, 81], [13, 1, 64], [31, 7, 60], [7, 0, 101]]:
    per = period(a, c, m)
    full = hull_dobell(a, c, m)
    agree = "agrees" if full == (per == m) else "DISAGREES"
    print(f"a {a:>2} c {c} m {m:>3}: cycle {per:>3}, theorem says full {'true' if full else 'false'}: {agree}")
