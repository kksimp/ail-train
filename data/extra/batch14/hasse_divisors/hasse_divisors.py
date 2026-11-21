def omega(n):
    m, k, f = n, 0, 2
    while m > 1:
        while m % f == 0:
            m //= f
            k += 1
        f += 1
    return k
def is_prime(n):
    if n < 2:
        return False
    f = 2
    while f * f <= n:
        if n % f == 0:
            return False
        f += 1
    return True
def chains(a, top, divs):
    if a == top:
        return 1
    return sum(chains(b, top, divs) for b in divs if b % a == 0 and is_prime(b // a))
n = 60
divs = [d for d in range(1, n + 1) if n % d == 0]
rank = omega(n)
widest = 0
for r in range(rank + 1):
    level = [d for d in divs if omega(d) == r]
    widest = max(widest, len(level))
    print(f"rank {r}: [{', '.join(map(str, level))}]")
covers = [f"{a}-{b}" for a in divs for b in divs if b % a == 0 and is_prime(b // a)]
print(f"{len(covers)} covering pairs, e.g. {', '.join(covers[:6])}")
print(f"maximal chains from 1 to 60: {chains(1, n, divs)}; largest rank level: {widest}")
