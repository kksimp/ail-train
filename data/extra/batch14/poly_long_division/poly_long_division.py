def show(p):
    deg = len(p) - 1
    parts = []
    for i, c in enumerate(p):
        e = deg - i
        if c != 0:
            mag = abs(c)
            pw = "" if e == 0 else ("x" if e == 1 else f"x^{e}")
            num = "" if mag == 1 and e > 0 else f"{mag}"
            sign = (" - " if c < 0 else " + ") if parts else ("-" if c < 0 else "")
            parts.append(f"{sign}{num}{pw}")
    return "".join(parts) if parts else "0"
def divide(p, d):
    rem = list(p)
    q = []
    steps = len(p) - len(d) + 1
    for i in range(steps):
        c = int(rem[i] / d[0])
        q.append(c)
        for j in range(len(d)):
            rem[i + j] -= c * d[j]
    return [q, rem[steps:]]
def mul(a, b):
    out = [0] * (len(a) + len(b) - 1)
    for i in range(len(a)):
        for j in range(len(b)):
            out[i + j] += a[i] * b[j]
    return out
for p, d in [[[1, -6, 11, -6], [1, -1]], [[2, 3, 0, -1, 5], [1, 1, -1]], [[1, 0, 0, 0, 0, -1], [1, -1]], [[3, 0, -2, 7], [1, 0, 4]]]:
    q, r = divide(p, d)
    print(f"({show(p)}) / ({show(d)})")
    back = mul(q, d)
    off = len(back) - len(r)
    for i in range(len(r)):
        back[off + i] += r[i]
    print(f"    quotient {show(q)}, remainder {show(r)}, check {'true' if back == p else 'false'}")
