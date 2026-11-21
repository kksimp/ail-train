spots = [["F-01", "Frozen", 150, True], ["F-02", "Frozen", 200, True], ["C-01", "Chilled", 120, True], ["C-02", "Chilled", 180, False], ["A-01", "Ambient", 100, True], ["A-02", "Ambient", 160, True], ["A-03", "Ambient", 220, True]]
deadline = {"Frozen": "15 minutes", "Chilled": "30 minutes", "Ambient": "end of shift"}
pallets = [("P1", "Ambient", 140), ("P2", "Frozen", 130), ("P3", "Chilled", 150), ("P4", "Ambient", 90), ("P5", "Frozen", 190), ("P6", "Ambient", 150), ("P7", "Frozen", 120)]
for pid, temp, h in pallets:
    pick = -1
    for i, s in enumerate(spots):
        if s[3] and s[1] == temp and s[2] >= h:
            if pick == -1 or s[2] < spots[pick][2]:
                pick = i
    if pick == -1:
        print(f"{pid} (Temp.{temp}, {h} cm): no space, waits at the dock")
    else:
        spots[pick][3] = False
        print(f"{pid} (Temp.{temp}, {h} cm): {spots[pick][0]}, put away within {deadline[temp]}")
free = [s[0] for s in spots if s[3]]
quoted = ", ".join(free)
print(f"free spots left: {quoted}")
