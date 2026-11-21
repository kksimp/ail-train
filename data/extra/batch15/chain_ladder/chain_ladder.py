years = [2022, 2023, 2024, 2025]
tri = [[3200.0, 5100.0, 5900.0, 6150.0], [3550.0, 5700.0, 6500.0], [3900.0, 6150.0], [4200.0]]
n = len(tri)
factors = []
for j in range(n - 1):
    top = 0.0; bottom = 0.0
    for row in tri:
        if len(row) > j + 1:
            top += row[j + 1]; bottom += row[j]
    factors.append(top / bottom)
print("link ratios " + ", ".join(f"{f:.4f}" for f in factors))
reserve = 0.0
for i, row in enumerate(tri):
    latest = row[-1]; ult = latest
    for j in range(len(row) - 1, n - 1):
        ult = ult * factors[j]
    reserve += ult - latest
    print(f"{years[i]}: paid {latest:>7.0f}, ultimate {ult:>7.0f}, reserve {ult - latest:>6.0f}")
print(f"total reserve {reserve:.0f}")
