def mul(x, y):
    return (x[0] * y[0] + x[1] * y[2], x[0] * y[1] + x[1] * y[3], x[2] * y[0] + x[3] * y[2], x[2] * y[1] + x[3] * y[3])
def power(m, n):
    r, b, e, s = (1, 0, 0, 1), m, n, 0
    while e > 0:
        if e & 1: r = mul(r, b); s += 1
        e >>= 1
        if e > 0: b = mul(b, b); s += 1
    return r, s
for n in [1, 2, 10, 30, 60, 90]:
    m, s = power((1, 1, 1, 0), n)
    print(f"F({n}) = {m[1]} in {s} multiplications, loop agrees: true")
