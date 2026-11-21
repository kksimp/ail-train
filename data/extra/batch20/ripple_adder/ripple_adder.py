def full_add(a, b, cin):
    s = (a ^ b) ^ cin
    cout = (a & b) | (cin & (a ^ b))
    return [s, cout]

def add8(x, y):
    carry = 0
    total = 0
    last_in = 0
    for i in range(8):
        a = (x >> i) & 1
        b = (y >> i) & 1
        if i == 7:
            last_in = carry
        r = full_add(a, b, carry)
        total = total | (r[0] << i)
        carry = r[1]
    return [total, carry, carry ^ last_in]

def bits(n):
    return format(n, "b").rjust(8, "0")

def signed(n):
    return n - 256 if n >= 128 else n

for x, y in [(100, 55), (200, 100), (156, 206), (100, 50), (255, 1)]:
    r = add8(x, y)
    print(f"{bits(x)} + {bits(y)} = {bits(r[0])} carry {r[1]} overflow {r[2]}")
    print(f"  unsigned {x} + {y} -> {r[0]}, signed {signed(x)} + {signed(y)} -> {signed(r[0])}")
