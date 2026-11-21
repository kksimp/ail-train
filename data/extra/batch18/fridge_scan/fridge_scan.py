sh = [[("yoghurt", 2), ("milk", 0), ("cream", 0)], [("ham", 3), ("cheese", 9)], [("salad", 0), ("chicken", -1), ("eggs", 12)], [("jam", 90)]]
today = []
for i, s in enumerate(sh):
    for n, d in s:
        if d == 0: today.append(f"shelf {i + 1}: {n}"); break
for t in today: print(f"use today, {t}")
chk = 0; found = "nothing"; done = False
for s in sh:
    for n, d in s:
        chk += 1
        if d < 0: found = n; done = True; break
    if done: break
print(f"first expired: {found} after checking {chk} items")
print(f"{sum(len(s) for s in sh)} items in the fridge")
