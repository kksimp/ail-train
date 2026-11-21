import math
def effective(r, n):
    return (1.0 + r / float(n)) ** float(n) - 1.0
periods = [("yearly", 1), ("half-yearly", 2), ("quarterly", 4), ("monthly", 12), ("daily", 365)]
label = "continuous"
for r in [0.05, 0.2]:
    print(f"nominal {r * 100.0:.1f}%:")
    for name, n in periods:
        print(f"  {name:<12} {effective(r, n) * 100.0:.4f}%")
    cont = (math.exp(r) - 1.0) * 100.0
    print(f"  {label:<12} {cont:.4f}%")
grown = 1000.0 * (1.0 + effective(0.2, 12)) ** 5.0
print(f"1000 at 20% compounded monthly for 5 years: {grown:.2f}")
