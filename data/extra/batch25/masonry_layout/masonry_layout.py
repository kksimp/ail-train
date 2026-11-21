def place(cards, cols, gap):
    tops = [0] * cols
    for name, h in cards:
        k = 0
        for i in range(1, cols):
            if tops[i] < tops[k]:
                k = i
        tops[k] += h + gap
    return tops

def show(xs):
    return "[" + ", ".join(str(x) for x in xs) + "]"

cards = [("sunset", 220), ("quote", 120), ("map", 340), ("portrait", 400), ("note", 90), ("chart", 260), ("poster", 380), ("ticket", 140), ("sketch", 200)]
cols = 3
gap = 20
tops = [0, 0, 0]
for name, h in cards:
    k = 0
    for i in range(1, cols):
        if tops[i] < tops[k]:
            k = i
    print(f"{name:<9} column {k + 1} at x={k * 320:>3} y={tops[k]:>3}")
    tops[k] += h + gap
robin = [0, 0, 0]
for i, (name, h) in enumerate(cards):
    robin[i % cols] += h + gap
best = place(cards, cols, gap)
print(f"shortest-first heights {show(best)}, tallest {max(best)}")
print(f"round-robin heights {show(robin)}, tallest {max(robin)}")
