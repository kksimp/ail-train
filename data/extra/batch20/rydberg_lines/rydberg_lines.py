R = 10973731.568

def wavelength_nm(n1, n2):
    a = float(n1)
    b = float(n2)
    return 1000000000.0 / (R * (1.0 / (a * a) - 1.0 / (b * b)))

def band(nm):
    if nm < 380.0:
        return "Ultraviolet"
    elif nm <= 750.0:
        return "Visible"
    return "Infrared"

for name, n1 in [("Lyman", 1), ("Balmer", 2), ("Paschen", 3)]:
    parts = []
    for n2 in range(n1 + 1, n1 + 5):
        nm = wavelength_nm(n1, n2)
        parts.append(f"{n2}->{n1} {nm:.1f}")
    limit = 1000000000.0 * float(n1 * n1) / R
    print(f"{name}: {', '.join(parts)} nm, limit {limit:.1f} nm")
    print(f"  first line is Band.{band(wavelength_nm(n1, n1 + 1))}")
