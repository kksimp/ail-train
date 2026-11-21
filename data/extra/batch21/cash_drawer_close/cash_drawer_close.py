denoms = [5000, 2000, 1000, 500, 200, 100, 50, 20, 10, 5, 2, 1]
counts = [2, 9, 14, 11, 8, 23, 17, 30, 25, 14, 20, 33]
float_cents = 15000
sales = 38250

def money(c):
    sign = "-" if c < 0 else ""
    a = abs(c)
    return f"{sign}{a // 100}.{a % 100:02d}"

counted = sum(d * c for d, c in zip(denoms, counts))
takings = counted - float_cents
diff = takings - sales
label = "exact" if diff == 0 else ("over" if diff > 0 else "short")
print(f"counted {money(counted)}, float {money(float_cents)}, takings {money(takings)}")
print(f"sales record {money(sales)}: {label} by {money(abs(diff))}")
left = counted
bag = []
for i in range(len(denoms)):
    n = 0
    while counts[i] > 0 and left - denoms[i] >= float_cents:
        counts[i] -= 1
        left -= denoms[i]
        n += 1
    if n > 0:
        bag.append(f"{n} x {money(denoms[i])}")
print(f"bank: {', '.join(bag)}")
print(f"left in the drawer: {money(left)}")
