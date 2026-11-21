def reply(rival): return rival - 2 if rival - 2 > 12 else 30
prices = [30, 28]
profit = [0, 0]
for day in range(1, 14):
    mover = day % 2
    prices[mover] = reply(prices[1 - mover])
    a, b = prices
    buyers = [50, 50]
    if a < b: buyers = [100, 0]
    elif b < a: buyers = [0, 100]
    for s in range(2): profit[s] += buyers[s] * (prices[s] - 10)
    winner = "A" if a < b else "B" if b < a else "both"
    print(f"day {day:>2}: A {a}, B {b} -> {winner}")
print(f"profit A {profit[0]}, B {profit[1]}")
