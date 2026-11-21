def weekly_demand(price):
    return max(50 - price // 2, 0)

def clear(qty, start, cut):
    left = qty
    price = start
    revenue = 0
    week = 0
    while week < 8 and left > 0:
        sold = min(weekly_demand(price), left)
        revenue += sold * price
        left -= sold
        price = price * (100 - cut) // 100
        week += 1
    return revenue + left * 10, left, week

price = 80
left = 120
for week in range(1, 5):
    sold = min(weekly_demand(price), left)
    left -= sold
    print(f"week {week}: price {price}, sold {sold}, left {left}")
    price = price * 80 // 100
for cut in [0, 10, 20, 30]:
    rev, lft, weeks = clear(120, 80, cut)
    print(f"cut {cut:>2}% a week: revenue {rev} after {weeks} weeks, {lft} to the jobber")
