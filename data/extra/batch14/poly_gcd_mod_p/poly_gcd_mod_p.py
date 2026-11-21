def trim(p):
    i = 0
    while i < len(p) - 1 and p[i] == 0:
        i += 1
    return p[i:]
def rem(a, b, m):
    r = list(a)
    inv = pow(b[0], m - 2, m)
    while len(r) >= len(b) and not (len(r) == 1 and r[0] == 0):
        c = r[0] * inv % m
        for j in range(len(b)):
            r[j] = ((r[j] - c * b[j]) % m + m) % m
        r = trim(r)
        if len(r) == 1 and r[0] == 0:
            break
    return r
def from_roots(roots, m):
    p = [1]
    for r in roots:
        nx = [0] * (len(p) + 1)
        for i in range(len(p)):
            nx[i] = (nx[i] + p[i]) % m
            nx[i + 1] = ((nx[i + 1] - r * p[i]) % m + m) % m
        p = nx
    return p
def show(p):
    deg = len(p) - 1
    parts = []
    for i, c in enumerate(p):
        e = deg - i
        if c != 0:
            num = "" if c == 1 and e > 0 else f"{c}"
            pw = "" if e == 0 else ("x" if e == 1 else f"x^{e}")
            parts.append(f"{num}{pw}")
    return " + ".join(parts) if parts else "0"
m = 7
f = from_roots([1, 2, 4], m)
g = from_roots([2, 4, 6], m)
print(f"f = {show(f)}  (roots 1, 2, 4)")
print(f"g = {show(g)}  (roots 2, 4, 6)")
a, b = f, g
while not (len(b) == 1 and b[0] == 0):
    r = rem(a, b, m)
    print(f"    {show(a)} mod {show(b)} = {show(r)}")
    a, b = b, r
inv = pow(a[0], m - 2, m)
monic = [c * inv % m for c in a]
roots = [x for x in range(m) if rem(monic, from_roots([x], m), m) == [0]]
print(f"gcd = {show(monic)}, roots [{', '.join(map(str, roots))}]")
