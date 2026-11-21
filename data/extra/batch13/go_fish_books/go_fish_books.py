def pick_rank(hand):
    best = hand[0]
    for c in hand:
        n = hand.count(c)
        m = hand.count(best)
        if n > m or (n == m and c < best):
            best = c
    return best

deck = [i % 13 + 1 for i in range(52)]
seed = 2024
i = 51
while i > 0:
    seed = (seed * 1103515245 + 12345) % 2147483648
    j = seed % (i + 1)
    deck[i], deck[j] = deck[j], deck[i]
    i -= 1
names = ["Ana", "Ben"]
hands = [deck[0:7], deck[7:14]]
top = 14
books = [0, 0]
p = 0
turn = 0
while turn < 40 and len(hands[0]) > 0 and len(hands[1]) > 0:
    turn += 1
    o = 1 - p
    r = pick_rank(hands[p])
    got = hands[o].count(r)
    again = False
    mine = list(hands[p])
    if got > 0:
        hands[o] = [x for x in hands[o] if x != r]
        for k in range(got):
            mine.append(r)
        again = True
    elif top < len(deck):
        drawn = deck[top]
        top += 1
        mine.append(drawn)
        again = drawn == r
    for b in range(1, 14):
        if mine.count(b) == 4:
            mine = [x for x in mine if x != b]
            books[p] += 1
            print(f"turn {turn:>2}: {names[p]} lays down a book of {b}s")
    hands[p] = mine
    if not again:
        p = o
print(f"after {turn} turns, {len(deck) - top} cards left to draw")
for k in range(2):
    print(f"{names[k]}: {books[k]} books, {len(hands[k])} cards in hand")
