ship_day = 100
lots = [["L1", 120, 40], ["L2", 135, 25], ["L3", 150, 60], ["L4", 128, 30], ["L5", 170, 50]]
lots.sort(key=lambda l: l[1])
orders = [("market", 50, 10), ("hospital", 45, 30), ("export", 40, 60), ("market", 30, 10), ("export", 20, 60)]
for who, want, life in orders:
    need = want
    picks = []
    for l in lots:
        if need > 0 and l[2] > 0 and l[1] - ship_day >= life:
            take = min(need, l[2])
            l[2] -= take
            need -= take
            picks.append(f"{l[0]} x{take}")
    joined = ", ".join(picks)
    short = f", short {need}" if need > 0 else ""
    print(f"{who:<8} {want} with {life}+ days left: {joined}{short}")
left = [f"{l[0]}:{l[2]}" for l in lots if l[2] > 0]
print(f"left: {' '.join(left)}")
