def points(taken):
    p = 0
    for card in taken.split(" "):
        if card == "QS":
            p += 13
        elif card.endswith("H"):
            p += 1
    return p

names = ["Ana", "Ben", "Cal", "Dee"]
rounds = [["2H 5H QS", "KH AH 9H", "", "3H 4H 6H 7H 8H TH JH QH"], ["", "2H 3H 4H 5H 6H 7H 8H 9H TH JH QH KH AH QS", "", ""], ["4H 9H", "", "QS AH KH", "2H 3H 5H 6H 7H 8H TH JH QH"], ["", "QS 2H", "3H 4H 5H 6H", "7H 8H 9H TH JH QH KH AH"]]
totals = [0, 0, 0, 0]
for ri, hand in enumerate(rounds):
    got = [points(t) for t in hand]
    moon = -1
    for i in range(4):
        if got[i] == 26:
            moon = i
    if moon >= 0:
        for i in range(4):
            got[i] = 0 if i == moon else 26
        print(f"round {ri + 1}: {names[moon]} shoots the moon")
    for i in range(4):
        totals[i] += got[i]
    shown = "".join(f"{g:>3}" for g in got)
    print(f"round {ri + 1} points:{shown}")
best = 0
for i in range(4):
    print(f"{names[i]:<4} {totals[i]:>3}")
    if totals[i] < totals[best]:
        best = i
print(f"winner: {names[best]}")
