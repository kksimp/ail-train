def threshold(r0): return 1.0 - 1.0 / r0
diseases = [("measles", 15.0, 0.97, 0.93), ("mumps", 10.0, 0.88, 0.93), ("rubella", 6.0, 0.97, 0.9), ("polio", 6.0, 0.99, 0.88), ("flu", 1.4, 0.5, 0.6)]
for name, r0, eff, cov in diseases:
    h = threshold(r0)
    need = h / eff
    immune = cov * eff
    reff = r0 * (1.0 - immune)
    if need > 1.0: status = "can't be reached by vaccine alone"
    elif cov >= need: status = "protected"
    else: status = f"gap {(need - cov) * 100.0:.1f} points"
    print(f"{name:<8} R0 {r0:>4.1f}: immune {h * 100.0:.1f}% needed, coverage {need * 100.0:.1f}% needed, R now {reff:.2f}, {status}")
