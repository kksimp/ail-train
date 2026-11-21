import math
def sat(t):
    return 6.112 * math.exp(17.67 * t / (t + 243.5))
def humidity(dry, wet):
    vapour = sat(wet) - 0.00066 * 1013.0 * (dry - wet)
    return vapour / sat(dry) * 100.0
for place, dry, wet in [("greenhouse", 28.0, 25.5), ("office", 22.0, 15.0), ("desert noon", 38.0, 19.0), ("cellar", 12.0, 11.5), ("sauna", 80.0, 40.0)]:
    rh = humidity(dry, wet)
    feel = "dry" if rh < 30.0 else ("comfortable" if rh < 60.0 else "humid")
    print(f"{place:<12} dry {dry:>4.1f} wet {wet:>4.1f}: {rh:>5.1f}% RH, {feel}")
print(f"saturation at 20 C: {sat(20.0):.2f} hPa")
