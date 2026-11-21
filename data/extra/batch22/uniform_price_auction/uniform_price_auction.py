bids = [["A", 99, 30, 0], ["B", 98, 25, 0], ["C", 97, 20, 0], ["D", 97, 30, 0], ["E", 96, 40, 0], ["F", 97, 7, 0]]
left = 100
clearing = 0
levels = sorted([b[1] for b in bids])[::-1]
seen = set()
for p in levels:
    if p in seen or left == 0:
        seen.add(p)
        continue
    seen.add(p)
    demand = sum(b[2] for b in bids if b[1] == p)
    clearing = p
    if demand <= left:
        for b in bids:
            if b[1] == p:
                b[3] = b[2]
        left -= demand
    else:
        handed = 0
        for b in bids:
            if b[1] == p:
                b[3] = left * b[2] // demand
                handed += b[3]
        spare = left - handed
        for b in bids:
            if b[1] == p and spare > 0 and b[3] < b[2]:
                b[3] += 1
                spare -= 1
        left = 0
as_bid = 0
for b in bids:
    as_bid += b[3] * b[1]
    print(f"{b[0]} bid {b[2]:>2} at {b[1]}: gets {b[3]:>2}")
sold = 100 - left
print(f"clearing price {clearing}: uniform revenue {sold * clearing}, pay-as-bid revenue {as_bid}")
