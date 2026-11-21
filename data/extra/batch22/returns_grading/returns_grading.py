returns = [("kettle", 40, 5, True, True), ("headset", 90, 12, False, True), ("drill", 120, 20, True, False), ("jacket", 75, 45, False, True), ("blender", 60, 28, True, True), ("speaker", 150, 3, True, False)]

def grade(price, days, opened, works):
    if days > 30:
        return "Refuse"
    if not opened:
        return "Resell"
    return "Refurbish" if works else "Liquidate"

def recovered(g, price):
    return {"Resell": price, "Refurbish": max(price * 70 // 100 - 5, 0), "Liquidate": price * 20 // 100, "Refuse": 0}[g]

refunds = 0
back = 0
counts = {}
for item, price, days, opened, works in returns:
    g = grade(price, days, opened, works)
    got = recovered(g, price)
    counts[g] = counts.get(g, 0) + 1
    if g != "Refuse":
        refunds += price
        back += got
    print(f"{item:<8} {price:>4}: Grade.{g}, recovers {got}")
print(f"refunded {refunds}, recovered {back}, cost of returns {refunds - back}")
for name, n in counts.items():
    print(f"{name}: {n}")
