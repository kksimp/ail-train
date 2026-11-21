def program(size, dirt):
    if size == "V": return "van bay"
    if dirt == 0: return "rinse only"
    if size == "S" and dirt <= 2: return "quick wash"
    if dirt >= 4: return "deluxe wash"
    return "standard wash"
price = {"van bay": 1500, "rinse only": 300, "quick wash": 600, "deluxe wash": 1400}
cars = [("AB12", "S", 1), ("CD34", "M", 0), ("EF56", "V", 5), ("GH78", "L", 4), ("IJ90", "M", 2), ("KL11", "S", 3)]
counts = {}; takings = 0
for plate, size, dirt in cars:
    p = program(size, dirt)
    counts[p] = counts.get(p, 0) + 1
    takings += price.get(p, 900)
    print(f"{plate} ({size}, dirt {dirt}): {p}")
for k, v in counts.items():
    print(f"{k}: {v}")
print(f"takings {takings // 100}.{takings % 100:02}")
