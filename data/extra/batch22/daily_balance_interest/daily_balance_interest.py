def money(c):
    return f"{c // 100}.{c % 100:02d}"

def interest(bd, apr):
    return bd * apr // (10000 * 365)

opening = 120000
moves = [(4, 35000), (10, -50000), (18, 12500), (25, 8000)]
bal = opening
bd = 0
for d in range(1, 31):
    for day, amt in moves:
        if day == d:
            bal += amt
    bd += bal
adb = bd // 30
paid = sum(a for _, a in moves if a < 0)
adjusted = opening + paid
print(f"opening {money(opening)}, closing {money(bal)}, average daily {money(adb)}")
print(f"average daily balance method: {money(interest(bd, 1899))}")
print(f"adjusted balance method:      {money(interest(adjusted * 30, 1899))}")
print(f"previous balance method:      {money(interest(opening * 30, 1899))}")
