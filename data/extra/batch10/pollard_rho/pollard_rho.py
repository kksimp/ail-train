from math import gcd

def rho(n):
    c = 1
    while c < 50:
        x = y = 2
        d = 1
        steps = 0
        while d == 1:
            x = (x * x + c) % n
            y = (y * y + c) % n
            y = (y * y + c) % n
            d = gcd(abs(x - y), n)
            steps += 1
        if d != n:
            return [d, steps, c]
        c += 1
    return [n, 0, 0]

for n in [8051, 10403, 455459, 1022117, 1999005997, 2147483649]:
    if n % 2 == 0:
        print(f"{n} is even")
        continue
    f, s, c = rho(n)
    print(f"{n}: factor {f} x {n // f} in {s} steps (c = {c})")
