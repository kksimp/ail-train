def fcr(f):
    gained = float(f[2]) * float(f[4] - 42) / 1000.0
    return float(f[3]) / gained
def epef(f):
    live = float(f[2]) / float(f[1]) * 100.0
    kg = float(f[4]) / 1000.0
    return live * kg / (float(f[5]) * fcr(f)) * 100.0
flocks = [("House 1", 24000, 23180, 77200, 2350, 38), ("House 2", 24000, 22704, 79900, 2410, 40), ("House 3", 18000, 17620, 54100, 2280, 36), ("House 4", 18000, 16950, 58300, 2390, 41)]
ranked = sorted(flocks, key=lambda f: -int(epef(f) * 100.0))
for f in ranked:
    mort = float(f[1] - f[2]) / float(f[1]) * 100.0
    print(f"{f[0]}: FCR {fcr(f):.3f}, mortality {mort:.2f}%, {f[4]} g at {f[5]} days, EPEF {epef(f):.0f}")
print(f"best house: {ranked[0][0]}")
