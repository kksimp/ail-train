def bi(p, q):
    out = f"{p // q}."; r = p % q; seen = {}; d = []
    while r and len(d) < 24:
        if r in seen: a = seen[r]; return f"{out}{''.join(d[:a])}({''.join(d[a:])})"
        seen[r] = len(d); r *= 2; d.append(str(r // q)); r %= q
    if not d: return str(p // q)
    return out + "".join(d)
for p, q in [(1, 2), (3, 4), (5, 8), (1, 3), (1, 5), (1, 10), (7, 3), (1, 7)]: print(f"{p}/{q} = {bi(p, q)}")
