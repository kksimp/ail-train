def sigma(n, k):
    x = n
    total = 1
    p = 2
    while x > 1:
        if x % p == 0:
            a = 0
            while x % p == 0:
                x //= p
                a += 1
            if k == 0:
                total *= a + 1
            else:
                total *= (p ** (k * (a + 1)) - 1) // (p ** k - 1)
        p += 1
    return total

def direct(n, k):
    return sum(d ** k for d in range(1, n + 1) if n % d == 0)

print("     n  sigma0  sigma1    sigma2  agrees")
for n in [12, 28, 60, 100, 360, 496, 945]:
    s0, s1, s2 = sigma(n, 0), sigma(n, 1), sigma(n, 2)
    ok = s0 == direct(n, 0) and s1 == direct(n, 1) and s2 == direct(n, 2)
    print(f"{n:>6} {s0:>7} {s1:>7} {s2:>9}  {str(ok).lower()}")
a = sigma(12, 1)
b = sigma(35, 1)
print(f"sigma1(12) * sigma1(35) = {a * b}, sigma1(420) = {sigma(420, 1)}")
