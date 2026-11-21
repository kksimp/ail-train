events = [("L", 0, -1), ("S", 0, 1), ("L", 2, -1), ("S", 2, 1), ("R", 1, -1), ("L", 1, -1), ("R", 1, -1), ("S", 1, 0), ("L", 2, -1), ("R", 0, -1)]
clock = [0, 0, 0]
inbox = [[], [], []]
stamped = []
for kind, who, to in events:
    if kind == "L":
        clock[who] += 1
        print(f"S{who} local       t={clock[who]}")
    elif kind == "S":
        clock[who] += 1
        inbox[to].append(clock[who])
        print(f"S{who} send to S{to}  t={clock[who]}")
    else:
        sent = inbox[who].pop(0)
        clock[who] = max(clock[who], sent) + 1
        print(f"S{who} receive {sent}   t={clock[who]}")
    stamped.append([clock[who], who])
order = " ".join(f"{p[0]}.S{p[1]}" for p in sorted(stamped))
print(f"total order: {order}")
