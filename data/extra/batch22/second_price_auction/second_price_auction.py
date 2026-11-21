def winner(b):
    best = 0
    for i in range(1, len(b)):
        if b[i] > b[best]:
            best = i
    return best

def second_value(v):
    w = winner(v)
    s = 0
    for i in range(len(v)):
        if i != w and v[i] > s:
            s = v[i]
    return s

auctions = [[120, 95, 80], [60, 150, 140, 70], [200, 90], [75, 85, 80, 90, 70]]
ts = 0
tf = 0
for k, vals in enumerate(auctions):
    n = len(vals)
    shaded = [v * (n - 1) // n for v in vals]
    w2 = winner(vals)
    pay2 = second_value(vals)
    w1 = winner(shaded)
    pay1 = shaded[w1]
    ts += pay2
    tf += pay1
    print(f"lot {k + 1}: values {vals}; second-price: bidder {w2 + 1} pays {pay2}; first-price bids {shaded}: bidder {w1 + 1} pays {pay1}")
print(f"revenue: second-price {ts}, first-price {tf}")
