def simpson(counts):
    total = sum(counts)
    pairs = sum(n * (n - 1) for n in counts)
    return 1.0 - float(pairs) / float(total * (total - 1))
sites = {"shaded pond": [40, 2, 1, 1], "open pond": [12, 10, 9, 8, 6], "ditch": [25, 25], "lake edge": [15, 3, 7, 2, 9, 4]}
best = ""
best_d = -1.0
for name, counts in sites.items():
    d = simpson(counts)
    total = sum(counts)
    print(f"{name:<11} {len(counts)} species, {total:>2} animals: D {d:.3f}")
    if d > best_d:
        best = name
        best_d = d
print(f"most diverse: {best}")
