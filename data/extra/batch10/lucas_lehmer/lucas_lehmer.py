def lucas_lehmer(p):
    m = (1 << p) - 1
    s = 4
    for i in range(p - 2):
        s = ((s * s - 2) % m + m) % m
    return s == 0

def smallest_factor(n):
    d = 2
    while d * d <= n:
        if n % d == 0:
            return d
        d += 1
    return n

primes = []
for p in [3, 5, 7, 11, 13, 17, 19, 23, 29, 31]:
    m = (1 << p) - 1
    if lucas_lehmer(p):
        primes.append(p)
        print(f"M{p} = {m} is prime")
    else:
        f = smallest_factor(m)
        print(f"M{p} = {m} = {f} x {m // f}")
print(f"Mersenne prime exponents found: {primes}")
