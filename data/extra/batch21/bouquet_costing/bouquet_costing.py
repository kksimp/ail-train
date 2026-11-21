cost = {"rose": 90, "tulip": 45, "eucalyptus": 30, "lily": 120, "gypsophila": 25}
recipes = {"romance": [("rose", 12), ("gypsophila", 5)], "spring": [("tulip", 15), ("eucalyptus", 4)], "grand": [("lily", 5), ("rose", 6), ("eucalyptus", 6)]}
orders = {"romance": 3, "spring": 5, "grand": 2}

def retail(sc):
    raw = sc * 5 // 2 + 450
    return (raw + 49) // 50 * 50

def money(c):
    return f"{c // 100}.{c % 100:02d}"

stems = {}
takings = 0
for name, recipe in recipes.items():
    sc = sum(cost[f] * k for f, k in recipe)
    price = retail(sc)
    n = orders.get(name, 0)
    takings += price * n
    for f, k in recipe:
        stems[f] = stems.get(f, 0) + k * n
    print(f"{name:<8} stems {money(sc)}, sells at {money(price)}, {n} ordered")
wholesale = 0
for flower, need in stems.items():
    bunches = (need + 9) // 10
    wholesale += bunches * 10 * cost[flower]
    print(f"  {flower:<10} {need:>3} stems: {bunches} bunches, {bunches * 10 - need} spare")
print(f"takings {money(takings)}, flowers cost {money(wholesale)}")
