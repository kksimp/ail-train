def g(b): return 1.0 / (1.0 - b * b) ** 0.5
for b in [0.1, 0.5, 0.8, 0.9, 0.99, 0.999]:
    G = g(b); print(f"{b:>5.3f} c: factor {G:>7.3f}, traveller ages {10.0 / G:>5.2f} years")
print(f"a year on a jet at 900 km/h gains about {(g(0.00000083) - 1.0) * 24.0 * 365.25 * 3600.0 * 1000000000.0:.0f} ns")
