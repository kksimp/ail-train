def next_state(s):
    return (s * 1103515245 + 12345) % 2147483648

def call(v):
    return "higher" if v <= 7 else "lower"

def shuffled(seed):
    deck = [v for v in range(1, 14) for _ in range(4)]
    s = seed
    for i in range(51, 0, -1):
        s = next_state(s)
        j = (s >> 16) % (i + 1)
        deck[i], deck[j] = deck[j], deck[i]
    return deck

deck = shuffled(31)
print(f"first cards: [{', '.join(str(x) for x in deck[:12])}]")
streaks = []
run = right = 0
for k in range(1, len(deck)):
    prev, cur = deck[k - 1], deck[k]
    won = cur > prev if call(prev) == "higher" else cur < prev
    if won:
        run += 1
        right += 1
    else:
        if run > 0:
            streaks.append(run)
        run = 0
if run > 0:
    streaks.append(run)
print(f"{right} of 51 calls right")
print(f"{len(streaks)} streaks, best {max(streaks) if streaks else 0}")
print(f"streaks of five or more: {len([x for x in streaks if x >= 5])}")
