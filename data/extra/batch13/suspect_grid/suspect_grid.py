def remaining(cards, crossed):
    return ", ".join(c for c in cards if c not in crossed)

suspects = ["Plum", "Scarlet", "Mustard", "Green", "Peacock"]
weapons = ["rope", "knife", "pipe", "candlestick"]
rooms = ["hall", "library", "kitchen", "study"]
mine = ["Green", "pipe", "hall"]
crossed = set(mine)
events = [("Plum knife library", "knife"), ("Scarlet rope study", "Scarlet"), ("Mustard rope kitchen", "kitchen"), ("Peacock candlestick study", "study"), ("Plum rope library", "")]
solution = []
for suggestion, shown in events:
    if shown == "":
        for c in suggestion.split(" "):
            if c not in mine and c not in solution:
                solution.append(c)
        print(f"{suggestion}: nobody can answer")
    else:
        crossed.add(shown)
        print(f"{suggestion}: shown {shown}")
for c in solution:
    for other in [suspects, weapons, rooms]:
        if c in other:
            for x in other:
                if x != c:
                    crossed.add(x)
print(f"suspects left: {remaining(suspects, crossed)}")
print(f"weapons left: {remaining(weapons, crossed)}")
print(f"rooms left: {remaining(rooms, crossed)}")
