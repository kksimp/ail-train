S = [("boil water", 10, []), ("chop veg", 15, []), ("cook pasta", 12, ["boil water"]), ("make sauce", 20, ["chop veg"]), ("combine", 3, ["cook pasta", "make sauce"]), ("grate cheese", 5, []), ("serve", 2, ["combine", "grate cheese"])]
f = {}
for n, m, nd in S:
    st = max([f[x] for x in nd], default=0); f[n] = st + m
    print(f"{n:<13} starts {st:>2}, ends {st + m:>2}")
print(f"ready after {max(f.values())} minutes")
print(f"one step at a time it would take {sum(s[1] for s in S)}")
