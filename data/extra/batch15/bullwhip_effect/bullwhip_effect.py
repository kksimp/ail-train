def variance(xs):
    n = float(len(xs)); mean = float(sum(xs)) / n
    acc = 0.0
    for x in xs: acc = acc + (float(x) - mean) * (float(x) - mean)
    return acc / n
def pass_up(d):
    orders = [d[0]]
    for t in range(1, len(d)):
        o = d[t] + (d[t] - d[t - 1])
        orders.append(0 if o < 0 else o)
    return orders
shop = [100, 104, 98, 102, 110, 106, 100, 95, 101, 108, 103, 99]
tiers = ["shop sales", "retailer orders", "wholesaler orders", "factory orders"]
flow = shop
for i, name in enumerate(tiers):
    if i > 0: flow = pass_up(flow)
    v = variance(flow)
    print(f"{name:<18} variance {v:>8.1f}  {flow}")
