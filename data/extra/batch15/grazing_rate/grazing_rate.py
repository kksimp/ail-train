def usable(p): return p[1] * p[2] * 0.5
def cows(p, intake, days): return int(usable(p) / (intake * float(days)))
weight = 550.0
intake = weight * 0.025
days = 120
paddocks = [("river flat", 14.0, 6200.0), ("top field", 22.0, 3100.0), ("hill block", 38.0, 1450.0), ("orchard", 3.5, 4800.0)]
print(f"cow of {weight:.0f} kg eats {intake:.2f} kg dry matter a day for {days} days")
herd = 0
for p in paddocks:
    n = cows(p, intake, days)
    herd += n
    per_ha = float(n) / p[1]
    print(f"{p[0]:<11} {usable(p):>8.0f} kg usable: {n:>2} cows ({per_ha:.2f} per ha)")
print(f"whole farm carries {herd} cows for the season")
shorter = 0
for p in paddocks: shorter = shorter + cows(p, intake, 90)
print(f"for a 90-day season: {shorter} cows")
