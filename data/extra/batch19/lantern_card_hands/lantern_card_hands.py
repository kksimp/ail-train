def kind(cards, wild):
    counts = {}; jokers = 0
    for c in cards:
        if wild and c == 'J': jokers += 1
        else: counts[c] = counts.get(c, 0) + 1
    sizes = sorted(counts.values(), reverse=True) or [0]
    sizes[0] += jokers
    if sizes[0] == 5: return 6
    if sizes[0] == 4: return 5
    if sizes[0] == 3: return 4 if sizes[1] == 2 else 3
    if sizes[0] == 2: return 2 if sizes[1] == 2 else 1
    return 0

def strength(cards, wild):
    order = "J23456789TQKA" if wild else "23456789TJQKA"
    s = kind(cards, wild)
    for c in cards:
        s = s * 15 + order.find(c)
    return s

def winnings(hands, wild):
    ranked = sorted(hands, key=lambda h: strength(h.split(" ")[0], wild))
    return sum((i + 1) * int(h.split(" ")[1]) for i, h in enumerate(ranked))

hands = ["KTJJT 220", "Q2Q2Q 15", "T3T3J 340", "A98J7 61", "55J55 503", "2345A 7"]
for h in hands:
    cards = h.split(" ")[0]
    print(f"{cards}: kind {kind(cards, False)}, with jokers {kind(cards, True)}")
print(f"part 1: winnings {winnings(hands, False)}")
print(f"part 2: winnings {winnings(hands, True)}")
