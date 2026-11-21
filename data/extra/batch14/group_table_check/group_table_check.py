def op(kind, a, b, m):
    if kind == 0:
        return (a + b) % m
    if kind == 1:
        return (a * b) % m
    if kind == 2:
        return (a - b + m) % m
    return a ^ b
def b(v):
    return "true" if v else "false"
def check(name, xs, kind, m):
    n = len(xs)
    t = []
    for a in xs:
        row = []
        for c in xs:
            r = op(kind, a, c, m)
            if r not in xs:
                return f"{name}: not closed ({a}, {c} gives {r})"
            row.append(xs.index(r))
        t.append(row)
    e = -1
    for i in range(n):
        if len([j for j in range(n) if t[i][j] == j and t[j][i] == j]) == n:
            e = i
    if e < 0:
        return f"{name}: closed, no identity"
    inv = all(any(t[i][j] == e and t[j][i] == e for j in range(n)) for i in range(n))
    assoc = all(t[t[a][c]][d] == t[a][t[c][d]] for a in range(n) for c in range(n) for d in range(n))
    comm = all(t[a][c] == t[c][a] for a in range(n) for c in range(n))
    verdict = "a group" if inv and assoc else "not a group"
    return f"{name}: identity {xs[e]}, inverses {b(inv)}, associative {b(assoc)}, commutative {b(comm)}: {verdict}"
print(check("Z4 under +", [0, 1, 2, 3], 0, 4))
print(check("1..4 times mod 5", [1, 2, 3, 4], 1, 5))
print(check("1..5 times mod 6", [1, 2, 3, 4, 5], 1, 6))
print(check("1,3,5,7 times mod 8", [1, 3, 5, 7], 1, 8))
print(check("0..3 under xor", [0, 1, 2, 3], 3, 0))
print(check("0..2 minus mod 3", [0, 1, 2], 2, 3))
print(check("0..4 times mod 5", [0, 1, 2, 3, 4], 1, 5))
