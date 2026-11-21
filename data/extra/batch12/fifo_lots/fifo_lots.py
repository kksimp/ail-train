def cents(c):
    return f"{c // 100}.{c % 100:02}"

def sell(lots, qty):
    need = qty
    total = 0
    while need > 0 and len(lots) > 0:
        take = min(need, lots[0][0])
        total += take * lots[0][1]
        lots[0][0] -= take
        need -= take
        if lots[0][0] == 0:
            lots.pop(0)
    return total

lots = []
events = [("buy", 100, 250), ("buy", 50, 275), ("sell", 80, 400), ("buy", 120, 260), ("sell", 100, 420), ("sell", 60, 410)]
profit = 0
for kind, qty, price in events:
    if kind == "buy":
        lots.append([qty, price])
        print(f"buy  {qty:>3} at {cents(price)}")
    else:
        cogs = sell(lots, qty)
        sales = qty * price
        profit += sales - cogs
        print(f"sell {qty:>3} at {cents(price)}: cost of goods {cents(cogs)}, margin {cents(sales - cogs)}")
left = ", ".join(f"{l[0]}@{cents(l[1])}" for l in lots)
value = sum(l[0] * l[1] for l in lots)
print(f"left: {left} worth {cents(value)}")
print(f"total margin {cents(profit)}")
