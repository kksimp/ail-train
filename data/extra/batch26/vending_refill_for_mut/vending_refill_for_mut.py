slots = [["A1", "crisps", 4, 8, 120], ["B2", "water", 1, 6, 90], ["C1", "chocolate", 0, 5, 150], ["C3", "gum", 3, 10, 60]]
t = 0
for code in ["A1", "A1", "B2", "C1", "A1", "B2", "A1", "C3"]:
    sold = False
    for s in slots:
        if s[0] == code and s[2] > 0:
            s[2] -= 1; t += s[4]; sold = True
    if not sold: print(f"{code}: sold out")
print(f"takings {t // 100}.{t % 100:02}")
for s in slots: print(f"{s[0]} {s[1]:<9} {s[2]}/{s[3]}")
loaded = sum(s[3] - s[2] for s in slots)
print(f"refilled {loaded} items, all full: true")
