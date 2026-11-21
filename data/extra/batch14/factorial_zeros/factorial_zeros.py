def legendre(n, p):
    t, q = 0, p
    while q <= n:
        t += n // q
        q *= p
    return t
print("     n  2s in n!  3s in n!  5s in n!  zeros base 10  zeros base 12")
for n in [10, 25, 100, 1000, 2026]:
    twos, threes, fives = legendre(n, 2), legendre(n, 3), legendre(n, 5)
    b12 = min(twos // 2, threes)
    print(f"{n:>6} {twos:>9} {threes:>9} {fives:>9} {min(fives, twos):>14} {b12:>14}")
f = 1
for i in range(1, 21):
    f *= i
zeros = 0
x = f
while x % 10 == 0:
    zeros += 1
    x //= 10
print(f"20! = {f} ends in {zeros} zeros, formula {legendre(20, 5)}")
