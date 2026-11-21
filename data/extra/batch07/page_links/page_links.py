def ba(c, l):
    P = []; pv = 0
    for p in range(1, l + 1):
        if not (p == 1 or p == l or c - 2 <= p <= c + 2): continue
        if p - pv > 1: P.append("...")
        P.append(f"[{p}]" if p == c else str(p)); pv = p
    return " ".join(P)
for c, l in [(1, 1), (1, 5), (3, 9), (6, 20), (19, 20), (10, 10), (4, 7)]: print(f"page {c} of {l}: {ba(c, l)}")
