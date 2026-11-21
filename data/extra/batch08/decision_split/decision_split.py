import math
def ent(y, n):
    t = y + n; h = 0.0
    for k in (y, n):
        if k > 0: p = k / t; h -= p * math.log(p) / math.log(2.0)
    return h
days = [("sunny", "hot", "high", "weak", "no"), ("sunny", "hot", "high", "strong", "no"), ("cloudy", "hot", "high", "weak", "yes"), ("rain", "mild", "high", "weak", "yes"), ("rain", "cool", "normal", "weak", "yes"), ("rain", "cool", "normal", "strong", "no"), ("cloudy", "cool", "normal", "strong", "yes"), ("sunny", "mild", "high", "weak", "no"), ("sunny", "cool", "normal", "weak", "yes"), ("rain", "mild", "normal", "weak", "yes"), ("sunny", "mild", "normal", "strong", "yes"), ("cloudy", "mild", "high", "strong", "yes"), ("cloudy", "hot", "normal", "weak", "yes"), ("rain", "mild", "high", "strong", "no")]
ya = sum(1 for d in days if d[4] == "yes"); base = ent(ya, len(days) - ya); print(f"label entropy {base:.3f}")
best = ""; bg = -1.0
for f, name in enumerate(["outlook", "temperature", "humidity", "wind"]):
    vals = set(d[f] for d in days); rest = 0.0
    for v in vals:
        y = sum(1 for d in days if d[f] == v and d[4] == "yes"); n = sum(1 for d in days if d[f] == v and d[4] == "no")
        rest += (y + n) / len(days) * ent(y, n)
    g = base - rest; print(f"{name:<11} gain {g:.3f}")
    if g > bg: best = name; bg = g
print(f"split first on {best}")
