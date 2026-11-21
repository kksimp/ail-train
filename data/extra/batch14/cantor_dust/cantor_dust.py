def intervals(n):
    ivs = [[0, 1]]
    for step in range(n):
        nx = []
        for a, b in ivs:
            a, b = a * 3, b * 3
            third = (b - a) // 3
            nx.append([a, a + third])
            nx.append([b - third, b])
        ivs = nx
    return ivs
def ternary(p, q):
    d = []
    r = p
    for i in range(8):
        r *= 3
        d.append(str(r // q))
        r %= q
    return "0." + "".join(d) + "..."
def in_cantor(p, q):
    r = p
    for i in range(40):
        r *= 3
        d = r // q
        r %= q
        if d == 1:
            return r == 0
    return True
for n in range(1, 4):
    ivs = intervals(n)
    den = 3 ** n
    shown = " ".join(f"[{a}/{den}, {b}/{den}]" for a, b in ivs)
    if n < 3:
        print(f"step {n}: {shown}")
    print(f"step {n}: {len(ivs)} pieces, length {2 ** n}/{den}")
for p, q in [[1, 4], [3, 4], [1, 3], [1, 2], [2, 3], [7, 10], [1, 10]]:
    verdict = "stays" if in_cantor(p, q) else "removed"
    print(f"{p}/{q} = {ternary(p, q)} in base 3: {verdict}")
