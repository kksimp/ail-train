bills = {4: 2400, 7: 1500, 10: 2400}
deposit = 400
bal = 200
low = bal
low_month = 0
for m in range(1, 13):
    bal += deposit
    out = bills.get(m, 0)
    bal -= out
    if bal < low:
        low = bal
        low_month = m
    if out > 0:
        print(f"month {m:>2}: pays {out}, balance {bal}")
yearly = sum(bills.values())
cushion = yearly // 6
shortage = max(cushion - low, 0)
print(f"yearly bills {yearly}, cushion {cushion}, lowest {low} in month {low_month}")
print(f"shortage {shortage}")
new_dep = (yearly + shortage + 11) // 12
print(f"new monthly deposit {new_dep} (was {deposit})")
