def ev(p, x):
    a = 0
    for c in reversed(p): a = a * x + c
    return a
def der(p): return [p[i] * i for i in range(1, len(p))]
def times(a, b):
    o = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            o[i + j] += x * y
    return o
def term(c, k):
    n = abs(c)
    body = f"{n}" if k == 0 else "x" if n == 1 else f"{n}x"
    return f"{body}^{k}" if k > 1 else body
def show(p):
    parts = []
    for i in range(len(p) - 1, -1, -1):
        c = p[i]
        if c == 0: continue
        if not parts:
            parts.append("-" + term(c, i) if c < 0 else term(c, i))
        else:
            parts.append(("-" if c < 0 else "+") + " " + term(c, i))
    return " ".join(parts) if parts else "0"
p, q = [4, -1, 3], [-2, 1]
print(f"p = {show(p)}")
print(f"q = {show(q)}")
print(f"p(2) = {ev(p, 2)}, p(-3) = {ev(p, -3)}")
print(f"p' = {show(der(p))}")
print(f"p*q = {show(times(p, q))}")
print(f"(p*q)' = {show(der(times(p, q)))}")
print(show([0, 0]))
