for n, m in [("Ridgecrest", 7.1), ("Tohoku", 9.1), ("Christchurch", 6.2), ("Northridge", 6.7), ("local tremor", 3.4)]:
    r = 10.0 ** (1.5 * (m - 5.0)); j = 10.0 ** (1.5 * m + 4.8); rd = f"{r:.0f}" if r >= 10.0 else f"{r:.3f}"
    print(f"{n:<12} M{m:.1f}: {rd} x an M5, about {j / 1000000000000.0:.1f} TJ")
