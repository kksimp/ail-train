def gmul(a, b):
    x, y, r = a, b, 0
    while y > 0:
        if y & 1:
            r ^= x
        x <<= 1
        if x & 256:
            x ^= 283
        y >>= 1
    return r
def gpow(a, e):
    r = 1
    for _ in range(e):
        r = gmul(r, a)
    return r
for a, b in [[87, 131], [87, 19], [2, 135], [83, 202]]:
    r = gmul(a, b)
    print(f"{a:02x} * {b:02x} = {r:02x}, while {a:02x} + {b:02x} = {a ^ b:02x}")
for a in [1, 2, 3, 83, 149]:
    inv = gpow(a, 254)
    print(f"inverse of {a:02x} is {inv:02x}, product {gmul(a, inv):02x}")
seen = set()
x = 1
for i in range(255):
    seen.add(x)
    x = gmul(x, 3)
print(f"powers of 03 reach {len(seen)} non-zero bytes")
