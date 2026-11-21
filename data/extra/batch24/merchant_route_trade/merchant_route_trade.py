towns = ["A", "B", "C"]; goods = ["grain", "cloth"]
price = [[10, 40], [16, 31], [13, 48]]
gold = 300; cargo = -1; amount = 0
for leg in range(9):
    here = leg % 3; there = (leg + 1) % 3
    if cargo >= 0:
        gold += amount * price[here][cargo]
        price[here][cargo] -= amount // 5
    pick = -1; best = 0
    for g in range(2):
        margin = price[there][g] - price[here][g]
        if margin > best: best = margin; pick = g
    cargo = pick; amount = 0
    if pick >= 0:
        amount = min(20, gold // price[here][pick])
        gold -= amount * price[here][pick]
        price[here][pick] += amount // 5
        print(f"leg {leg + 1}: at {towns[here]} buy {amount} {goods[pick]} (markup {best}), gold {gold}")
    else:
        print(f"leg {leg + 1}: at {towns[here]} nothing worth carrying, gold {gold}")
if cargo >= 0: gold += amount * price[0][cargo]
print(f"back at A with {gold} gold; prices now {price}")
