def pts(c): return 11 if c == "A" else 10 if c in ("K", "Q", "J") else int(c)
def hand(cards):
    t = sum(pts(c) for c in cards); aces = cards.count("A")
    while t > 21 and aces > 0: t -= 10; aces -= 1
    s = " ".join(cards)
    if t > 21: return f"{s}: {t} bust"
    if t == 21 and len(cards) == 2: return f"{s}: blackjack"
    if aces > 0: return f"{s}: soft {t}"
    return f"{s}: {t}"
for h in [["A", "K"], ["A", "6"], ["A", "6", "9"], ["10", "7", "5"], ["A", "A", "9"], ["5", "4", "A", "A"], ["Q", "J"], ["7", "7", "7"]]: print(hand(h))
