buy = {"tube": 450, "bolt": 12, "rim": 900, "spoke": 8, "hub": 1500, "seat": 2200, "chain": 1300, "pedal": 600}
scrap = {"spoke": 5, "bolt": 10, "tube": 4}
bom = {"frame": [("tube", 3), ("bolt", 6)], "wheel": [("rim", 1), ("spoke", 32), ("hub", 1)], "bike": [("frame", 1), ("wheel", 2), ("seat", 1), ("chain", 1), ("pedal", 2), ("bolt", 10)]}
labour = {"frame": 2500, "wheel": 1200, "bike": 3500}

def cost(name):
    if name in buy:
        return buy[name]
    total = labour.get(name, 0)
    for p, q in bom.get(name, []):
        total += q * cost(p) * (100 + scrap.get(p, 0)) // 100
    return total

def money(c):
    return f"{c // 100}.{c % 100:02d}"

for name in ["frame", "wheel", "bike"]:
    print(f"{name:<5} {money(cost(name)):>7} (labour {money(labour[name])})")
print(f"spokes in one bike: {money(2 * (32 * buy['spoke'] * (100 + scrap['spoke']) // 100))}")
