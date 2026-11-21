cards = 1200000
price = 200
prizes = [(2000000, 2), (100000, 30), (10000, 1200), (2000, 24000), (500, 60000), (200, 150000)]
paid = winners = 0
for amount, count in prizes:
    paid += amount * count
    winners += count
    print(f"{amount // 100:>6}: {count:>6} prizes, 1 in {cards // count}")
ev = float(paid) / float(cards) / 100.0
back = paid * 1000 // (cards * price)
odds = float(cards) / float(winners)
print(f"expected prize per card {ev:.2f} on a 2.00 stake")
print(f"paid back {back // 10}.{back % 10}% of stakes")
print(f"odds of any prize: 1 in {odds:.2f}")
small = sum(c for a, c in prizes if a <= price)
print(f"{small * 100 // winners}% of wins only give the stake back or less")
