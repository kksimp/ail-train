def log2(n):
    k = 0
    while (1 << k) < n:
        k += 1
    return k

def is_pow2(n):
    return n > 0 and (n & (n - 1)) == 0

def low_bit(n):
    k = 0
    while (n >> k) & 1 == 0:
        k += 1
    return k

def plan(op, c):
    if op == "*" and is_pow2(c):
        return [1, log2(c), 0]
    if op == "*" and is_pow2(c - (1 << low_bit(c))):
        lo = low_bit(c)
        return [2, log2(c - (1 << lo)), lo]
    if op == "*" and is_pow2(c + 1):
        return [3, log2(c + 1), 0]
    if op == "/" and is_pow2(c):
        return [4, log2(c), 0]
    if op == "%" and is_pow2(c):
        return [5, c - 1, 0]
    return [0, 0, 0]

def text(p, op, c):
    k = p[0]
    if k == 1: return f"y << {p[1]}"
    if k == 2: return f"(y << {p[1]}) + (y << {p[2]})"
    if k == 3: return f"(y << {p[1]}) - y"
    if k == 4: return f"y >> {p[1]}"
    if k == 5: return f"y & {p[1]}"
    return f"y {op} {c}"

def direct_of(op, c, y):
    if op == "*": return y * c
    if op == "/": return y // c
    return y % c

def run(p, op, c, y):
    k = p[0]
    if k == 1: return y << p[1]
    if k == 2: return (y << p[1]) + (y << p[2])
    if k == 3: return (y << p[1]) - y
    if k == 4: return y >> p[1]
    if k == 5: return y & p[1]
    return direct_of(op, c, y)

cases = [("*", 8), ("*", 2), ("/", 4), ("%", 16), ("*", 10), ("*", 7), ("*", 12), ("*", 11)]
for op, c in cases:
    p = plan(op, c)
    ok = True
    for y in [37, 1000, 4095]:
        if run(p, op, c, y) != direct_of(op, c, y):
            ok = False
    verdict = "agrees" if ok else "differs"
    print(f"y {op} {c:<3} -> {text(p, op, c):<22} 37 gives {run(p, op, c, 37):>4}, {verdict}")
