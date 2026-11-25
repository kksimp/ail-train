import sys

VAL = {str(i): i for i in range(2, 10)}
for t in "TJQK":
    VAL[t] = 10
VAL["A"] = 11

for line in sys.stdin.read().splitlines():
    cards = line.split()
    if not cards:
        continue
    text = " ".join(cards)
    if any(c not in VAL for c in cards):
        print(text + ": invalid")
        continue
    total = sum(VAL[c] for c in cards)
    aces = cards.count("A")
    while total > 21 and aces > 0:
        total -= 10
        aces -= 1
    if len(cards) == 2 and total == 21:
        st = "blackjack 21"
    elif total > 21:
        st = f"bust {total}"
    elif aces > 0:
        st = f"{total} soft"
    else:
        st = f"{total} hard"
    print(f"{text}: {st}")
