h0 = 70.0
c = 299792.458
for name, mpc in [("Virgo cluster", 16.5), ("Coma cluster", 99.0), ("Hercules cluster", 150.0), ("distant group", 400.0)]:
    v = h0 * mpc
    z = v / c
    print(f"{name:<16} {mpc:>6.1f} Mpc: {v:>8.1f} km/s, z {z:.4f}")
for z in [0.01, 0.023, 0.05]:
    d = c * z / h0
    light_years = d * 3.262
    print(f"z {z}: about {d:.1f} Mpc ({light_years:.1f} million light years)")
print(f"Hubble time {977.8 / h0:.2f} billion years")
