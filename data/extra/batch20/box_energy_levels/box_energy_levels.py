H = 0.000000000000000000000000000000000662607
ME = 0.000000000000000000000000000000910938
EV = 0.0000000000000000001602177
C = 299792458.0

def level_ev(n, l_nm):
    l = l_nm / 1000000000.0
    return float(n * n) * H * H / (8.0 * ME * l * l) / EV

def absorb_nm(electrons, l_nm):
    homo = electrons // 2
    gap = level_ev(homo + 1, l_nm) - level_ev(homo, l_nm)
    return H * C / (gap * EV) * 1000000000.0

for n in range(1, 5):
    print(f"1 nm box, level {n}: {level_ev(n, 1.0):.3f} eV")
for name, e, l in [("butadiene", 4, 0.578), ("hexatriene", 6, 0.867), ("octatetraene", 8, 1.156), ("beta-carotene", 22, 1.77)]:
    nm = absorb_nm(e, l)
    seen = "ultraviolet, so colourless" if nm < 380.0 else ("visible, so coloured" if nm <= 750.0 else "infrared")
    print(f"{name:<13} {e:>2} pi electrons over {l} nm: absorbs {nm:.0f} nm, {seen}")
