patches = [["clover", 60, 2, 10], ["heather", 120, 3, 10], ["lime", 40, 5, 10]]
stored = 0
for r in range(1, 9):
    haul = []
    for p in patches:
        got = min(p[1], p[3])
        p[1] -= got
        haul.append(got)
        stored += got
    worst = -1; best = -1
    for i in range(3):
        if patches[i][3] >= 5 and (worst < 0 or haul[i] * patches[worst][3] < haul[worst] * patches[i][3]):
            worst = i
        if best < 0 or haul[i] * patches[i][2] > haul[best] * patches[best][2]:
            best = i
    if worst != best:
        patches[worst][3] -= 5
        patches[best][3] += 5
    print(f"round {r}: haul {haul}, bees now {[p[3] for p in patches]}")
print(f"stored {stored}, nectar left {[p[1] for p in patches]}")
