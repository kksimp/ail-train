E0 = 0.000000000008854
area = 0.1 * 0.1
gap = 0.0001
stuff = [("air", 1.0006, 3.0), ("paper", 3.7, 16.0), ("mica", 6.0, 118.0), ("polyester", 3.3, 60.0), ("barium titanate", 1200.0, 4.0)]
energies = {}
for name, er, mv in stuff:
    c = E0 * er * area / gap
    vmax = mv * 1000000.0 * gap
    joules = 0.5 * c * vmax * vmax
    energies[name] = joules
    print(f"{name:<16} C {c * 1000000000000.0:>9.1f} pF, up to {vmax:>6.0f} V, stores {joules * 1000.0:>8.3f} mJ")
ranked = sorted(energies.keys(), key=lambda k: -energies[k])
print(f"best store: {ranked[0]}, worst: {ranked[-1]}")
