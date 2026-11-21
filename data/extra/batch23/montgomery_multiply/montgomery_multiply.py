R = 65536

def neg_inverse(n):
    inv = 1
    for _ in range(5):
        t = (n * inv) % R
        inv = (inv * ((R + 2 - t) % R)) % R
    return (R - inv) % R

def redc(t, n, np):
    m = ((t % R) * np) % R
    u = (t + m * n) // R
    return u - n if u >= n else u

def mont_pow(a, e, n, np):
    x = R % n
    base = (a * R) % n
    k = e
    while k > 0:
        if (k & 1) == 1:
            x = redc(x * base, n, np)
        base = redc(base * base, n, np)
        k = k >> 1
    return redc(x, n, np)

def plain_pow(a, e, n):
    x = 1
    base = a % n
    k = e
    while k > 0:
        if (k & 1) == 1:
            x = x * base % n
        base = base * base % n
        k = k >> 1
    return x

for n in [3329, 40961, 65521]:
    np = neg_inverse(n)
    check = (n * np) % R
    print(f"n = {n}: n' = {np}, n * n' mod R = {check}")
    for a in [3, 12345]:
        e = n - 2
        print(f"  {a}^{e}: Montgomery {mont_pow(a, e, n, np)}, plain {plain_pow(a, e, n)}")
