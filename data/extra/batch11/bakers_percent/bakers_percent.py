breads = [("baguette", [("flour", 100.0), ("water", 68.0), ("salt", 2.0), ("yeast", 1.0)]), ("pizza", [("flour", 100.0), ("water", 62.0), ("salt", 2.5), ("yeast", 0.5), ("olive oil", 3.0)]), ("brioche", [("flour", 100.0), ("milk", 30.0), ("egg", 40.0), ("butter", 50.0), ("sugar", 12.0), ("salt", 2.0), ("yeast", 2.0)])]
total = 1500.0
for name, parts in breads:
    pct = 0.0
    for p in parts:
        pct = pct + p[1]
    flour = total / (pct / 100.0)
    pieces = []
    for p in parts:
        grams = flour * p[1] / 100.0
        pieces.append(f"{p[0]} {grams:.1f} g")
    line = ", ".join(pieces)
    print(f"{name} ({pct}% in all): {line}")
water = 68.0
print(f"baguette hydration {water}%: {1500.0 / 1.71 * water / 100.0:.1f} g water to {1500.0 / 1.71:.1f} g flour")
