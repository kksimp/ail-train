NAMES = ["Jab", "Slash", "Blast", "Focus"]
DMG = [3, 7, 12, 0]; COOL = [0, 2, 4, 3]
def gain(a, focused): return DMG[a] * 2 if focused and a != 3 else DMG[a]
def after(cds, a):
    out = [max(c - 1, 0) for c in cds]
    out[a] = COOL[a]
    return out
def best(left, cds, focused):
    if left == 0: return 0
    top = 0
    for a in range(4):
        if cds[a] == 0:
            top = max(top, gain(a, focused) + best(left - 1, after(cds, a), a == 3))
    return top
cds = [0, 0, 0, 0]; focused = False; plan = []; total = 0
for t in range(8):
    target = best(8 - t, cds, focused)
    for a in range(4):
        if cds[a] == 0 and gain(a, focused) + best(7 - t, after(cds, a), a == 3) == target:
            plan.append(NAMES[a]); total += gain(a, focused)
            cds = after(cds, a); focused = a == 3
            break
print(f"best:   {' '.join(plan)} = {total}")
g_cds = [0, 0, 0, 0]; greedy = []; g_total = 0
for t in range(8):
    pick = 0
    for a in range(3):
        if g_cds[a] == 0 and DMG[a] > DMG[pick]: pick = a
    greedy.append(NAMES[pick]); g_total += DMG[pick]
    g_cds = after(g_cds, pick)
print(f"greedy: {' '.join(greedy)} = {g_total}")
print(f"search gains {total - g_total} damage over greed")
