import sys


class Err(Exception):
    pass


def parallel(a, b):
    # a*b/(a+b) rounded half up
    return (a * b * 2 + (a + b)) // (2 * (a + b))


def evaluate(s):
    pos = 0

    def skip():
        nonlocal pos
        while pos < len(s) and s[pos] == " ":
            pos += 1

    def cur():
        return s[pos] if pos < len(s) else ""

    def number():
        nonlocal pos
        skip()
        start = pos
        while cur() != "" and cur() in "0123456789":
            pos += 1
        if pos == start:
            raise Err(f"expected value at column {start + 1}")
        v = int(s[start:pos])
        if v < 1 or v > 10000000:
            raise Err(f"out of range at column {start + 1}")
        return v, 0, 1

    def expr():
        nonlocal pos
        skip()
        kind = cur()
        if kind not in ("S", "P"):
            return number()
        pos += 1
        skip()
        if cur() != "(":
            raise Err(f"expected '(' at column {pos + 1}")
        pos += 1
        items = [expr()]
        while True:
            skip()
            if cur() == ")":
                pos += 1
                break
            if cur() != ",":
                raise Err(f"expected ',' or ')' at column {pos + 1}")
            pos += 1
            items.append(expr())
        r = items[0][0]
        for it in items[1:]:
            r = r + it[0] if kind == "S" else parallel(r, it[0])
        return r, max(i[1] for i in items) + 1, sum(i[2] for i in items)

    res = expr()
    skip()
    if pos < len(s):
        raise Err(f"trailing input at column {pos + 1}")
    return res


for k, line in enumerate(sys.stdin.read().splitlines(), 1):
    if not line.strip():
        continue
    try:
        r, d, n = evaluate(line)
    except Err as e:
        print(f"line {k}: error: {e}")
        continue
    print(f"line {k}: {r // 1000}.{r % 1000:03d} ohm depth={d} leaves={n}")
