bids = [(120, "Ama"), (95, "Raj"), (150, "Liu"), (80, "Sven"), (110, "Noor"), (101, "Kai")]
s = sorted(bids, reverse=True)
w = s[:3]; price = s[3][0]
for a, n in w:
    print(f"{n} wins a ticket: bid {a}, pays {price}, saves {a - price}")
print(f"price set by the best losing bid: {price}")
print(f"revenue {price * 3}, {len(s) - 3} bidders miss out")
print(f"all bids high to low: {sorted([b[0] for b in bids], reverse=True)}")
