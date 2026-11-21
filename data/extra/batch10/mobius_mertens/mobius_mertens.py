def mu(n):
    x = n
    k = 0
    p = 2
    while p * p <= x:
        if x % p == 0:
            x = x // p
            if x % p == 0:
                return 0
            k += 1
        p += 1
    if x > 1:
        k += 1
    return 1 if k % 2 == 0 else -1

def divisor_sum(n):
    return sum(mu(d) for d in range(1, n + 1) if n % d == 0)

print(f"mu(1..20) = {[mu(n) for n in range(1, 21)]}")
running = 0
marks = []
zeros = 0
for n in range(1, 101):
    v = mu(n)
    running += v
    if v == 0:
        zeros += 1
    if n % 20 == 0:
        marks.append(f"M({n}) = {running}")
print(", ".join(marks))
print(f"{100 - zeros} of 1..100 are square-free")
for n in [1, 12, 30, 97, 360]:
    print(f"sum of mu(d) over divisors of {n}: {divisor_sum(n)}")
