state = 1337
print("six turns, mana equal to the turn, 300 shuffled games per deck")
def below(n):
    global state
    state = (state * 1103515245 + 12345) % 2147483648
    return (state // 65536) % n
def play_game(deck):
    cards = list(deck)
    for i in range(len(cards)):
        j = i + below(len(cards) - i)
        cards[i], cards[j] = cards[j], cards[i]
    hand = cards[0:4]
    wasted = 0; cast = 0
    for turn in range(1, 7):
        hand.append(cards[3 + turn])
        mana = turn
        while True:
            fits = [c for c in hand if c <= mana]
            if not fits: break
            dearest = max(fits)
            hand.remove(dearest)
            mana -= dearest; cast += 1
        wasted += mana
    return [wasted, cast]
decks = [("low curve", [1, 1, 1, 1, 2, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 5, 5, 6, 6]), ("high curve", [1, 1, 2, 2, 3, 3, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6, 7, 7, 7])]
for title, deck in decks:
    wasted = 0; cast = 0
    for g in range(300):
        r = play_game(deck)
        wasted += r[0]; cast += r[1]
    w = wasted / 300.0; c = cast / 300.0
    print(f"{title:<10}: {w:.3f} mana wasted of 21, {c:.3f} cards cast per game")
