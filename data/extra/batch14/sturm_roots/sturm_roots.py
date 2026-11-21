def content_div(p):
    g = 0
    for c in p:
        a, b = abs(c), g
        while b != 0:
            a, b = b, a % b
        g = a
    return p if g <= 1 else [c // g for c in p]
def neg_rem(a, b):
    r = list(a)
    lb = b[0]
    sb = -1 if lb < 0 else 1
    while len(r) >= len(b):
        la = r[0]
        nx = [c * abs(lb) for c in r]
        for j in range(len(b)):
            nx[j] -= sb * la * b[j]
        r = nx[1:]
        while len(r) > 0 and r[0] == 0:
            r = r[1:]
    return content_div([-c for c in r])
def sturm(p):
    n = len(p) - 1
    d = [p[i] * (n - i) for i in range(n)]
    seq = [p, content_div(d)]
    while True:
        r = neg_rem(seq[-2], seq[-1])
        if not r:
            break
        seq.append(r)
    return seq
def sign_at_half(p, m):
    n = len(p) - 1
    t = sum(p[i] * m ** (n - i) * 2 ** i for i in range(len(p)))
    return 1 if t > 0 else (-1 if t < 0 else 0)
def changes(seq, m):
    last = 0
    count = 0
    for p in seq:
        s = sign_at_half(p, m)
        if s != 0:
            if last != 0 and s != last:
                count += 1
            last = s
    return count
polys = [("x^3 - 3x + 1", [1, 0, -3, 1]), ("x^4 - 5x^2 + 4", [1, 0, -5, 0, 4]), ("x^3 + x + 1", [1, 0, 1, 1]), ("x^5 - 5x^3 + 4x", [1, 0, -5, 0, 4, 0])]
for name, p in polys:
    seq = sturm(p)
    total = changes(seq, -5) - changes(seq, 5)
    per = []
    for k in range(-2, 3):
        n = changes(seq, 2 * k - 1) - changes(seq, 2 * k + 1)
        if n > 0:
            per.append(f"{n} near {k}")
    print(f"{name}: {len(seq)} Sturm polynomials, {total} real roots in (-2.5, 2.5]: {', '.join(per)}")
