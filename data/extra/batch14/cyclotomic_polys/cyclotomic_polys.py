def divide(p, d):
    rem = list(p)
    q = []
    for i in range(len(p) - len(d) + 1):
        c = rem[i]
        q.append(c)
        for j in range(len(d)):
            rem[i + j] -= c * d[j]
    return q
def show(p):
    deg = len(p) - 1
    parts = []
    for i, c in enumerate(p):
        e = deg - i
        if c != 0:
            pw = "1" if e == 0 else ("x" if e == 1 else f"x^{e}")
            head = "" if abs(c) == 1 else f"{abs(c)}"
            sign = (" - " if c < 0 else " + ") if parts else ("-" if c < 0 else "")
            parts.append(f"{sign}{head}{pw}")
    return "".join(parts)
phi = {}
for n in range(1, 106):
    if n <= 12 or 105 % n == 0:
        p = [1] + [0] * (n - 1) + [-1]
        for d in range(1, n):
            if n % d == 0:
                p = divide(p, phi[d])
        phi[n] = p
for n in range(1, 13):
    print(f"Phi{n} = {show(phi[n])}")
big = phi[105]
deg = len(big) - 1
spots = [deg - i for i in range(len(big)) if abs(big[i]) > 1]
print(f"Phi105 has degree {deg} and coefficient -2 at x^k for k in [{', '.join(map(str, spots))}]")
