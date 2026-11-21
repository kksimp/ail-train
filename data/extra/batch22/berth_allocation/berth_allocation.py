berths = [["North", 180, 0], ["Middle", 250, 0], ["South", 320, 0]]
ships = [("Aurora", 0, 160, 10), ("Borealis", 2, 290, 14), ("Cygnus", 3, 200, 8), ("Draco", 5, 150, 6), ("Electra", 6, 240, 12), ("Fornax", 9, 310, 9), ("Gemma", 11, 170, 5)]
waited = 0
for name, arrive, length, hours in ships:
    pick = -1
    pick_start = 0
    for i, b in enumerate(berths):
        if b[1] >= length:
            start = max(arrive, b[2])
            if pick == -1 or start < pick_start or (start == pick_start and b[1] < berths[pick][1]):
                pick = i
                pick_start = start
    if pick == -1:
        print(f"{name}: too long for every berth")
        continue
    berths[pick][2] = pick_start + hours
    wait = pick_start - arrive
    waited += wait
    print(f"{name:<8} ({length} m) arrives {arrive:>2}h: {berths[pick][0]} from {pick_start:>2}h to {pick_start + hours:>2}h, waits {wait}h")
print(f"total waiting {waited} hours")
