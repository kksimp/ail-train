from math import gcd

def phi(n):
    return len([i for i in range(1, n + 1) if gcd(i, n) == 1])

def burnside(n, k):
    total = 0
    for d in range(1, n + 1):
        if n % d == 0:
            total += phi(d) * k ** (n // d)
    return total // n

def brute(n, k):
    seen = set()
    for code in range(k ** n):
        digits = []
        x = code
        for i in range(n):
            digits.append(x % k)
            x //= k
        best = -1
        for r in range(n):
            v = 0
            for i in range(n):
                v = v * k + digits[(i + r) % n]
            if best < 0 or v < best:
                best = v
        seen.add(best)
    return len(seen)

for k in [2, 3]:
    for n in range(1, 9):
        if k == 3 and n > 6:
            continue
        print(f"{n} beads, {k} colours: Burnside {burnside(n, k):>4}, brute force {brute(n, k):>4}")
