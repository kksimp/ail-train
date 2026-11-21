def parts(f):
    return [float(f[2]) / float(f[1]), float(f[1]) / float(f[3]), float(f[3]) / float(f[4])]
firms = [("grocer", 9200, 230, 3100, 1250), ("software", 1800, 410, 2600, 2000), ("utility", 2400, 260, 9800, 2100)]
for f in firms:
    p = parts(f)
    roe = p[0] * p[1] * p[2] * 100.0
    driver = "margin" if p[0] > 0.15 else "turnover" if p[1] > 2.0 else "leverage"
    print(f"{f[0]:<9} margin {p[0] * 100.0:>5.2f}% x turnover {p[1]:.2f} x multiplier {p[2]:.2f} = ROE {roe:.1f}% ({driver})")
best = max(firms, key=lambda f: f[2] * 1000 // f[4])
print(f"highest ROE: {best[0]}")
