mode = ("patrol", 1)
pos = 0; battery = 100; last = ""
for tick in range(60):
    if mode[0] == "patrol":
        battery -= 6
        d = mode[1]
        if pos + d < 0 or pos + d > 7: d = -d
        pos += d
        mode = ("homing", 0) if battery <= pos * 4 + 12 else ("patrol", d)
    elif mode[0] == "homing":
        battery -= 4
        pos -= 1
        mode = ("charging", 0) if pos == 0 else ("homing", 0)
    else:
        battery = min(battery + 25, 100)
        mode = ("patrol", 1) if battery == 100 else ("charging", 0)
    now = mode[0]
    if now != last:
        print(f"tick {tick:>2}: {now} at cell {pos}, battery {battery}%")
        last = now
