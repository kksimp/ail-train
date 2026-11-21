def ext_gcd(a, b):
    if b == 0:
        return [a, 1, 0]
    r = ext_gcd(b, a % b)
    return [r[0], r[2], r[1] - (a // b) * r[2]]

def inverse(a, m):
    g = ext_gcd(a, m)
    if g[0] != 1:
        return None, f"{a} has no inverse mod {m} (gcd {g[0]})"
    return ((g[1] % m) + m) % m, None

for a, b in [[240, 46], [35, 64], [1001, 77], [99, 78]]:
    g = ext_gcd(a, b)
    print(f"{a}*{g[1]} + {b}*{g[2]} = {g[0]}")
row = []
for a in range(1, 11):
    v, e = inverse(a, 11)
    row.append(v if e is None else 0)
print(f"inverses mod 11 of 1..10: {row}")
for a in [3, 4, 7, 13, 15]:
    v, e = inverse(a, 26)
    if e is None:
        print(f"{a} * {v} = {a * v} = 1 mod 26")
    else:
        print(e)
