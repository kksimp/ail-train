def bias(r1, r2, rc, re, beta):
    vcc = 12.0
    vbb = vcc * r2 / (r1 + r2)
    rbb = r1 * r2 / (r1 + r2)
    ib = (vbb - 0.7) / (rbb + (beta + 1.0) * re)
    ic = beta * ib
    vce = vcc - ic * rc - (ib + ic) * re
    return [ic, vce]

def region(ic, vce):
    if ic <= 0.0:
        return "Cutoff"
    elif vce < 0.2:
        return "Saturated"
    return "Active"

designs = [("stiff divider", 47000.0, 10000.0, 2200.0, 1000.0), ("no emitter R", 470000.0, 47000.0, 2200.0, 1.0), ("too much base", 10000.0, 10000.0, 4700.0, 470.0)]
for name, r1, r2, rc, re in designs:
    print(f"{name}:")
    for beta in [50.0, 150.0, 300.0]:
        ic, vce = bias(r1, r2, rc, re, beta)
        reg = region(ic, vce)
        if reg == "Saturated":
            sat = (12.0 - 0.2) / (rc + re) * 1000.0
            print(f"  beta {beta:.0f}: Region.{reg}, Vce pinned near 0.2 V, Ic held at {sat:.3f} mA")
        else:
            print(f"  beta {beta:.0f}: Ic {ic * 1000.0:.3f} mA, Vce {vce:.2f} V, Region.{reg}")
