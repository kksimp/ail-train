from math import gcd
def frac(n, d):
    g = gcd(n, d)
    s = -1 if d < 0 else 1
    num, den = s * n // g, d * s // g
    return f"{num}" if den == 1 else f"{num}/{den}"
def solve(name, a, b):
    pn = b[1][1] - b[1][0]
    pd = b[0][0] - b[1][0] - b[0][1] + b[1][1]
    qn = a[1][1] - a[0][1]
    qd = a[0][0] - a[0][1] - a[1][0] + a[1][1]
    rv = qn * a[0][0] + (qd - qn) * a[0][1]
    cv = pn * b[0][0] + (pd - pn) * b[1][0]
    print(f"{name}: row plays first move with chance {frac(pn, pd)}, column with {frac(qn, qd)}")
    print(f"    row expects {frac(rv, qd)}, column expects {frac(cv, pd)}")
solve("matching pennies", [[1, -1], [-1, 1]], [[-1, 1], [1, -1]])
solve("concert or match", [[2, 0], [0, 1]], [[1, 0], [0, 2]])
kick = [[58, 95], [93, 70]]
solve("penalty kick (% scored)", kick, [[-v for v in r] for r in kick])
solve("hawk or dove", [[-1, 4], [0, 2]], [[-1, 0], [4, 2]])
