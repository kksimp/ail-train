jobs = [("Raleigh", 50, [("brake pads", 1200), ("cable", 450)]), ("Brompton", 15, [("tube", 600)]), ("Trek", 95, [("chain", 2500), ("cassette", 4200)]), ("kids bike", 31, [])]

def money(c):
    return f"{c // 100}.{c % 100:02d}"

day = 0
for bike, minutes, parts in jobs:
    lab = (minutes + 14) // 15 * 1200
    pc = sum(p[1] * 120 // 100 for p in parts)
    sub = lab + pc
    vat = sub // 5
    day += sub + vat
    lst = "no parts" if not parts else " and ".join(p[0] for p in parts)
    print(f"{bike:<9} {minutes} min labour {money(lab)}, parts {money(pc)} ({lst}), VAT {money(vat)}, total {money(sub + vat)}")
print(f"quotes for the day: {money(day)}")
