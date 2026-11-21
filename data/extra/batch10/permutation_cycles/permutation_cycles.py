from math import gcd

def cycles_of(perm):
    seen = [False] * len(perm)
    out = []
    for s in range(len(perm)):
        if not seen[s]:
            cyc = []
            j = s
            while not seen[j]:
                seen[j] = True
                cyc.append(j + 1)
                j = perm[j]
            out.append(cyc)
    return out

def order_by_repeats(perm):
    ident = list(range(len(perm)))
    cur = ident[:]
    k = 0
    while True:
        cur = [perm[x] for x in cur]
        k += 1
        if cur == ident:
            break
    return k

perms = [[1, 2, 0, 4, 3], [3, 0, 1, 2, 5, 6, 4, 8, 9, 7], [0, 1, 2, 3], [7, 6, 5, 4, 3, 2, 1, 0], [1, 2, 3, 4, 5, 6, 7, 8, 0, 10, 11, 9]]
for p in perms:
    cs = cycles_of(p)
    parts = []
    order = 1
    for c in cs:
        parts.append("(" + " ".join(str(x) for x in c) + ")")
        order = order // gcd(order, len(c)) * len(c)
    sign = "even" if (len(p) - len(cs)) % 2 == 0 else "odd"
    print(f"{''.join(parts)}: order {order} (repeats {order_by_repeats(p)}), {sign}")
