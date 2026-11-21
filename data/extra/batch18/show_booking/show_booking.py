seats = {"Hamlet": 8, "Cats": 3, "Gaslight": 20}; booked = 0
for show, n in [("Hamlet", 4), ("Cats", 2), ("Cats", 2), ("Grease", 2), ("Gaslight", 9), ("Hamlet", 4), ("Hamlet", 1)]:
    if n > 6: print(f"{n} for {show}: at most 6 seats per booking"); continue
    if show not in seats: print(f"{n} for {show}: no show called {show}"); continue
    if seats[show] < n: print(f"{n} for {show}: {show} is sold out"); continue
    seats[show] -= n; booked += n; print(f"{n} for {show}: ok, {seats[show]} left")
print(f"{booked} seats booked")
for s, l in seats.items(): print(f"{s}: {l} free")
