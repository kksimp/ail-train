def next_state(s):
    return (s * 1103515245 + 12345) % 2147483648

def shuffled(seed):
    deck = [v for v in range(1, 14) for _ in range(4)]
    s = seed
    for i in range(51, 0, -1):
        s = next_state(s)
        j = (s >> 16) % (i + 1)
        deck[i], deck[j] = deck[j], deck[i]
    return deck

def play(deck):
    piles = [[] for _ in range(13)]
    for i, c in enumerate(deck):
        piles[i % 13].append(c)
    cur = 12
    turned = kings = 0
    while piles[cur]:
        card = piles[cur].pop()
        turned += 1
        if card == 13:
            kings += 1
            if kings == 4:
                break
        cur = card - 1
    return turned

wins = 0
for seed in range(1, 9):
    n = play(shuffled(seed))
    if n == 52:
        wins += 1
    print(f"deal {seed}: {'WIN' if n == 52 else f'out after {n} cards'}")
print(f"{wins} of 8 deals come out")
