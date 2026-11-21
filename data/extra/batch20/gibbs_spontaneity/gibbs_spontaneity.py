changes = [("ice melting", 6.01, 22.0), ("ammonia synthesis", -92.2, -198.7), ("limestone to lime", 178.3, 160.5), ("hydrogen peroxide splitting", -196.0, 125.8), ("ozone from oxygen", 285.4, -137.6)]

def kind(dh, ds):
    if dh < 0.0 and ds > 0.0:
        return "Always"
    elif dh > 0.0 and ds < 0.0:
        return "Never"
    elif dh < 0.0:
        return "BelowT"
    return "AboveT"

for name, dh, ds in changes:
    parts = [f"{dh - t * ds / 1000.0:.1f} at {t:.0f} K" for t in [250.0, 298.0, 1500.0]]
    print(f"{name}: dG {', '.join(parts)} kJ")
    k = kind(dh, ds)
    if k == "BelowT":
        print(f"  runs below {dh / ds * 1000.0:.0f} K")
    elif k == "AboveT":
        print(f"  runs above {dh / ds * 1000.0:.0f} K")
    elif k == "Always":
        print("  runs at every temperature")
    else:
        print("  never runs on its own")
