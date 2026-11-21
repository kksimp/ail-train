def deal_round(cards, chosen):
    piles = [[], [], []]
    for i, c in enumerate(cards):
        piles[i % 3].append(c)
    k = 0
    for p in range(3):
        if chosen in piles[p]:
            k = p
    others = [p for p in range(3) if p != k]
    return piles[others[0]] + piles[k] + piles[others[1]]

def after_three(chosen):
    cards = list(range(1, 22))
    where = []
    for r in range(3):
        cards = deal_round(cards, chosen)
        where.append(cards.index(chosen) + 1)
    return where

def show(xs):
    return "[" + ", ".join(str(x) for x in xs) + "]"

print(f"card 5 moves to places {show(after_three(5))} after each deal")
print(f"card 19 moves to places {show(after_three(19))} after each deal")
ok = all(after_three(c)[2] == 11 for c in range(1, 22))
print(f"every card ends 11th: {'true' if ok else 'false'}")
