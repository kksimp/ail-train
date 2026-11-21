base_units = 400
full_price = 200
cost = 120
sister_base = 300
sister_margin = 70
usual = (full_price - cost) * base_units
promos = [("10% off", 180, 560, 270), ("25% off", 150, 900, 220), ("2 for 3.20", 160, 900, 260)]
print(f"usual week: {base_units} units, margin {usual // 100}")
for label, price, units, su in promos:
    margin = (price - cost) * units
    lost = (sister_base - su) * sister_margin
    change = margin - usual - lost
    lift = (units - base_units) * 100 // base_units
    needed = (usual + lost + price - cost - 1) // (price - cost)
    verdict = "pays" if change >= 0 else "loses"
    q = int(change / 100)
    print(f"{label:<10} lift {lift:>3}%, margin {margin // 100}, sister loss {lost // 100}, change {q}: {verdict}; break-even {needed} units")
