S = [("06:10", 370, 372), ("06:40", 400, 409), ("07:05", 425, -1), ("07:30", 450, 450), ("08:00", 480, 478), ("08:20", 500, 531), ("08:45", 525, 529)]
ot = ran = tl = 0
for n, p, a in S:
    if a < 0: print(f"{n}: cancelled"); continue
    ran += 1; l = max(a - p, 0); tl += l
    if l < 5: ot += 1; print(f"{n}: on time")
    else: print(f"{n}: {l} min late")
pc = ot * 1000 // len(S)
print(f"punctuality {pc // 10}.{pc % 10}% of {len(S)} planned, {tl} min late in total over {ran} trains")
