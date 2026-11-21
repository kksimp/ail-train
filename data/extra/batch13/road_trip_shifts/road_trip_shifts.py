legs = [("Leeds", 95), ("York", 40), ("Durham", 70), ("Newcastle", 25), ("Berwick", 75), ("Edinburgh", 60), ("Perth", 50), ("Pitlochry", 35), ("Aviemore", 55), ("Inverness", 40)]
drivers = [{"name": "Ana", "stint": 0, "day": 0}, {"name": "Raj", "stint": 0, "day": 0}, {"name": "Sue", "stint": 0, "day": 0}]
cur = 0
for place, minutes in legs:
    if drivers[cur]["stint"] + minutes > 120:
        drivers[cur]["stint"] = 0
        nxt = (cur + 1) % 3
        while drivers[nxt]["day"] + minutes > 240:
            nxt = (nxt + 1) % 3
        print(f"swap at the start of the leg to {place}: {drivers[cur]['name']} hands over to {drivers[nxt]['name']}")
        cur = nxt
    drivers[cur]["stint"] += minutes
    drivers[cur]["day"] += minutes
for d in drivers:
    print(f"{d['name']}: {d['day'] // 60} h {d['day'] % 60:02} min")
