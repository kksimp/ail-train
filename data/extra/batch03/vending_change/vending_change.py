stock = {200: 1, 100: 2, 50: 1, 20: 3, 10: 2, 5: 1}
def mc(a):
    left = a; used = []
    for c in [200, 100, 50, 20, 10, 5]:
        while left >= c and stock.get(c, 0) > 0: left -= c; stock[c] -= 1; used.append(c)
    if left:
        for c in used: stock[c] += 1
        return None
    return used
for p, d in [(120, 500), (95, 200), (70, 100), (45, 100), (60, 100)]:
    r = mc(d - p)
    print(f"price {p}, paid {d}: change {r}" if r is not None else f"price {p}, paid {d}: refused, cannot make {d - p}")
print("stock left: " + " ".join(f"{c}x{stock[c]}" for c in [200, 100, 50, 20, 10, 5]))
