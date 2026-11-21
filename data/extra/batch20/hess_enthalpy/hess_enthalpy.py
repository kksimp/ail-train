def combine(parts, factors):
    terms = {}
    dh = 0.0
    for i in range(len(parts)):
        for sp, c in parts[i][0].items():
            terms[sp] = terms.get(sp, 0.0) + c * factors[i]
        dh += parts[i][1] * factors[i]
    kept = {k: v for k, v in terms.items() if v != 0.0}
    return (kept, dh)

def show(r):
    t = r[0]
    lhs = " + ".join(f"{-t[k]} {k}" for k in sorted(k for k in t if t[k] < 0.0))
    rhs = " + ".join(f"{t[k]} {k}" for k in sorted(k for k in t if t[k] > 0.0))
    return f"{lhs} -> {rhs}"

burn_c = ({"C": -1.0, "O2": -1.0, "CO2": 1.0}, -393.5)
burn_h2 = ({"H2": -1.0, "O2": -0.5, "H2O": 1.0}, -285.8)
burn_ch4 = ({"CH4": -1.0, "O2": -2.0, "CO2": 1.0, "H2O": 2.0}, -890.3)
burn_co = ({"CO": -1.0, "O2": -0.5, "CO2": 1.0}, -283.0)
methane = combine([burn_c, burn_h2, burn_ch4], [1.0, 2.0, -1.0])
print(f"methane from its elements: {show(methane)}")
print(f"  dH = {methane[1]:.1f} kJ/mol")
monoxide = combine([burn_c, burn_co], [1.0, -1.0])
print(f"carbon monoxide from carbon: {show(monoxide)}")
print(f"  dH = {monoxide[1]:.1f} kJ/mol")
