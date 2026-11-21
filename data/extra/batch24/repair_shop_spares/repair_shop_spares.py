def short_hours(spares):
    state = 99
    def life():
        nonlocal state
        state = (state * 1103515245 + 12345) % 2147483648
        return 30 + (state // 65536) % 20
    running = [life() for i in range(5)]
    stand_by = spares; broken = 0; repair_left = 0; short = 0; fixed = 0
    for hour in range(400):
        broke_now = sum(1 for t in running if t == hour)
        running = [t for t in running if t != hour]
        broken += broke_now
        while len(running) < 5 and stand_by > 0:
            stand_by -= 1
            running.append(hour + life())
        if repair_left == 0 and broken > 0:
            broken -= 1
            repair_left = 6
        if repair_left > 0:
            repair_left -= 1
            if repair_left == 0:
                stand_by += 1
                fixed += 1
        if len(running) < 5: short += 1
    return [short, fixed]
for spares in range(4):
    r = short_hours(spares)
    print(f"{spares} spares: running short {r[0]:>3} of 400 hours, {r[1]} repairs")
