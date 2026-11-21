class Interval:
    def __init__(s, name, start, stop):
        s.name, s.start, s.stop = name, start, stop

raw = [Interval("i", 0, 9), Interval("sum", 1, 12), Interval("tmp", 2, 4), Interval("p", 3, 7), Interval("q", 5, 6), Interval("r", 8, 11), Interval("out", 10, 13)]
ivs = sorted(raw, key=lambda v: v.start)
reg = [-1] * len(ivs)
free = [1, 0]
active = []
spills = 0
for i in range(len(ivs)):
    keep = []
    for j in active:
        if ivs[j].stop < ivs[i].start:
            free.append(reg[j])
        else:
            keep.append(j)
    active = keep
    if not free:
        far = active[0]
        for j in active:
            if ivs[j].stop > ivs[far].stop:
                far = j
        spills += 1
        if ivs[far].stop > ivs[i].stop:
            reg[i] = reg[far]
            reg[far] = -1
            active = [j for j in active if j != far]
            active.append(i)
            print(f"at {ivs[i].start:>2}: spill {ivs[far].name}, give its register to {ivs[i].name}")
        else:
            print(f"at {ivs[i].start:>2}: spill {ivs[i].name}")
    else:
        reg[i] = free.pop()
        active.append(i)
for i in range(len(ivs)):
    place = "stack slot" if reg[i] < 0 else f"r{reg[i]}"
    print(f"{ivs[i].name:<4} [{ivs[i].start:>2}, {ivs[i].stop:>2}] -> {place}")
print(f"spills: {spills}")
