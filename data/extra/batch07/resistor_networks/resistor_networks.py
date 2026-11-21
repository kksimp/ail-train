def pa(s, p):
    if s[p] in "sp":
        k = s[p]; i = p + 2; P = []
        while s[i] != ")":
            v, i = pa(s, i); P.append(v)
            if s[i] == ",": i += 1
        return (sum(P) if k == "s" else 1.0 / sum(1.0 / r for r in P)), i + 1
    j = p; n = 0
    while j < len(s) and s[j].isdigit(): n = n * 10 + int(s[j]); j += 1
    return float(n), j
for n in ["s(100,220)", "p(100,100)", "s(47,p(100,150),33)", "p(s(100,200),300)", "p(1000,1000,1000,1000)"]:
    o = pa(n, 0)[0]; print(f"{n}: {o:.2f} ohm, {12.0 / o * 1000.0:.2f} mA at 12 V")
