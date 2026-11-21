B = {"paper": "blue", "card": "blue", "glass": "green", "plastic": "yellow", "metal": "yellow", "food": "brown"}; w = {}
for n, m, g in [("newspaper", "paper", 300), ("jar", "glass", 250), ("crisp packet", "foil-plastic", 10), ("tin", "metal", 60), ("peel", "food", 120), ("box", "card", 180), ("bottle", "plastic", 40), ("nappy", "mixed", 400)]:
    b = B.get(m, "landfill"); w[b] = w.get(b, 0) + g; print(f"{n:<13} -> {b}")
for b in sorted(w): print(f"{b}: {w[b]} g")
t = sum(w.values()); print(f"recycled {(t - w.get('landfill', 0)) * 100 // t}%")
