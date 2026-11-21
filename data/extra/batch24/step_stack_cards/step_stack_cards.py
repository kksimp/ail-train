state = 404
def below(n):
    global state
    state = (state * 1103515245 + 12345) % 2147483648
    return (state // 65536) % n
def choose(hand, top, style):
    legal = [c for c in hand if abs(c - top) <= 2]
    if not legal: return -1
    if style == 0: return max(legal)
    if style == 1: return min(legal)
    return min(legal, key=lambda c: (abs(c - top), c))
deck = [v for k in range(3) for v in range(1, 11)]
for i in range(len(deck)):
    j = i + below(len(deck) - i)
    deck[i], deck[j] = deck[j], deck[i]
names = ["High", "Low", "Near"]
hands = [deck[0:5], deck[5:10], deck[10:15]]
top = deck[15]; next_card = 16; turn = 0
while all(hands) and turn < 60:
    p = turn % 3
    card = choose(hands[p], top, p)
    if card >= 0:
        hands[p].remove(card)
        top = card
    elif next_card < len(deck):
        hands[p].append(deck[next_card]); next_card += 1
    if p == 2:
        print(f"round {turn // 3 + 1:>2}: top {top:>2}, hand sizes {[len(h) for h in hands]}")
    turn += 1
for p in range(3):
    if not hands[p]: print(f"{names[p]} empties their hand first")
