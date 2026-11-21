def avg_inv(c): return float(c[3] + c[4]) / 2.0
def gmroi(c): return float(c[1] - c[2]) / avg_inv(c)
cats = [("fresh food", 820000, 590000, 21000, 19000), ("clothing", 310000, 155000, 96000, 112000), ("electronics", 450000, 382000, 88000, 92000), ("homeware", 190000, 108000, 41000, 37000)]
for c in sorted(cats, key=lambda c: -int(gmroi(c) * 1000.0)):
    margin = float(c[1] - c[2]) / float(c[1]) * 100.0
    turns = float(c[2]) / avg_inv(c)
    verdict = "  below 1, review" if gmroi(c) < 1.0 else ""
    print(f"{c[0]:<12} margin {margin:>4.1f}%, turns {turns:>5.2f}, GMROI {gmroi(c):>5.2f}{verdict}")
