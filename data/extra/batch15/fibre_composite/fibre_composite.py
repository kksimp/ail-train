def along(f, m, vf): return vf * f[1] + (1.0 - vf) * m[1]
def across(f, m, vf): return 1.0 / (vf / f[1] + (1.0 - vf) / m[1])
epoxy = ("epoxy", 3.5, 1.2)
for f in [("carbon", 230.0, 1.8), ("glass", 72.0, 2.54)]:
    print(f"{f[0]} fibre in {epoxy[0]}:")
    for vf in [0.35, 0.55, 0.65]:
        e1 = along(f, epoxy, vf)
        e2 = across(f, epoxy, vf)
        rho = vf * f[2] + (1.0 - vf) * epoxy[2]
        specific = e1 / rho
        print(f"  Vf {vf:.2f}: along {e1:>6.1f} GPa, across {e2:>5.2f} GPa, {rho:.2f} g/cm3, specific {specific:.1f}")
steel = 200.0 / 7.85
print(f"steel specific stiffness {steel:.1f}")
