def allocate(total, weights):
    w_sum = sum(weights)
    days = [total * w // w_sum for w in weights]
    rems = [total * w % w_sum for w in weights]
    spare = total - sum(days)
    order = sorted(range(len(weights)), key=lambda i: (-rems[i], i))
    for k in range(spare):
        days[order[k]] += 1
    return days

cities = ["Lisbon", "Porto", "Seville", "Granada", "Madrid"]
weights = [5, 3, 4, 2, 4]
for total in [14, 10]:
    days = allocate(total, weights)
    day = 1
    legs = []
    for i, c in enumerate(cities):
        if days[i] == 0:
            continue
        last = day + days[i] - 1
        legs.append(f"{c} {day}-{last}")
        day = last + 1
    plan = ", ".join(legs)
    print(f"{total} days: {days}")
    print(f"  {plan}")
