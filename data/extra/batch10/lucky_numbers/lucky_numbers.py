def lucky(limit):
    xs = [n for n in range(1, limit + 1) if n % 2 == 1]
    i = 1
    while i < len(xs) and xs[i] <= len(xs):
        k = xs[i]
        xs = [v for j, v in enumerate(xs) if (j + 1) % k != 0]
        i += 1
    return xs

def is_prime(n):
    if n < 2:
        return False
    d = 2
    while d * d <= n:
        if n % d == 0:
            return False
        d += 1
    return True

small = lucky(200)
print(f"lucky numbers to 200: {small}")
big = lucky(10000)
primes = [n for n in range(2, 10001) if is_prime(n)]
both = [n for n in big if is_prime(n)]
print(f"below 10000: {len(big)} lucky, {len(primes)} prime, {len(both)} both")
print(f"first lucky primes: {both[:10]}")
twins = len([i for i in range(1, len(big)) if big[i] - big[i - 1] == 2])
print(f"lucky pairs two apart: {twins}")
