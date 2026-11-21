def window_sum(xs, end, n):
    return sum(xs[end - n + 1:end + 1])

prices = [50, 51, 53, 52, 54, 56, 55, 53, 50, 48, 47, 49, 52, 55, 57, 60, 62, 61, 58, 55, 52, 54, 57, 59]
state = 0
holding = -1
profit = 0
for day in range(5, len(prices)):
    gap = 2 * window_sum(prices, day, 3) - window_sum(prices, day, 6)
    now = 1 if gap > 0 else (-1 if gap < 0 else state)
    if now != state and state != 0:
        if now == 1:
            holding = prices[day]
            print(f"day {day + 1}: buy at {prices[day]}")
        elif holding >= 0:
            profit += prices[day] - holding
            print(f"day {day + 1}: sell at {prices[day]} (made {prices[day] - holding})")
            holding = -1
        else:
            print(f"day {day + 1}: sell signal, nothing held")
    state = now
print(f"total made {profit}")
