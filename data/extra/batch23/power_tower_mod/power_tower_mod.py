def phi(m):
    result = m
    x = m
    p = 2
    while p * p <= x:
        if x % p == 0:
            while x % p == 0:
                x = x // p
            result = result // p * (p - 1)
        p += 1
    if x > 1:
        result = result // x * (x - 1)
    return result

def pow_mod(a, e, m):
    x = 1 % m
    base = a % m
    k = e
    while k > 0:
        if (k & 1) == 1:
            x = x * base % m
        base = base * base % m
        k = k >> 1
    return x

def capped(a, h, cap):
    v = 1
    for _ in range(h):
        r = 1
        i = 0
        while i < v and r < cap:
            r = r * a
            i += 1
        v = min(r, cap)
    return v

def tower(a, h, m):
    if m == 1:
        return 0
    if h == 0:
        return 1 % m
    p = phi(m)
    true_exp = capped(a, h - 1, p)
    e = true_exp if true_exp < p else tower(a, h - 1, p) + p
    return pow_mod(a, e, m)

print(f"3^3^3 = 7625597484987 ends {tower(3, 3, 1000000)}, 2^2^2^2 = 65536 ends {tower(2, 4, 1000)}")
for h in range(1, 9):
    print(f"{h} threes: last 8 digits {tower(3, h, 100000000):08}")
for h in range(3, 7):
    print(f"{h} twos:   last 6 digits {tower(2, h, 1000000):06}")
assert tower(3, 3, 10**13) == 7625597484987
