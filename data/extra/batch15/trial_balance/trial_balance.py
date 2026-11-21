kinds = {"Cash": "Asset", "Equipment": "Asset", "Bank loan": "Liability", "Capital": "Equity", "Sales": "Income", "Rent": "Expense", "Wages": "Expense"}
def debit_normal(k): return k in ("Asset", "Expense")
entries = [[("Cash", 2000000), ("Capital", -2000000)], [("Equipment", 850000), ("Cash", -350000), ("Bank loan", -500000)], [("Cash", 1240000), ("Sales", -1240000)], [("Rent", 180000), ("Cash", -180000)], [("Wages", 420000), ("Cash", -420000)], [("Bank loan", 50000), ("Cash", -40000)]]
net = {}
for i, e in enumerate(entries):
    total = sum(l[1] for l in e)
    if total != 0:
        print(f"entry {i + 1} does not balance by {total}, skipped")
        continue
    for name, amt in e:
        net[name] = net.get(name, 0) + amt
dr = 0; cr = 0
for name, k in kinds.items():
    bal = net.get(name, 0)
    side = "Dr" if debit_normal(k) else "Cr"
    shown = bal if debit_normal(k) else -bal
    if bal >= 0: dr += bal
    else: cr -= bal
    print(f"{name:<10} {k:<9} {side} {int(shown / 100):>7}")
print(f"debits {dr // 100}, credits {cr // 100}, balanced: {'true' if dr == cr else 'false'}")
