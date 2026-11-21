def expand(roots):
    p = [1]
    for r in roots:
        nx = p + [0]
        for i in range(len(p)):
            nx[i + 1] -= r * p[i]
        p = nx
    return p
def show(p):
    deg = len(p) - 1
    parts = []
    for i, c in enumerate(p):
        e = deg - i
        if c != 0:
            pw = "" if e == 0 else ("x" if e == 1 else f"x^{e}")
            num = "" if abs(c) == 1 and e > 0 else f"{abs(c)}"
            sign = (" - " if c < 0 else " + ") if parts else ("-" if c < 0 else "")
            parts.append(f"{sign}{num}{pw}")
    return "".join(parts)
for roots in [[1, 2, 3, 4], [2, -3, 5], [-1, -1, 2, 6, 0]]:
    p = expand(roots)
    es = []
    for k in range(1, len(p)):
        sign = 1 if k % 2 == 0 else -1
        es.append(f"e{k} = {sign * p[k]}")
    print(f"roots [{', '.join(map(str, roots))}]: {show(p)}")
    print("    " + ", ".join(es))
total, product = 13, 40
disc = total * total - 4 * product
s = 0
while s * s < disc:
    s += 1
print(f"sum {total}, product {product}: x^2 - {total}x + {product} = 0 gives {(total - s) // 2} and {(total + s) // 2}")
