def trip(depart, spots, offsets):
    t = depart; stops = 0; at = 0
    for i in range(len(spots)):
        t += (spots[i] - at) // 10
        at = spots[i]
        phase = (t - offsets[i] + 600) % 60
        if phase >= 30:
            t += 60 - phase; stops += 1
    return [t - depart, stops]
spots = [0, 300, 650, 900, 1300]
print("five lights, green 30 s of each 60, one car departing each second for a minute")
plans = [("all at zero", [0, 0, 0, 0, 0]), ("green wave", [(s // 10) % 60 for s in spots])]
for title, offsets in plans:
    total = 0; stops = 0
    for depart in range(60):
        r = trip(depart, spots, offsets)
        total += r[0]; stops += r[1]
    mean = total / 60.0
    print(f"{title:<11} offsets {offsets}: mean trip {mean:.2f} s, {stops} stops for 60 cars")
