import sys
M = 2147483648
def deal(seed, players, cards):
    deck = [r + s for s in "SHDC" for r in "A23456789TJQK"]
    state = seed % M
    for i in range(51, 0, -1):
        state = (state * 1103515245 + 12345) % M
        j = state % (i + 1)
        deck[i], deck[j] = deck[j], deck[i]
    hands = [[] for _ in range(players)]
    pos = 0
    for _ in range(cards):
        for p in range(players):
            hands[p].append(deck[pos])
            pos += 1
    return hands, 52 - pos
lines = sys.stdin.read().split("\n")
if lines and lines[-1] == "":
    lines.pop()
for k, line in enumerate(lines, 1):
    w = line.split()
    try:
        if len(w) != 3:
            raise ValueError
        seed, players, cards = map(int, w)
        if seed < 0 or players < 1 or cards < 1 or players * cards > 52:
            raise ValueError
    except ValueError:
        print("deal %d: bad request" % k)
        continue
    hands, left = deal(seed, players, cards)
    print("deal %d" % k)
    for p, h in enumerate(hands, 1):
        print("P%d: %s" % (p, " ".join(h)))
    print("left=%d" % left)
