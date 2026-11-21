cap = 160200
for name, monthly in [("Ana", 9000), ("Raj", 15000), ("Lee", 25000)]:
    ytd = 0
    paid = 0
    capped = 0
    full = monthly * 62 // 1000
    for m in range(1, 13):
        room = max(cap - ytd, 0)
        taxable = min(monthly, room)
        ytd += monthly
        c = taxable * 62 // 1000
        paid += c
        if c < full and capped == 0:
            capped = m
    health = monthly * 12 * 145 // 10000
    bp = paid * 10000 // (monthly * 12)
    note = "never reaches the cap" if capped == 0 else f"cap reached in month {capped}"
    print(f"{name}: social {paid} ({bp // 100}.{bp % 100:02d}% of pay), health {health}, {note}")
