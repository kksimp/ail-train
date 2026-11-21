rooms = [("main hall", 240, [110, 110, 90]), ("studio", 64, [90]), ("bar", 85, [80, 75]), ("garden room", 150, [120])]
layouts = [("standing", 5), ("theatre", 8), ("banquet", 12)]
print("room         standing  theatre  banquet")
limited = 0
for name, area, exits in rooms:
    cells = []
    for lname, tenths in layouts:
        by_area = area * 10 // tenths
        cap = min(by_area, sum(exits))
        flag = "*" if cap < by_area else " "
        if cap < by_area:
            limited += 1
        cells.append(f"{cap:>7}{flag}")
    print(f"{name:<12} {' '.join(cells).rstrip()}")
print(f"* exits limit the number ({limited} cases)")
