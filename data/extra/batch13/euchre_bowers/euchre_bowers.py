def suit_of(c):
    return {"H": "Hearts", "D": "Diamonds", "C": "Clubs"}.get(c, "Spades")

def same_colour(s):
    return {"Hearts": "Diamonds", "Diamonds": "Hearts", "Clubs": "Spades", "Spades": "Clubs"}[s]

def rank_value(card):
    return "9TJQKA".find(card[0])

def effective(card, trump):
    s = suit_of(card[1])
    return trump if card.startswith("J") and s == same_colour(trump) else s

def power(card, trump, led):
    s = suit_of(card[1])
    if card.startswith("J") and s == trump:
        return 100
    if card.startswith("J") and s == same_colour(trump):
        return 99
    eff = effective(card, trump)
    if eff == trump:
        return 50 + rank_value(card)
    if eff == led:
        return 10 + rank_value(card)
    return 0

trump = "Hearts"
print(f"trumps: Suit.{trump}")
tricks = [["9H", "AD", "JD", "KH"], ["AC", "KC", "9C", "TC"], ["JD", "QH", "AH", "9S"], ["QS", "AS", "TH", "JH"], ["KD", "9D", "TS", "QD"]]
for t in tricks:
    led = effective(t[0], trump)
    best = 0
    for i in range(1, 4):
        if power(t[i], trump, led) > power(t[best], trump, led):
            best = i
    cards = " ".join(t)
    print(f"{cards}: led Suit.{led}, won by {t[best]} (power {power(t[best], trump, led)})")
