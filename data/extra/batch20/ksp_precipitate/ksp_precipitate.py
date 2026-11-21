import math

def solubility(ksp, ratio):
    return math.sqrt(ksp) if ratio == 1 else math.cbrt(ksp / 4.0)

salts = [("silver chloride", 0.00000000018, 1), ("barium sulfate", 0.0000000011, 1), ("lead iodide", 0.0000000071, 2), ("fluorite CaF2", 0.000000000039, 2), ("silver chromate", 0.0000000000011, 2)]
for name, ksp, ratio in salts:
    print(f"{name:<16} dissolves {solubility(ksp, ratio) * 1000000.0:>8.2f} umol/L")
agcl = salts[0][1]
for c in [0.00001, 0.0001, 0.001]:
    q = (c / 2.0) * (c / 2.0)
    verdict = "precipitate forms" if q > agcl else "stays clear"
    print(f"equal volumes of {c * 1000.0} mM silver nitrate and salt: Q {q / agcl:.3f} x Ksp, {verdict}")
common = agcl / 0.1
print(f"in 0.1 M salt water silver chloride dissolves only {common * 1000000000.0:.1f} nmol/L")
