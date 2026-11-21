RANK = {"Critical": 0, "Normal": 1, "Batch": 2}

def admit(reqs, capacity):
    left = capacity
    shed = []
    for r in sorted(reqs, key=lambda q: RANK[q[1]]):
        if r[2] <= left:
            left -= r[2]
        else:
            shed.append(r[0])
    return shed

seconds = [[("login", "Critical", 2), ("feed", "Normal", 3), ("report", "Batch", 4)], [("export", "Batch", 5), ("pay", "Critical", 4), ("search", "Normal", 3), ("feed", "Normal", 3)], [("reindex", "Batch", 6), ("pay", "Critical", 4), ("login", "Critical", 2), ("feed", "Normal", 3), ("thumbs", "Batch", 1)]]
total_shed = 0
for i, reqs in enumerate(seconds):
    demand = sum(r[2] for r in reqs)
    shed = admit(reqs, 10)
    total_shed += len(shed)
    names = "none" if not shed else ", ".join(shed)
    print(f"second {i + 1}: demand {demand:>2}, shed {names}")
print(f"{total_shed} requests shed in total")
