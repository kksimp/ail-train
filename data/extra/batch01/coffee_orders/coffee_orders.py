PRICES = {"S": 280, "M": 330, "L": 380}
def money(c):
    return f"{c // 100}.{c % 100:02d}"
orders = ["latte M", "flat white S", "latte L", "mocha M", "latte M", "tea S", "flat white M", "latte S", "mocha X"]
drinks = []
by_size = {}
for o in orders:
    cut = o.rfind(" ")
    drink, size = o[:cut], o[cut + 1:]
    price = PRICES.get(size, 0)
    if price == 0:
        print(f"unknown size in '{o}'")
        continue
    drinks.append(drink)
    by_size[size] = by_size.get(size, 0) + price
counts = {}
for d in drinks:
    counts[d] = counts.get(d, 0) + 1
print(f"kinds: {len(counts)}")
order = list(counts)
top = sorted(order, key=lambda k: (-counts[k], order.index(k)))[:2]
print("most ordered: " + ", ".join(top))
for size in ["S", "M", "L"]:
    print(f"{size}: {money(by_size.get(size, 0))}")
print(f"takings: {money(sum(by_size.values()))}")
