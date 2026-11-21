def sweep(levels, qty):
    left = qty
    cost = 0
    for p, q in levels:
        take = min(q, left)
        cost += take * p
        left -= take
    return cost

levels = [[10010, 300], [10015, 250], [10020, 400], [10030, 500], [10050, 800]]
best = float(levels[0][0])
for qty in [200, 700, 1200, 1900]:
    cost = sweep(levels, qty)
    vwap = float(cost) / float(qty)
    slip = (vwap - best) / best * 10000.0
    price = vwap / 100.0
    print(f"buy {qty:>4}: cost {cost // 100}, average price {price:.4f}, slippage {slip:.2f} bp")
