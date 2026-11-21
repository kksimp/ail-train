G = sorted([(r / c * 27.0, f"{r}x{c}") for r in [34, 50] for c in [11, 13, 15, 17, 19, 21, 23, 28]], key=lambda g: g[0]); p = 0.0
for v, n in G: print(f"{n:<6} {v:>6.1f}" + (" (close to previous)" if p > 0 and (v - p) / p < 0.02 else "")); p = v
print(f"range {G[0][0]:.1f} to {G[-1][0]:.1f}")
