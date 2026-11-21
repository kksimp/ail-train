plan = [[10, 6000], [40, 6000], [70, 6000]]
check = 50
payments = {"Amir": [[8, 6000], [39, 6000]], "Beth": [[5, 18000]], "Cole": [[12, 6000]], "Dina": [[20, 3000], [45, 3000], [48, 6000]], "Ezra": []}
consent = {"Amir", "Beth", "Dina", "Ezra"}

def money(c):
    return f"{c // 100}.{c % 100:02d}"

owed = sum(p[1] for p in plan if p[0] <= check)
print(f"due by day {check}: {money(owed)}")
going = 0
for name, pays in payments.items():
    paid = sum(p[1] for p in pays if p[0] <= check)
    status = "paid in full" if paid >= 18000 else ("up to date" if paid >= owed else f"behind by {money(owed - paid)}")
    form = "" if name in consent else ", no consent form"
    if name in consent and paid >= owed:
        going += 1
    print(f"{name:<5} paid {money(paid):>6}: {status}{form}")
print(f"{going} pupils cleared to go")
