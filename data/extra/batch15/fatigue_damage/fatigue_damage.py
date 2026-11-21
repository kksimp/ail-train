def cycles_to_failure(stress):
    s = float(stress)
    return 2000000000000.0 / (s * s * s)
spectrum = [(40, 2000000), (60, 500000), (90, 60000), (140, 5000), (200, 200)]
damage = 0.0
worst = spectrum[0]; worst_d = 0.0
for st, cy in spectrum:
    n = cycles_to_failure(st)
    d = float(cy) / n
    damage += d
    if d > worst_d:
        worst_d = d; worst = (st, cy)
    print(f"{st:>3} MPa: {cy:>9,} cycles of {n:>12,.0f} allowed, damage {d:.5f}")
print(f"yearly damage {damage:.4f}, expected life {1.0 / damage:.1f} years")
print(f"most damaging band: {worst[0]} MPa")
print(f"total cycles a year: {sum(c for _, c in spectrum):,}")
