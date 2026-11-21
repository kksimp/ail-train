T = {"H": 1.008, "C": 12.011, "N": 14.007, "O": 15.999, "Na": 22.99, "Cl": 35.45, "Ca": 40.078, "S": 32.06}
def ms(f):
    t = 0.0; g = 0.0; ig = False; i = 0
    while i < len(f):
        c = f[i]
        if c == "(": ig = True; g = 0.0; i += 1; continue
        if c == ")": ig = False; a = g; i += 1
        else:
            s = c; i += 1
            if i < len(f) and f[i].islower(): s += f[i]; i += 1
            a = T.get(s, 0.0)
        n = 0
        while i < len(f) and f[i].isdigit(): n = n * 10 + int(f[i]); i += 1
        k = 1 if n == 0 else n
        if ig: g += a * k
        else: t += a * k
    return t
for f in ["H2O", "CO2", "NaCl", "C6H12O6", "Ca(OH)2", "H2SO4", "(NH4)2SO4"]: print(f"{f}: {ms(f):.3f} g/mol")
