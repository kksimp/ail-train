def ext_gcd(a, b):
    if b == 0:
        return [a, 1, 0]
    r = ext_gcd(b, a % b)
    return [r[0], r[2], r[1] - (a // b) * r[2]]

def solve(a, b, c):
    g = ext_gcd(a, b)
    if c % g[0] != 0:
        return None, f"no solutions: gcd {g[0]} does not divide {c}"
    step = b // g[0]
    x0 = g[1] * (c // g[0])
    x = ((x0 % step) + step) % step
    out = []
    while a * x <= c:
        out.append([x, (c - a * x) // b])
        x += step
    return out, None

for a, b, c in [[7, 11, 100], [15, 21, 300], [6, 9, 100], [12, 20, 400], [3, 5, 7]]:
    sols, err = solve(a, b, c)
    if err is None:
        text = " ".join(f"({s[0]}, {s[1]})" for s in sols) or "none"
        print(f"{a}x + {b}y = {c}: {len(sols)} non-negative: {text}")
    else:
        print(f"{a}x + {b}y = {c}: {err}")
