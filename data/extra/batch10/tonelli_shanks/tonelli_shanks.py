def pow_mod(b, e, m):
    result = 1
    base = b % m
    while e > 0:
        if e % 2 == 1:
            result = result * base % m
        base = base * base % m
        e //= 2
    return result

def sqrt_mod(n, p):
    a = n % p
    if a == 0:
        return 0
    if pow_mod(a, (p - 1) // 2, p) != 1:
        return None
    q, s = p - 1, 0
    while q % 2 == 0:
        q //= 2
        s += 1
    z = 2
    while pow_mod(z, (p - 1) // 2, p) != p - 1:
        z += 1
    m, c, t, r = s, pow_mod(z, q, p), pow_mod(a, q, p), pow_mod(a, (q + 1) // 2, p)
    while t != 1:
        i = 0
        t2 = t
        while t2 != 1:
            t2 = t2 * t2 % p
            i += 1
        b = pow_mod(c, 1 << (m - i - 1), p)
        m = i
        c = b * b % p
        t = t * c % p
        r = r * b % p
    return r

for n, p in [[10, 13], [2, 17], [5, 41], [3, 41], [99, 113], [1000, 1000003], [123456, 1000003]]:
    r = sqrt_mod(n, p)
    if r is not None:
        lo = r if r < p - r else p - r
        print(f"x^2 = {n} mod {p}: x = {lo} or {p - lo}, check {lo * lo % p}")
    else:
        print(f"x^2 = {n} mod {p}: no root, {n} is not a square mod {p}")
