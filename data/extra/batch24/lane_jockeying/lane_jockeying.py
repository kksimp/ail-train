arrivals = [(0, 4), (0, 2), (1, 5), (1, 1), (2, 3), (2, 2), (3, 6), (3, 1), (4, 2), (4, 3)]
lanes = [[], []]
done = 0; switches = 0; minute = 0
while done < len(arrivals):
    for i, a in enumerate(arrivals):
        if a[0] == minute:
            lane = 1 if len(lanes[1]) < len(lanes[0]) else 0
            lanes[lane].append([i + 1, a[1], False])
    for k in range(2):
        if len(lanes[k]) >= len(lanes[1 - k]) + 2:
            s = lanes[k].pop()
            s[2] = True
            switches += 1
            lanes[1 - k].append(s)
    minute += 1
    for k in range(2):
        if lanes[k]:
            lanes[k][0][1] -= 1
            if lanes[k][0][1] == 0:
                s = lanes[k].pop(0)
                note = " (switched)" if s[2] else ""
                print(f"minute {minute:>2}: shopper {s[0]} leaves lane {k + 1}{note}")
                done += 1
print(f"{switches} switches, last shopper out at minute {minute}")
