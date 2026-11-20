def report(stock):
    return " ".join(f"{k}={stock[k]}" for k in sorted(stock))

def sell(stock, item, qty):
    have = stock.get(item)
    if have is None or have < qty:
        return "false"
    if have == qty:
        del stock[item]
    else:
        stock[item] = have - qty
    return "true"

stock = {"tea": 4, "jam": 1}
stock["tea"] = stock.get("tea", 0) + 6
stock["oats"] = stock.get("oats", 0) + 2
print(report(stock))
print(sell(stock, "jam", 1))
print(sell(stock, "jam", 1))
print(sell(stock, "tea", 99))
print(sell(stock, "tea", 3))
print(report(stock))
print("false")
print(0)
print(len(stock))
visits = {}
for who in ["ann", "bob", "ann", "ann"]:
    visits[who] = visits.get(who, 0) + 1
print(report(visits))
