def grow(v, pct):
    return v * (100 + pct) // 100

rent = 1500
invested = 60000
rent_paid = 0
value = 300000
owed = 240000
own_paid = 60000
payment = 17268
first_ahead = 0
for year in range(1, 11):
    rent_paid += rent * 12
    rent = grow(rent, 3)
    invested = grow(invested, 5)
    upkeep = value * 15 // 1000
    own_paid += payment + upkeep
    owed = owed + owed * 6 // 100 - payment
    value = grow(value, 3)
    renter = invested - rent_paid
    owner = value - owed - own_paid
    if owner > renter and first_ahead == 0:
        first_ahead = year
    if year % 2 == 0:
        print(f"year {year:>2}: renter net {renter:>8}, owner net {owner:>8}, owed {owed}")
if first_ahead > 0:
    print(f"buying pulls ahead in year {first_ahead}")
else:
    print("renting stays ahead for all ten years")
