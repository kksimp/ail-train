levels = [(25, "bronze"), (50, "silver"), (100, "gold")]
log = [(1, "Ola", 12), (1, "Pip", 20), (1, "Raj", 8), (2, "Ola", 15), (2, "Pip", 9), (2, "Raj", 30), (3, "Ola", 30), (3, "Pip", 25), (3, "Raj", 4), (4, "Ola", 46), (4, "Pip", 3), (4, "Raj", 20)]
totals = {}
for week, who, n in log:
    before = totals.get(who, 0)
    after = before + n
    totals[who] = after
    for line, name in levels:
        if before < line <= after:
            print(f"week {week}: {who} earns {name} ({after} merits)")
for i, who in enumerate(sorted(totals, key=lambda k: -totals[k])):
    print(f"{i + 1}. {who} {totals[who]}")
