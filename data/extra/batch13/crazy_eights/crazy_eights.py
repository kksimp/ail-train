FACES = "A23456789TJQK"

def parse(s):
    return (FACES.find(s[0]) + 1, s[1])

def label(c):
    return f"{FACES[c[0] - 1]}{c[1]}"

def choose(hand, top, suit):
    best = -1
    for i, c in enumerate(hand):
        if c[0] != 8 and (c[1] == suit or c[0] == top[0]):
            if best < 0 or c[0] > hand[best][0]:
                best = i
    if best >= 0:
        return f"play {label(hand[best])}"
    for c in hand:
        if c[0] == 8:
            counts = {}
            for d in hand:
                if d[0] != 8:
                    counts[d[1]] = counts.get(d[1], 0) + 1
            pick = c[1]
            most = 0
            for s, n in counts.items():
                if n > most:
                    pick = s
                    most = n
            return f"play {label(c)} and call {pick}"
    return "draw a card"

situations = [("9H", 'H', "3H KH 9C 2S"), ("5C", 'C', "5D 8S JH QH"), ("TD", 'D', "2S 3S 4C"), ("8S", 'H', "4H 8D AH 7C"), ("QS", 'S', "8H 2D 4D 9D JC"), ("7C", 'C', "7H 7S KC")]
for top, suit, cards in situations:
    hand = [parse(x) for x in cards.split(" ")]
    print(f"top {top}, suit {suit}, hand {cards}: {choose(hand, parse(top), suit)}")
