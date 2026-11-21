accts = {"Aisha": [1200, False], "Brodie": [300, False], "Chen": [0, True], "Dara": [-200, False]}
events = [(1, "Aisha", 0), (1, "Brodie", 0), (1, "Chen", 0), (1, "Dara", 0), (2, "Brodie", 0), (2, "Dara", 0), (2, "Dara", 1000), (3, "Brodie", 0), (3, "Brodie", 0), (4, "Aisha", 0), (4, "Brodie", 0), (5, "Chen", 0), (5, "Aisha", 0)]

def money(c):
    sign = "-" if c < 0 else ""
    a = abs(c)
    return f"{sign}{a // 100}.{a % 100:02d}"

for day, who, topup in events:
    a = accts[who]
    if topup > 0:
        a[0] += topup
        print(f"day {day}: {who} tops up {money(topup)}")
    elif a[1]:
        continue
    elif a[0] - 240 >= -500:
        a[0] -= 240
    else:
        print(f"day {day}: {who} refused at {money(a[0])}, packed lunch")
for who, a in accts.items():
    note = "free meals" if a[1] else ("send a letter" if a[0] < 500 else "fine")
    print(f"{who:<6} {money(a[0]):>6} {note}")
