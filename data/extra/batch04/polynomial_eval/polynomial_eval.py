def ev(p, x):
    a = 0
    for c in reversed(p): a = a * x + c
    return a
def add(a, b):
    n = max(len(a), len(b)); return [(a[i] if i < len(a) else 0) + (b[i] if i < len(b) else 0) for i in range(n)]
def mul(a, b):
    o = [0] * (len(a) + len(b) - 1)
    for i in range(len(a)):
        for j in range(len(b)): o[i + j] += a[i] * b[j]
    return o
def show(p):
    t = []
    for i in range(len(p) - 1, -1, -1):
        c = p[i]
        if c:
            pw = "" if i == 0 else "x" if i == 1 else f"x^{i}"
            cf = "" if c == 1 and i > 0 else str(c)
            t.append(cf + pw)
    return " + ".join(t) if t else "0"
p, q = [1, 2, 3], [-1, 0, 1]
print(f"p = {show(p)}"); print(f"q = {show(q)}"); print(f"p + q = {show(add(p, q))}"); print(f"p * q = {show(mul(p, q))}")
print(f"p(2) = {ev(p, 2)}, q(3) = {ev(q, 3)}, (p*q)(2) = {ev(mul(p, q), 2)}")
