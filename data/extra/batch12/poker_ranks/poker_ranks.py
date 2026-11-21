def value(c):
    return {'T': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}.get(c, int(c) if c.isdigit() else 0)

def score(hand):
    cards = hand.split(" ")
    vals = sorted([value(c[0]) for c in cards], reverse=True)
    suit_set = set(c[1] for c in cards)
    counts = {}
    for v in vals:
        counts[v] = counts.get(v, 0) + 1
    order = sorted(counts.keys(), key=lambda k: (-counts[k], -k))
    flush = len(suit_set) == 1
    straight = len(counts) == 5 and vals[0] - vals[4] == 4
    top = counts[order[0]]
    if straight and flush: cat = 8
    elif top == 4: cat = 7
    elif top == 3 and len(counts) == 2: cat = 6
    elif flush: cat = 5
    elif straight: cat = 4
    elif top == 3: cat = 3
    elif top == 2 and len(counts) == 3: cat = 2
    elif top == 2: cat = 1
    else: cat = 0
    return [cat] + order

names = ["high card", "pair", "two pair", "three of a kind", "straight", "flush", "full house", "four of a kind", "straight flush"]
players = [("Ivy", "KH KD 7S 7C 2H"), ("Jon", "9C TC JC QC KC"), ("Kim", "3D 3S 3H 9C 9D"), ("Lee", "AS 4S 9S JS 2S"), ("Max", "5H 6D 7S 8C 9H"), ("Ned", "KS KC 7D 7H AH")]
best_name = ""
best = [-1]
for who, hand in players:
    s = score(hand)
    print(f"{who}: {hand} is {names[s[0]]} {s}")
    if s > best:
        best = s
        best_name = who
print(f"winner: {best_name}")
