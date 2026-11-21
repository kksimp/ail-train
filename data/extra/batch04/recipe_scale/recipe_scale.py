import math
def r5(x): return int(math.floor(x / 5 + 0.5)) * 5
G = [("flour", 250), ("sugar", 120), ("butter", 115), ("milk", 300)]
for s in [2, 6, 10]:
    f = s / 4; print(f"{s} servings: " + ", ".join(f"{n} {r5(g * f)}g" for n, g in G) + f", {math.ceil(3 * f)} eggs")
