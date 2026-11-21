def pow_mod(b, e, m):
    result = 1
    base = b % m
    while e > 0:
        if e % 2 == 1:
            result = result * base % m
        base = base * base % m
        e //= 2
    return result

def bsgs(g, h, p):
    m = 1
    while m * m < p:
        m += 1
    baby = {}
    v = 1
    for j in range(m):
        if v not in baby:
            baby[v] = j
        v = v * g % p
    giant = pow_mod(g, p - 1 - m, p)
    y = h % p
    for i in range(m):
        if y in baby:
            return i * m + baby[y]
        y = y * giant % p
    return None

for g, h, p in [[3, 13, 17], [2, 1000, 1019], [5, 123456, 1000003], [2, 7, 7919], [4, 3, 7]]:
    x = bsgs(g, h, p)
    if x is not None:
        print(f"{g}^x = {h} mod {p}: x = {x}, check {pow_mod(g, x, p)}")
    else:
        print(f"{g}^x = {h} mod {p}: no solution")
