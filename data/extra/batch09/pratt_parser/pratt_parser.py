def power(a, b):
    r = 1
    for i in range(b):
        r *= a
    return r

def tokens(s):
    return [t for t in s.replace("(", " ( ").replace(")", " ) ").split(" ") if t != ""]

def bp(op):
    return {"+": 10, "-": 10, "*": 20, "/": 20, "^": 30}.get(op, 0)

def parse(toks, pos, min_bp):
    t = toks[pos[0]]
    pos[0] += 1
    left = (t, int(t) if t.isdigit() else 0)
    if t == "-":
        inner = parse(toks, pos, 25)
        left = (f"(-{inner[0]})", -inner[1])
    elif t == "(":
        left = parse(toks, pos, 0)
        pos[0] += 1
    while pos[0] < len(toks):
        op = toks[pos[0]]
        p = bp(op)
        if p == 0 or p <= min_bp:
            break
        pos[0] += 1
        next_min = p - 1 if op == "^" else p
        right = parse(toks, pos, next_min)
        a, b = left[1], right[1]
        if op == "+":
            value = a + b
        elif op == "-":
            value = a - b
        elif op == "*":
            value = a * b
        elif op == "/":
            value = a // b
        else:
            value = power(a, b)
        left = (f"({left[0]} {op} {right[0]})", value)
    return left

for src in ["1 + 2 * 3", "(1 + 2) * 3", "2 ^ 3 ^ 2", "- 2 ^ 2", "10 - 4 - 3", "64 / 4 / 2", "2 * (3 + 4) ^ 2 - 1"]:
    r = parse(tokens(src), [0], 0)
    print(f"{src:<20} {r[0]:<28} = {r[1]}")
