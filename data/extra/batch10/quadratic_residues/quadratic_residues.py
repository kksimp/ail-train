def pow_mod(b, e, m):
    result = 1
    base = b % m
    while e > 0:
        if e % 2 == 1:
            result = result * base % m
        base = base * base % m
        e //= 2
    return result

def legendre(a, p):
    r = pow_mod(((a % p) + p) % p, (p - 1) // 2, p)
    return -1 if r == p - 1 else r

for p in [7, 11, 13, 17, 23, 29]:
    res = sorted({x * x % p for x in range(1, p)})
    minus = legendre(-1, p)
    two = legendre(2, p)
    rule_minus = 1 if p % 4 == 1 else -1
    rule_two = 1 if p % 8 == 1 or p % 8 == 7 else -1
    ok = minus == rule_minus and two == rule_two
    print(f"p = {p:>2}: residues {res}")
    print(f"        (-1|p) = {minus}, (2|p) = {two}, rules agree: {str(ok).lower()}")
