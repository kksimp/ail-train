def money(c): return f"{c // 100}.{c % 100:02}"
names = ["card", "transfer", "wallet"]
saved = 0
for price in [450, 1200, 2599, 9900, 300]:
    fees = [price * 14 // 1000 + 20, 35, max(price * 3 // 100, 10)]
    best = 0
    for i in range(1, 3):
        if fees[i] < fees[best]: best = i
    saved += max(fees) - fees[best]
    print(f"{money(price):>6}: fees {'/'.join(money(f) for f in fees)}, use {names[best]}")
print(f"saved {money(saved)} against the dearest choices")
