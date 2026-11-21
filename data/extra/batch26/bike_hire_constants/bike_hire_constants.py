def fare(mins, ebike, member):
    rate = 25 if ebike else 15
    paid = max(mins - 10, 0) if member else mins
    return min(100 + paid * rate, 1500)
m = lambda c: f"{c // 100}.{c % 100:02}"
total = 0; capped = 0
rides = [(12, False, False), (12, False, True), (45, True, False), (70, True, True), (8, False, True)]
for mins, e, mem in rides:
    f = fare(mins, e, mem)
    if f == 1500: capped += 1
    total += f
    print(f"{mins:>3} min {'e-bike' if e else 'bike':<6} {'member' if mem else 'guest':<6} {m(f):>6}")
print(f"{len(rides)} rides, {m(total)} in all, {capped} at the {m(1500)} cap")
