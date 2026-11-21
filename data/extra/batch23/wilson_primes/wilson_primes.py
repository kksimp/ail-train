def fact_mod(k, m):
    acc = 1 % m
    for i in range(2, k + 1):
        acc = acc * i % m
    return acc

def is_prime(n):
    return n > 1 and fact_mod(n - 1, n) == n - 1

primes = [n for n in range(2, 40) if is_prime(n)]
print(f"primes below 40 by Wilson: {primes}")
for n in [4, 6, 8, 9, 12, 25]:
    k = n - 1
    print(f"{k}! mod {n} = {fact_mod(k, n)}")
special = []
for p in range(2, 600):
    if is_prime(p):
        sq = p * p
        if fact_mod(p - 1, sq) == sq - 1:
            special.append(p)
print(f"Wilson primes below 600: {special}")
