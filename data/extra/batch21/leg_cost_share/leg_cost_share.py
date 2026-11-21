def money(c):
    return f"{c // 100}.{c % 100:02d}"

legs = [("Hilltown", "Ayr", 54, ["Owen"]), ("Ayr", "Girvan", 34, ["Owen", "Pia"]), ("Girvan", "Stranraer", 49, ["Owen", "Pia", "Quin"]), ("Stranraer", "Newton", 72, ["Pia", "Quin"]), ("Newton", "Hilltown", 61, [])]
owes = {"Nia": 0}
for f, t, km, riders in legs:
    cost = km * 12
    n = len(riders) + 1
    each = cost // n
    owes["Nia"] += cost - each * (n - 1)
    for r in riders:
        owes[r] = owes.get(r, 0) + each
    print(f"{f} to {t}, {km} km: {money(cost)} for {n}, {money(each)} each")
total = 0
for who, c in owes.items():
    total += c
    print(f"{who:<5} {money(c):>6}")
print(f"trip fuel {money(total)}")
