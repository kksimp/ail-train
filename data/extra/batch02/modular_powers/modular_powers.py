def ip(n):
    if n < 2: return False
    d = 2
    while d * d <= n:
        if n % d == 0: return False
        d += 1
    return True
b = lambda x: str(x).lower()
print(f"last 4 digits of 7^1000: {pow(7, 1000, 10000):04d}")
print(f"2^100 mod 1000007: {pow(2, 100, 1000007)}")
print(f"3^0 mod 5: {pow(3, 0, 5)}")
for n in [97, 561, 1105, 1009, 341, 91]:
    f = n == 2 or pow(2, n - 1, n) == 1
    print(f"{n}: fermat {b(f)}, really {b(ip(n))}")
