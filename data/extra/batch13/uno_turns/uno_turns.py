names = ["Ann", "Bob", "Cy", "Dot"]
plays = [("num", 5), ("skip",), ("num", 3), ("rev",), ("num", 7), ("draw",), ("num", 2), ("rev",), ("skip",), ("num", 9)]
cards = [7, 7, 7, 7]
p = 0
d = 1
for play in plays:
    cards[p] -= 1
    step = 1
    text = {"num": f"plays {play[-1]}", "skip": "plays skip", "rev": "plays reverse", "draw": "plays draw two"}[play[0]]
    note = ""
    if play[0] == "skip":
        step = 2
    elif play[0] == "rev":
        d = -d
    elif play[0] == "draw":
        victim = (p + d + 4) % 4
        cards[victim] += 2
        note = f", {names[victim]} draws 2"
        step = 2
    print(f"{names[p]} {text}{note}")
    p = ((p + d * step) % 4 + 4) % 4
for i in range(4):
    print(f"{names[i]} holds {cards[i]}")
