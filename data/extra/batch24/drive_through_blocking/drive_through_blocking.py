cars = [(0, 40, 30), (20, 35, 90), (30, 50, 25), (70, 30, 40), (80, 45, 120), (100, 20, 30), (160, 40, 35), (300, 30, 30)]
order_free = 0; pickup_free = 0; blocked_total = 0
for i, (arrive, order, pickup) in enumerate(cars):
    start = max(arrive, order_free)
    ordered = start + order
    at_window = max(ordered, pickup_free)
    blocked = at_window - ordered
    order_free = at_window
    pickup_free = at_window + pickup
    blocked_total += blocked
    print(f"car {i + 1}: in {arrive:>3}, ordered {ordered:>3}, blocked {blocked:>3}, leaves {pickup_free:>3}")
print(f"order window blocked {blocked_total} s in all; last car leaves at {pickup_free} s")
