def clock(seconds):
    return f"{seconds // 3600}:{seconds // 60 % 60:02}:{seconds % 60:02}"

def gap(seconds):
    return f"+{seconds // 60}:{seconds % 60:02}"

riders = ["Aru", "Bernal", "Cort", "Dumoulin"]
stages = [[17520, 17514, 17530, 17514], [14402, 14450, 14380, 14395], [20110, 20025, 20090, 20160], [9030, 9041, 9022, 9030]]
bonus = [10, 6, 4]
gc = [0, 0, 0, 0]
for si, st in enumerate(stages):
    order = sorted([0, 1, 2, 3], key=lambda i: (st[i], i))
    for i in range(4):
        gc[i] += st[i]
    for k in range(3):
        gc[order[k]] -= bonus[k]
    leader = sorted([0, 1, 2, 3], key=lambda i: (gc[i], i))[0]
    print(f"after stage {si + 1}: {riders[order[0]]} wins, {riders[leader]} leads in {clock(gc[leader])}")
final_order = sorted([0, 1, 2, 3], key=lambda i: (gc[i], i))
best = gc[final_order[0]]
for place, i in enumerate(final_order):
    shown = clock(gc[i]) if place == 0 else gap(gc[i] - best)
    print(f"{place + 1}. {riders[i]:<9} {shown}")
