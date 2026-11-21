waiting = [[], []]
arrivals = [[2, 4, 5, 9, 11, 12, 14, 15, 16, 30, 33, 41, 44, 50, 58, 61, 63], [1, 3, 8, 20, 22, 24, 26, 27, 28, 29, 31, 35, 47, 66, 70]]
next_car = [0, 0]
port = 0; sail_at = 0; carried = 0; waited = 0
for trip in range(1, 9):
    depart = sail_at + 5
    for p in range(2):
        while next_car[p] < len(arrivals[p]) and arrivals[p][next_car[p]] <= depart:
            waiting[p].append(arrivals[p][next_car[p]])
            next_car[p] += 1
    load = min(len(waiting[port]), 6)
    for k in range(load):
        waited += depart - waiting[port][k]
    waiting[port] = waiting[port][load:]
    carried += load
    name = "A" if port == 0 else "B"
    print(f"trip {trip}: leaves {name} at {depart:>3} with {load} cars, {len(waiting[port])} left behind")
    sail_at = depart + 20
    port = 1 - port
print(f"{carried} cars carried, mean wait {waited / carried:.2f} minutes")
