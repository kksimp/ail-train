def gcd(a, b):
    return a if b == 0 else gcd(b, a % b)

def frac(n, d):
    g = max(gcd(abs(n), abs(d)), 1)
    s = -1 if d < 0 else 1
    return ((s * n) // g, (s * d) // g)

def search(vals, exprs):
    n = len(vals)
    if n == 1:
        return exprs[0] if vals[0][0] == 24 and vals[0][1] == 1 else ""
    for i in range(n):
        for j in range(n):
            if i != j:
                rv = [vals[k] for k in range(n) if k != i and k != j]
                re = [exprs[k] for k in range(n) if k != i and k != j]
                a = vals[i]
                b = vals[j]
                ea = exprs[i]
                eb = exprs[j]
                opts = []
                texts = []
                if i < j:
                    opts.append(frac(a[0] * b[1] + b[0] * a[1], a[1] * b[1]))
                    texts.append(f"({ea}+{eb})")
                    opts.append(frac(a[0] * b[0], a[1] * b[1]))
                    texts.append(f"({ea}*{eb})")
                opts.append(frac(a[0] * b[1] - b[0] * a[1], a[1] * b[1]))
                texts.append(f"({ea}-{eb})")
                if b[0] != 0:
                    opts.append(frac(a[0] * b[1], a[1] * b[0]))
                    texts.append(f"({ea}/{eb})")
                for o in range(len(opts)):
                    found = search(rv + [opts[o]], re + [texts[o]])
                    if found != "":
                        return found
    return ""

def solve(hand):
    vals = [frac(x, 1) for x in hand]
    exprs = [f"{x}" for x in hand]
    e = search(vals, exprs)
    return "no way" if e == "" else e[1:len(e) - 1]

for hand in [[4, 7, 8, 8], [1, 5, 5, 5], [3, 3, 8, 8], [6, 6, 6, 6], [1, 1, 1, 1], [2, 3, 5, 12], [1, 3, 4, 6]]:
    print(f"{hand}: {solve(hand)}")
