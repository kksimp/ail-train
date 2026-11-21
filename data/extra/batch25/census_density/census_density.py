regions = [("Harbourside", 1840000, 1250), ("Midvale", 920000, 6450), ("Northfell", 210000, 18200), ("Riverlands", 1330000, 9800), ("Eastmarsh", 455000, 7100), ("Highcairn", 96000, 21500)]

def density(r):
    return r[1] / r[2]

people = sum(r[1] for r in regions)
land = sum(r[2] for r in regions)
ranked = sorted(regions, key=lambda r: -density(r))
for i, r in enumerate(ranked):
    share_p = r[1] / people * 100.0
    share_l = r[2] / land * 100.0
    print(f"{i + 1}. {r[0]:<12} {r[1]:>9,} people {r[2]:>6,} km2 {density(r):>7.1f}/km2  {share_p:>4.1f}% of people on {share_l:>4.1f}% of land")
national = people / land
ratio = density(ranked[0]) / density(ranked[-1])
print(f"national {national:.1f}/km2; the densest region is {ratio:.0f} times the sparsest")
