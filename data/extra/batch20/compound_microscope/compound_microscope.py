def mag(focal, eye):
    return 160.0 / focal * (250.0 / eye)

def res_um(na):
    return 0.61 * 0.55 / na

objectives = [(40.0, 0.1), (16.0, 0.25), (4.0, 0.65), (1.6, 1.25)]
for focal, na in objectives:
    res = res_um(na)
    print(f"objective f {focal} mm, NA {na}: resolves {res:.2f} um")
    for eye in [25.0, 10.0]:
        m = mag(focal, eye)
        verdict = "empty magnification" if m > 1000.0 * na else "useful"
        print(f"  eyepiece {eye} mm: {m:.0f}x {verdict}")
