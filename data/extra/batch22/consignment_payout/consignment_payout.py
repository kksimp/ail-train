def commission(price):
    return price * 40 // 100 if price < 100 else price * 30 // 100

today = 90
items = [("May", "lamp", 45, 5, 30), ("May", "desk", 180, 12, 70), ("May", "vase", 25, 20, None), ("Jon", "coat", 120, 40, 55), ("Jon", "boots", 60, 50, None), ("Kai", "guitar", 250, 2, None), ("Kai", "amp", 95, 33, 88)]
payout = {}
kept = 0
for owner, name, price, listed, sold in items:
    if sold is not None:
        cut = commission(price)
        kept += cut
        payout[owner] = payout.get(owner, 0) + price - cut
        print(f"{name:<6} sold day {sold} for {price}: owner {price - cut}, shop {cut}")
    elif today - listed > 60:
        print(f"{name:<6} unsold after {today - listed} days: returned to {owner}")
    else:
        print(f"{name:<6} on the floor")
for owner, amount in payout.items():
    print(f"pay {owner} {amount}")
print(f"shop keeps {kept}")
