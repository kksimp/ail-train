lots = [[1, 10, 5000, False], [2, 80, 4200, False], [3, 150, 4500, False], [4, 35, 3000, False]]
sales = [(1, 60, 4000), (2, 130, 4700), (3, 200, 4900), (4, 220, 5500)]
allowed = 0
deferred = 0
for lid, day, proceeds in sales:
    i = 0
    while lots[i][0] != lid:
        i += 1
    lots[i][3] = True
    result = proceeds - lots[i][2]
    if result >= 0:
        allowed += result
        print(f"day {day}: lot {lid} sold at a gain of {result}")
        continue
    loss = -result
    swap = -1
    for j in range(len(lots)):
        if not lots[j][3] and abs(lots[j][1] - day) <= 30 and swap == -1:
            swap = j
    if swap == -1:
        allowed += result
        print(f"day {day}: lot {lid} loss of {loss} allowed")
    else:
        lots[swap][2] += loss
        deferred += loss
        print(f"day {day}: lot {lid} loss of {loss} deferred to lot {lots[swap][0]}, its cost now {lots[swap][2]}")
print(f"net result counted {allowed}, losses deferred {deferred}")
