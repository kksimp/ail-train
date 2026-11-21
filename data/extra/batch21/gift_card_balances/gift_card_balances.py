cards = {"GC100": [5000, 365], "GC200": [2500, 180], "GC300": [2000, 400], "GC400": [1500, 90]}
txns = [("GC100", 10, 2500), ("GC100", 40, 3000), ("GC200", 200, 1000), ("GC999", 12, 500), ("GC300", 50, 1999), ("GC100", 60, 100), ("GC400", 30, 700)]

def money(c):
    return f"{c // 100}.{c % 100:02d}"

def redeem(code, day, amount):
    if code not in cards:
        return None, f"unknown card {code}"
    card = cards[code]
    if day > card[1]:
        return None, f"{code} expired on day {card[1]}"
    if card[0] == 0:
        return None, f"{code} is empty"
    take = min(amount, card[0])
    card[0] -= take
    return take, None

for code, day, amount in txns:
    took, err = redeem(code, day, amount)
    if err is None:
        print(f"day {day:>3} {code}: took {money(took)}, customer pays {money(amount - took)} more")
    else:
        print(f"day {day:>3} refused: {err}")
lapsed = 0
for code, c in cards.items():
    print(f"{code}: {money(c[0])} left, expires day {c[1]}")
    if c[1] < 365:
        lapsed += c[0]
print(f"unspent on cards lapsing within the year: {money(lapsed)}")
