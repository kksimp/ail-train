import math
stars = [("Sirius", -1.46, 8.6), ("Vega", 0.03, 25.0), ("Betelgeuse", 0.5, 548.0), ("Polaris", 1.98, 433.0), ("Proxima", 11.13, 4.24), ("Rigel", 0.13, 863.0)]
for n, m, ly in stars:
    M = m - 5.0 * math.log10(ly / 3.2616 / 10.0); dim = 10.0 ** (0.4 * (m - -1.46))
    print(f"{n:<10} m {m:>6.2f}, {ly:>5.0f} ly, M {M:>6.2f}, {dim:>10.1f}x dimmer than Sirius")
