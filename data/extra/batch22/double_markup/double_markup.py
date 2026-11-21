def retail_price(w):
    return (100 + w) // 2

def demand(p):
    return max(100 - p, 0)

best_p = 20
for p in range(20, 101):
    if (p - 20) * demand(p) > (best_p - 20) * demand(best_p):
        best_p = p
joint = (best_p - 20) * demand(best_p)
print(f"one firm: price {best_p}, sells {demand(best_p)}, profit {joint}")
best_w = 20
best_maker = 0
for half in range(10, 51):
    w = half * 2
    p = retail_price(w)
    maker = (w - 20) * demand(p)
    if half % 5 == 0:
        print(f"wholesale {w:>3}: shop price {p:>3}, sells {demand(p):>2}, maker {maker:>4}, shop {(p - w) * demand(p):>4}")
    if maker > best_maker:
        best_maker = maker
        best_w = w
p = retail_price(best_w)
shop = (p - best_w) * demand(p)
print(f"two firms: wholesale {best_w}, price {p}, total profit {best_maker + shop} against {joint}")
