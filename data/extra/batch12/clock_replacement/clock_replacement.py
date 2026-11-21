def show(frames, used, hand):
    parts = []
    for i in range(len(frames)):
        p = "-" if frames[i] < 0 else f"{frames[i]}"
        star = "*" if used[i] else ""
        arrow = ">" if i == hand else " "
        parts.append(f"{arrow}{p}{star}")
    return " ".join(parts)

refs = [1, 2, 3, 4, 1, 2, 5, 1, 2, 3, 4, 5, 2]
frames = [-1, -1, -1, -1]
used = [False] * 4
hand = 0
faults = 0
for p in refs:
    at = frames.index(p) if p in frames else -1
    if at >= 0:
        used[at] = True
        print(f"{p:>2} hit    {show(frames, used, hand)}")
        continue
    faults += 1
    while used[hand]:
        used[hand] = False
        hand = (hand + 1) % len(frames)
    frames[hand] = p
    used[hand] = True
    hand = (hand + 1) % len(frames)
    print(f"{p:>2} fault  {show(frames, used, hand)}")
print(f"{faults} faults for {len(refs)} references")
