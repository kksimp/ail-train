recipes = {"chilli": {"mince": 500, "beans": 400, "rice": 300, "onion": 2}, "risotto": {"rice": 350, "broth cube": 2, "onion": 1, "cheese": 80}, "stir fry": {"chicken": 400, "rice": 300, "pepper": 2}, "omelette": {"egg": 6, "cheese": 60, "pepper": 1}}
week = ["chilli", "stir fry", "omelette", "risotto", "chilli", "omelette", "stir fry"]
pantry = {"rice": 500, "onion": 3, "egg": 4}
packs = {"mince": [500, 450], "beans": [400, 65], "rice": [1000, 180], "onion": [3, 90], "broth cube": [8, 120], "cheese": [200, 250], "chicken": [600, 520], "pepper": [3, 140], "egg": [6, 200]}
need = {}
for meal in week:
    for item, qty in recipes[meal].items():
        need[item] = need.get(item, 0) + qty
cost = 0
for item, qty in need.items():
    missing = qty - pantry.get(item, 0)
    if missing <= 0:
        print(f"{item:<10} {qty:>5} needed, pantry has enough")
        continue
    p = packs[item]
    n = (missing + p[0] - 1) // p[0]
    cost += n * p[1]
    print(f"{item:<10} {qty:>5} needed, buy {n} x {p[0]} for {n * p[1] // 100}.{n * p[1] % 100:02}")
print(f"shopping total {cost // 100}.{cost % 100:02}")
