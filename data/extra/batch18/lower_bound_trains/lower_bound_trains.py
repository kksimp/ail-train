import bisect
trains = [(6, 15), (7, 5), (7, 40), (9, 0), (12, 30), (17, 45), (22, 10)]
def show(c): return f"{c[0]:02}:{c[1]:02}"
for now in [(5, 50), (7, 5), (13, 0), (23, 0)]:
    i = bisect.bisect_left(trains, now)
    if i < len(trains):
        w = (trains[i][0] * 60 + trains[i][1]) - (now[0] * 60 + now[1])
        print(f"at {show(now)}: next train {show(trains[i])}, wait {w} min")
    else: print(f"at {show(now)}: no more trains today")
fares = [8, 12, 12, 19, 25, 40]
for cap in [12, 20]:
    print(f"fares up to {cap}: {bisect.bisect_left(fares, cap + 1)} of {len(fares)}")
