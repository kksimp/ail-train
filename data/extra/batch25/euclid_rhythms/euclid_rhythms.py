def pattern(k, n):
    return "".join("x" if i * k % n < k else "." for i in range(n))

def gaps(p):
    hits = [i for i, c in enumerate(p) if c == 'x']
    out = []
    for j in range(len(hits)):
        nxt = hits[j + 1] if j + 1 < len(hits) else hits[0] + len(p)
        out.append(nxt - hits[j])
    return out

named = [(3, 8, "tresillo"), (5, 8, "cinquillo"), (2, 5, "khafif-e-ramal"), (3, 7, "ruchenitza"), (4, 9, "aksak"), (5, 12, "venda clapping"), (7, 12, "bembe bell"), (7, 16, "samba"), (9, 16, "rumba variant")]
for k, n, name in named:
    p = pattern(k, n)
    g = gaps(p)
    even = max(g) - min(g) <= 1
    shown = "[" + ", ".join(str(x) for x in g) + "]"
    print(f"E({k},{n:>2}) {p:<16} {shown} {name}{'' if even else ' (uneven)'}")
