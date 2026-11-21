def ca(side):
    C = {}
    for term in side.split(" + "):
        p = term.split(" "); co = int(p[0]) if len(p) == 2 else 1; f = p[-1]; i = 0
        while i < len(f):
            s = f[i]; i += 1
            if i < len(f) and f[i].islower(): s += f[i]; i += 1
            n = 0
            while i < len(f) and f[i].isdigit(): n = n * 10 + int(f[i]); i += 1
            C[s] = C.get(s, 0) + co * (1 if n == 0 else n)
    return C
for eq in ["2 H2 + O2 -> 2 H2O", "CH4 + 2 O2 -> CO2 + 2 H2O", "N2 + H2 -> 2 NH3", "C3H8 + 5 O2 -> 3 CO2 + 4 H2O", "Fe + O2 -> Fe2O3"]:
    a, b = eq.split(" -> "); L = ca(a); R = ca(b); K = list(L)
    for k in R:
        if k not in K: K.append(k)
    off = [f"{k} {L.get(k, 0)} vs {R.get(k, 0)}" for k in sorted(K) if L.get(k, 0) != R.get(k, 0)]
    print(f"{eq}: {'balanced' if not off else ', '.join(off)}")
