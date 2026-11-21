route = [("Paris-Lille", 225, 300), ("tunnel", 50, 160), ("Kent line", 108, 186 * 1609 // 1000), ("London approach", 20, 60 * 1609 // 1000)]
train = 250; m = 0
for n, km, lim in route:
    run = min(train, lim) if train < lim else lim
    t = km * 60 // run; m += t
    print(f"{n:<16} limit {lim:>3} km/h, runs at {run:>3}, {t} min")
print(f"journey {m // 60} h {m % 60} min")
print(f"sections below the train's top speed: {sum(1 for r in route if r[2] < train)}")
