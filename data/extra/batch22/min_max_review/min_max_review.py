demand = [8, 12, 5, 9, 14, 7, 10, 6, 11, 13, 4, 9, 15, 8, 6, 12, 10, 7, 9, 11]
on_hand = 40
arrivals = {}
lost = 0
held = 0
orders = 0
for day in range(1, len(demand) + 1):
    got = arrivals.get(day, 0)
    if got > 0:
        on_hand += got
        del arrivals[day]
        print(f"day {day:>2}: received {got}")
    d = demand[day - 1]
    served = min(d, on_hand)
    on_hand -= served
    lost += d - served
    position = on_hand + sum(arrivals.values())
    if position <= 20:
        q = 60 - position
        arrivals[day + 2] = q
        orders += 1
        print(f"day {day:>2}: on hand {on_hand}, ordered {q}")
    held += on_hand
print(f"{orders} orders, {lost} units lost, average on hand {held // len(demand)}")
