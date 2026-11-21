import math
coils = [("relay coil", 0.5, 100.0, 12.0), ("motor winding", 0.02, 2.0, 24.0), ("ignition coil", 0.008, 0.5, 12.0)]
for name, henry, ohm, volts in coils:
    tau = henry / ohm
    final = volts / ohm
    print(f"{name}: tau {tau * 1000.0:.1f} ms, final {final:.3f} A, stores {0.5 * henry * final * final * 1000.0:.1f} mJ")
    parts = []
    for k in range(1, 5):
        cur = volts / ohm * (1.0 - math.exp(-(float(k) * tau) / tau))
        pct = cur / final * 100.0
        parts.append(f"{k} tau {pct:.1f}%")
    print("  " + ", ".join(parts))
    kick = henry * final / 0.000001
    print(f"  cut in 1 us: about {kick / 1000.0:.0f} kV across the contacts")
