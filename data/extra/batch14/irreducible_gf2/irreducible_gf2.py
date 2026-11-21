def clmul(a, b):
    r = 0
    while b > 0:
        if b & 1:
            r ^= a
        a <<= 1
        b >>= 1
    return r
def degree(p):
    return p.bit_length() - 1
def mu(n):
    m, sign, f = n, 1, 2
    while f * f <= m:
        if m % f == 0:
            m //= f
            if m % f == 0:
                return 0
            sign = -sign
        f += 1
    return -sign if m > 1 else sign
def gauss(n):
    return sum(mu(d) * (1 << (n // d)) for d in range(1, n + 1) if n % d == 0) // n
def show(p):
    terms = []
    for i in range(degree(p), -1, -1):
        if (p >> i) & 1:
            terms.append("1" if i == 0 else ("x" if i == 1 else f"x^{i}"))
    return " + ".join(terms)
top = 8
red = set()
for a in range(2, 1 << top):
    for b in range(a, 1 << top):
        if degree(a) + degree(b) <= top:
            red.add(clmul(a, b))
for n in range(1, top + 1):
    found = [p for p in range(1 << n, 1 << (n + 1)) if p not in red]
    print(f"degree {n}: {len(found):>2} irreducible, formula {gauss(n):>2}")
    if n <= 4:
        print("    " + ", ".join(show(p) for p in found))
