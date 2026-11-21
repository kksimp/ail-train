uses = [("pickles", 3.5), ("olives", 10.0), ("turkey", 6.0), ("kimchi", 2.0), ("feta", 8.0)]
for n, p in uses:
    s = 1000.0 * p / (100.0 - p); print(f"{n:<8} {p:>4.1f}%: {s:>6.1f} g salt per litre, {s / 18.0:.1f} tbsp")
print(f"all five: {sum(1000.0 * p / (100.0 - p) for n, p in uses):.0f} g")
