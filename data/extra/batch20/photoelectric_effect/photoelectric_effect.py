HC = 1239.84
metals = [("caesium", 2.1), ("sodium", 2.28), ("zinc", 4.3), ("platinum", 5.65)]
waves = [620.0, 450.0, 250.0, 180.0]
for w in waves:
    print(f"{w:.0f} nm photons carry {HC / w:.3f} eV")
for name, work in metals:
    parts = []
    for w in waves:
        ke = HC / w - work
        parts.append(f"{ke:.2f}" if ke > 0.0 else "-")
    print(f"{name:<9} threshold {HC / work:>5.0f} nm, stopping volts {' / '.join(parts)}")
