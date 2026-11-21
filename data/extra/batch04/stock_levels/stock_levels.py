S = [["milk", 30, 40, 12, 9], ["bread", 25, 25, 8, 6], ["eggs", 18, 36, 10, 4]]
for d in range(1, 8):
    rf = []
    for s in S:
        s[1] -= min(s[1], s[4])
        if s[1] < s[3]: rf.append(f"{s[0]}+{s[2] - s[1]}"); s[1] = s[2]
    print(f"day {d}: " + (" ".join(rf) if rf else "no refills") if rf else f"day {d}: no refills")
print(" ".join(f"{s[0]}={s[1]}" for s in S))
