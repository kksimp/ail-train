def pow_mod(b, e, m):
    result = 1
    base = b % m
    while e > 0:
        if e % 2 == 1:
            result = result * base % m
        base = base * base % m
        e //= 2
    return result

def prime_factors(n):
    out = []
    x = n
    p = 2
    while p * p <= x:
        if x % p == 0:
            out.append(p)
            while x % p == 0:
                x //= p
        p += 1
    if x > 1:
        out.append(x)
    return out

def is_root(g, p):
    return all(pow_mod(g, (p - 1) // q, p) != 1 for q in prime_factors(p - 1))

for p in [7, 11, 13, 17, 19, 23, 41]:
    roots = [g for g in range(1, p) if is_root(g, p)]
    print(f"p = {p:>2}: smallest {roots[0]}, {len(roots)} roots {roots}")
print(f"powers of 3 mod 7: {[pow_mod(3, k, 7) for k in range(1, 7)]}")
print(f"powers of 2 mod 7: {[pow_mod(2, k, 7) for k in range(1, 7)]} (order 3, not a root)")
