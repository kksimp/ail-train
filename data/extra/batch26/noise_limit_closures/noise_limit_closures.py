readings = [(6, 48), (8, 58), (12, 54), (18, 61), (22, 50), (23, 47), (2, 44), (3, 52)]
b = 0
for h, db in readings:
    day = 7 <= h < 23
    lim = 55 if day else 45
    loud = db > lim
    if loud: b += 1
    print(f"{h:02}:00 {db} dB (limit {lim}) {'BREACH' if loud else 'ok'}")
near = [r for r in readings if 7 <= r[0] < 23 and r[1] > 52 and r[1] <= 55]
print(f"breaches: {b}; near the day limit: {len(near)}")
