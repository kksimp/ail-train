bags = {"rook": [["rope", "lantern", "map"], 20], "wren": [["potion"], 55], "moss": [["sword", "shield"], 5]}
def trade(f, t, item, price):
    g, b = bags[f], bags[t]
    if item not in g[0]: return f"{f} has no {item}"
    if b[1] < price: return f"{t} cannot pay {price}"
    g[0].remove(item); g[1] += price; b[0].append(item); b[1] -= price
    return f"{t} buys {item} from {f} for {price}"
print(trade("rook", "wren", "lantern", 15))
print(trade("moss", "rook", "shield", 40))
print(trade("wren", "moss", "map", 10))
print(trade("moss", "wren", "sword", 30))
for n, b in bags.items(): print(f"{n}: {b[1]} gold, [{', '.join(b[0])}]")
print(f"gold in play: {sum(b[1] for b in bags.values())}")
