prices = [40.0, 32.0, 25.0, 32.0, 40.0, 50.0]
units = 0.0
spent = 0.0
for i, p in enumerate(prices):
    bought = 300.0 / p
    units += bought
    spent += 300.0
    print(f"month {i + 1}: price {p:.2f}, buys {bought:.4f} units, holding {units:.4f}")
avg_cost = spent / units
mean_price = 0.0
for p in prices:
    mean_price = mean_price + p
mean_price = mean_price / 6.0
last = prices[5]
print(f"average cost {avg_cost:.4f} against average price {mean_price:.4f}")
lump = spent / prices[0]
print(f"worth now: monthly {units * last:.2f}, lump sum in month 1 {lump * last:.2f}")
