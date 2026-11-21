def next_state(s):
    return (s * 1103515245 + 12345) % 2147483648

def best_mask(table, need):
    best = [0, 0]
    for mask in range(1, 1 << len(table)):
        total = n = 0
        for b in range(len(table)):
            if ((mask >> b) & 1) == 1:
                total += table[b]
                n += 1
        if total == need and n > best[1]:
            best = [mask, n]
    return best

deck = [k // 4 + 1 for k in range(40)]
s = 77
i = len(deck) - 1
while i > 0:
    s = next_state(s)
    j = (s >> 16) % (i + 1)
    deck[i], deck[j] = deck[j], deck[i]
    i -= 1
table = deck[:4]
pos = 4
hands = [[], []]
score = [0, 0]
turn = 0
while True:
    if not hands[0] and not hands[1]:
        if pos >= len(deck):
            break
        for p in range(2):
            hands[p] = deck[pos:pos + 3]
            pos += 3
    hand = hands[turn]
    pick, cap = -1, [0, 0]
    for h, card in enumerate(hand):
        m = best_mask(table, 15 - card)
        if m[1] > cap[1]:
            pick, cap = h, m
    if pick < 0:
        low = hand.index(min(hand))
        table.append(hand[low])
        hands[turn].pop(low)
    else:
        table = [table[b] for b in range(len(table)) if ((cap[0] >> b) & 1) == 0]
        hands[turn].pop(pick)
        score[turn] += cap[1] + 1
    turn = 1 - turn
winner = "North" if score[0] > score[1] else ("South" if score[1] > score[0] else "nobody")
print(f"North took {score[0]} cards, South {score[1]}")
print(f"left on the table: [{', '.join(str(x) for x in table)}]")
print(f"winner: {winner}")
