bom = {"bike": [("frame", 1), ("wheel", 2), ("seat", 1), ("bolt", 6)], "wheel": [("rim", 1), ("spoke", 32), ("hub", 1)], "hub": [("bearing", 2), ("bolt", 1)]}
def explode(item, qty, gross):
    gross[item] = gross.get(item, 0) + qty
    for part, q in bom.get(item, []):
        explode(part, qty * q, gross)
on_hand = {"frame": 12, "wheel": 30, "seat": 80, "bolt": 150, "rim": 10, "spoke": 900, "hub": 4, "bearing": 40}
lots = {"bolt": 100, "spoke": 500, "bearing": 50}
gross = {}
explode("bike", 60, gross)
for part, g in gross.items():
    if part == "bike": continue
    have = on_hand.get(part, 0)
    net = g - have if g > have else 0
    lot = lots.get(part, 1)
    order = (net + lot - 1) // lot * lot
    print(f"{part:<8} gross {g:>5}, on hand {have:>4}, net {net:>5}, order {order:>5}")
