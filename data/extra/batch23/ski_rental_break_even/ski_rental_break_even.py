def break_even(days, buy):
    if days < buy:
        return days
    return buy - 1 + buy

def hindsight(days, buy):
    return min(days, buy)

buy = 10
print(f"skis cost {buy} to buy or 1 a day to rent")
worst_num = 0
worst_den = 1
worst_day = 0
for days in [1, 5, 9, 10, 11, 15, 30, 100]:
    paid = break_even(days, buy)
    best = hindsight(days, buy)
    print(f"season {days:>3} days: strategy pays {paid:>2}, hindsight {best:>2}")
for days in range(1, 101):
    paid = break_even(days, buy)
    best = hindsight(days, buy)
    if paid * worst_den > worst_num * best:
        worst_num = paid
        worst_den = best
        worst_day = days
ratio = worst_num / worst_den
print(f"worst ratio {worst_num}/{worst_den} = {ratio} at {worst_day} days (2 - 1/B = 1.9)")
print(f"buying on day one pays {buy} even for a 1-day season: {buy}x worse")
