def pow_mod(b, e, m):
    result = 1
    base = b % m
    while e > 0:
        if e % 2 == 1:
            result = result * base % m
        base = base * base % m
        e //= 2
    return result

def inverse(a, m):
    t, new_t, r, new_r = 0, 1, m, a
    while new_r != 0:
        q = r // new_r
        t, new_t = new_t, t - q * new_t
        r, new_r = new_r, r - q * new_r
    return ((t % m) + m) % m

def make(p, q, e):
    phi = (p - 1) * (q - 1)
    return (p * q, e, inverse(e, phi))

n, e, d = make(61, 53, 17)
print(f"public (n {n}, e {e}), private d {d}")
letters = [((ord(c) - 65) % 26 + 26) % 26 for c in "MATHS!"]
blocks = []
i = 0
while i + 1 < len(letters):
    blocks.append(letters[i] * 26 + letters[i + 1])
    i += 2
locked = [pow_mod(b, e, n) for b in blocks]
opened = [pow_mod(c, d, n) for c in locked]
print(f"blocks {blocks} -> cipher {locked} -> {opened}")
bn, be, bd = make(1009, 1013, 65537)
for m in [42, 123456, 1000000]:
    c = pow_mod(m, be, bn)
    print(f"n {bn}: {m} -> {c} -> {pow_mod(c, bd, bn)}")
