def pow_mod(b, e, m):
    result = 1
    base = b % m
    while e > 0:
        if e % 2 == 1:
            result = result * base % m
        base = base * base % m
        e //= 2
    return result

def passes(n, a):
    d = n - 1
    s = 0
    while d % 2 == 0:
        d //= 2
        s += 1
    x = pow_mod(a, d, n)
    if x == 1 or x == n - 1:
        return True
    for r in range(1, s):
        x = x * x % n
        if x == n - 1:
            return True
    return False

def trial_prime(n):
    p = 2
    while p * p <= n:
        if n % p == 0:
            return False
        p += 1
    return n > 1

bases = [2, 3, 5, 7]
for n in [97, 561, 2047, 7919, 1373653, 25326001, 1000000007, 2147483647]:
    fooled = [a for a in bases if passes(n, a)]
    verdict = "prime" if len(fooled) == 4 else "composite"
    print(f"{n:>10}: passes bases {fooled}, says {verdict}, trial division {str(trial_prime(n)).lower()}")
