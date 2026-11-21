def tier_price(n):
    return 1500 if n <= 10 else (1200 if n <= 50 else 900)

def graduated(s):
    return sum(tier_price(i) for i in range(1, s + 1))

def volume(s):
    return s * tier_price(s)

for n in [8, 10, 11, 40, 45, 50, 51, 120]:
    print(f"{n:>3} seats: graduated {graduated(n) // 100:>5}, volume {volume(n) // 100:>5}")
cheapest = 45
for n in range(45, 61):
    if volume(n) < volume(cheapest):
        cheapest = n
print(f"for at least 45 seats, volume pricing is cheapest at {cheapest} seats")
