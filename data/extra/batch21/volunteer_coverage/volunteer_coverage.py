helpers = [("Abi", 9, 12), ("Ben", 10, 14), ("Cat", 12, 17), ("Dan", 9, 11), ("Eve", 13, 16), ("Fay", 15, 17), ("Gil", 11, 12)]
gaps = 0
for hour in range(9, 17):
    need = 3 if hour in (12, 13) else 2
    names = [h[0] for h in helpers if h[1] <= hour < h[2]]
    mark = "ok" if len(names) >= need else f"SHORT {need - len(names)}"
    if len(names) < need:
        gaps += 1
    print(f"{hour:02d}:00 {len(names)}/{need} {mark:<7} {' '.join(names)}")
print(f"{gaps} hours short of helpers")
longest = max(helpers, key=lambda h: h[2] - h[1])
total = sum(h[2] - h[1] for h in helpers)
print(f"{total} volunteer hours; longest shift {longest[0]} ({longest[2] - longest[1]} h)")
