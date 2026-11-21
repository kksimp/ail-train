buyers = [("Abe", 5), ("Bea", 12), ("Cal", 3), ("Dee", 8), ("Eve", 1), ("Fay", 6)]
prizes = ["hamper", "bike", "spa voucher", "cinema tickets", "wine"]
owner = []
for name, count in buyers:
    for _ in range(count):
        owner.append(name)
print(f"{len(owner)} tickets sold")
seed = 123
winners = set()
drawn = set()
for prize in prizes:
    done = False
    while not done:
        seed = (seed * 1103515245 + 12345) % 2147483648
        ticket = (seed // 65536) % len(owner) + 1
        if ticket in drawn:
            continue
        drawn.add(ticket)
        who = owner[ticket - 1]
        if who in winners:
            print(f"  ticket {ticket} ({who}) already won, redraw")
            continue
        winners.add(who)
        print(f"{prize}: ticket {ticket}, {who}")
        done = True
