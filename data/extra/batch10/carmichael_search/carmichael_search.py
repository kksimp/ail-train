def factors(n):
    out = []
    x = n
    p = 2
    while p * p <= x:
        while x % p == 0:
            out.append(p)
            x //= p
        p += 1
    if x > 1:
        out.append(x)
    return out

def korselt(n):
    fs = factors(n)
    if len(fs) < 2:
        return False
    for i in range(1, len(fs)):
        if fs[i] == fs[i - 1]:
            return False
    return all((n - 1) % (p - 1) == 0 for p in fs)

def pow_mod(b, e, m):
    result = 1
    base = b % m
    while e > 0:
        if e % 2 == 1:
            result = result * base % m
        base = base * base % m
        e //= 2
    return result

found = []
for n in range(3, 20000):
    if korselt(n):
        found.append(n)
        print(f"{n:>5} = {' x '.join(str(f) for f in factors(n))}")
print(f"{len(found)} Carmichael numbers below 20000")
from math import gcd
coprime = 0
fooled = 0
for a in range(2, 561):
    if gcd(a, 561) == 1:
        coprime += 1
        if pow_mod(a, 560, 561) == 1:
            fooled += 1
print(f"561: {fooled} of {coprime} coprime bases give a^560 = 1 (mod 561)")
