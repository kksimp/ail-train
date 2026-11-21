def rank_of(card):
    return "A23456789TJQK".find(card[0]) + 1

def points(rank):
    return 10 if rank >= 10 else rank

def classify(cards):
    if len(cards) < 3:
        return None, "too few cards"
    ranks = [rank_of(c) for c in cards]
    suits = set(c[1] for c in cards)
    if all(r == ranks[0] for r in ranks):
        if len(suits) != len(cards) or len(cards) > 4:
            return None, "repeated suit"
        return ("group", ranks[0]), None
    if len(suits) != 1:
        return None, "mixed ranks and suits"
    order = sorted(ranks)
    for i in range(1, len(order)):
        if order[i] != order[i - 1] + 1:
            return None, "gap in run"
    return ("run", order[0], order[-1]), None

melds = ["7H 7S 7D", "4C 5C 6C 7C", "QD KD JD", "9S 9S 9H", "2H 3H 5H", "AS 2S 3S", "8C 8D", "TH JS QH"]
total = 0
for line in melds:
    cards = line.split(" ")
    m, err = classify(cards)
    if m is not None:
        text = f"group of rank {m[1]}" if m[0] == "group" else f"run from {m[1]} to {m[2]}"
        value = sum(points(rank_of(c)) for c in cards)
        total += value
        print(f"{line}: {text}, worth {value}")
    else:
        print(f"{line}: invalid, {err}")
print(f"points in valid melds: {total}")
