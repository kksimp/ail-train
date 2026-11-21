def evolve(s):
    v = ((s * 32) ^ s) % 1048576
    v = ((v // 16) ^ v) % 1048576
    return ((v * 512) ^ v) % 1048576

traders = [1, 10, 100, 2024]
total = 0; sales = {}
for t in traders:
    s = t; prices = [s % 10]
    for _ in range(500):
        s = evolve(s); prices.append(s % 10)
    print(f"trader {t}: 500th secret {s}")
    total += s
    first = set()
    for i in range(4, len(prices)):
        key = f"{prices[i - 3] - prices[i - 4]},{prices[i - 2] - prices[i - 3]},{prices[i - 1] - prices[i - 2]},{prices[i] - prices[i - 1]}"
        if key not in first:
            first.add(key)
            sales[key] = sales.get(key, 0) + prices[i]
print(f"part 1: sum of secrets {total}")
best = max(sales, key=lambda k: sales[k])
print(f"part 2: changes {best} sell for {sales[best]}")
print(f"{len(sales)} distinct change runs seen")
