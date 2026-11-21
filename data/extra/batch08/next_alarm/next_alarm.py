days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
alarms = [(0, 6, 30), (1, 6, 30), (2, 6, 30), (3, 6, 30), (4, 7, 0), (5, 9, 15)]
week = 7 * 24 * 60
for d, h, mi in [(0, 5, 0), (0, 6, 30), (4, 8, 0), (5, 10, 0), (6, 22, 45), (2, 23, 59)]:
    now = d * 1440 + h * 60 + mi; best = week + 1; pick = 0
    for i, a in enumerate(alarms):
        w = (a[0] * 1440 + a[1] * 60 + a[2] - now + week) % week; g = week if w == 0 else w
        if g < best: best = g; pick = i
    n = alarms[pick]; print(f"{days[d]} {h:02}:{mi:02} -> {days[n[0]]} {n[1]:02}:{n[2]:02} in {best // 60} h {best % 60} min")
