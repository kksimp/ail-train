events = [("O", "A", 20), ("O", "B", 25), ("O", "C", 15), ("O", "D", 30), ("D", "", 25), ("O", "E", 5), ("D", "", 40)]
shelf = 50
queue = []
ordered = 0
at_once = 0
for day, (kind, who, qty) in enumerate(events):
    if kind == "O":
        ordered += qty
        if not queue:
            ship = min(qty, shelf)
            shelf -= ship
            at_once += ship
            if ship < qty:
                queue.append([who, qty - ship])
            print(f"day {day + 1}: {who} orders {qty}, ships {ship}")
        else:
            queue.append([who, qty])
            print(f"day {day + 1}: {who} orders {qty}, joins the queue")
    else:
        shelf += qty
        print(f"day {day + 1}: delivery of {qty}")
        while shelf > 0:
            if not queue:
                break
            front = queue.pop(0)
            ship = min(front[1], shelf)
            shelf -= ship
            print(f"  {front[0]} gets {ship}")
            if ship < front[1]:
                queue.insert(0, [front[0], front[1] - ship])
print(f"shipped at once {at_once} of {ordered} ({at_once * 100 // ordered}%), shelf ends at {shelf}, {len(queue)} waiting")
