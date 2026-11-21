sizes = ["XS", "S", "M", "L", "XL"]
counts = {}; unknown = []
for o in ["m", "L", "xl", "XXL", " s ", "M", "l", "medium"]:
    t = o.strip().upper()
    if t not in sizes:
        unknown.append(o.strip()); continue
    counts[t] = counts.get(t, 0) + 1
for v in sizes:
    print(f"{v:<2} {counts.get(v, 0)}")
print(f"not understood: {', '.join(unknown)}")
print("M sold out, offer L; XL stays XL")
