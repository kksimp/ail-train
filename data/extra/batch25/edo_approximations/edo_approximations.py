import math

def log2(x):
    return math.log(x) / math.log(2.0)

def miss(n, ratio):
    exact = 1200.0 * log2(ratio)
    steps = float(math.floor(n * log2(ratio) + 0.5))
    return steps * 1200.0 / n - exact

ratios = [1.5, 1.25, 1.75]
print("EDO   fifth 3/2  third 5/4  seventh 7/4  total")
best = 0
best_total = 1000.0
for n in [5, 7, 12, 19, 22, 31, 53]:
    errs = [miss(n, r) for r in ratios]
    total = 0.0
    for e in errs:
        total = total + abs(e)
    if total < best_total:
        best_total = total
        best = n
    print(f"{n:>3}   {errs[0]:>9.1f}  {errs[1]:>9.1f}  {errs[2]:>11.1f}  {total:>5.1f}")
print(f"closest overall: {best}-EDO, {best_total:.2f} cents off in all")
