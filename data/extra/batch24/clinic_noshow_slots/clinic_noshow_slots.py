def hhmm(m): return f"{9 + m // 60}:{m % 60:02d}"
names = ["Abe", "Bea", "Col", "Dot", "Eve", "Fin", "Gwen", "Hank"]
late = [5, -10, 0, 99, 20, -5, 0, 35]
consult = [12, 20, 15, 0, 10, 18, 25, 12]
seen = [l == 99 for l in late]
now = 0; idle = 0; done = late.count(99)
while done < 8:
    pick = -1
    for i in range(8):
        if not seen[i] and i * 15 + late[i] <= now and i * 15 <= now:
            pick = i; break
    if pick < 0:
        now += 1; idle += 1; continue
    seen[pick] = True; done += 1
    print(f"{names[pick]:<5} slot {hhmm(pick * 15)}, seen {hhmm(now)}")
    now += consult[pick]
print(f"Dot did not come; doctor idle {idle} min, finished at {hhmm(now)}")
