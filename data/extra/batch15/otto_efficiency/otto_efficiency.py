import math
def otto(r, g): return 1.0 - math.pow(r, 1.0 - g)
def diesel(r, rho, g): return 1.0 - (math.pow(rho, g) - 1.0) / (g * (rho - 1.0)) / math.pow(r, g - 1.0)
gamma = 1.4
print("petrol (Otto):")
for r in [6, 8, 10, 12, 14]:
    e = otto(float(r), gamma) * 100.0
    bar = "#" * int(e / 5.0)
    print(f"  r = {r:>2}: {e:.1f}% {bar}")
print("diesel, cut-off ratio 2:")
for r in [16, 18, 20, 22]:
    e = diesel(float(r), 2.0, gamma) * 100.0
    o = otto(float(r), gamma) * 100.0
    print(f"  r = {r}: {e:.1f}% (Otto at same r {o:.1f}%)")
