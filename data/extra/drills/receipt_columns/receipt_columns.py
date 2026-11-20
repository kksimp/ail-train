def center(s, w, fill):
    if len(s) >= w:
        return s
    left = (w - len(s)) // 2
    return fill * left + s + fill * (w - len(s) - left)

def money(cents):
    return f"{cents // 100}.{str(cents % 100).rjust(2, '0')}"

def row(name, qty, cents):
    return name.ljust(12, '.') + str(qty).rjust(3) + money(qty * cents).rjust(8)

items = [("tea", 2, 349), ("oat biscuits", 1, 205), ("jam", 12, 99)]
print("[" + center("RECEIPT", 23, '=') + "]")
total = 0
for name, qty, cents in items:
    print(row(name, qty, cents))
    total += qty * cents
print("-" * 23)
print("total".ljust(15) + money(total).rjust(8))
print("[" + center("ok", 5, '*') + "]")
