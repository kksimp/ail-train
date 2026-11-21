party = [("Wren", "Hero", 16), ("Tobin", "Hero", 10), ("Goblin A", "Monster", 14), ("Goblin B", "Monster", 14), ("Ogre", "Monster", 8), ("Isolde", "Hero", 12)]

def modifier(dex):
    return dex // 2 - 5

seed = 1234
totals = []
for c in party:
    seed = (seed * 1103515245 + 12345) % 2147483648
    roll = (seed // 65536) % 20 + 1
    totals.append(roll + modifier(c[2]))
order = sorted(range(6), key=lambda i: (-totals[i], -party[i][2], 0 if party[i][1] == "Hero" else 1))
for place, i in enumerate(order):
    c = party[i]
    print(f"{place + 1}. {c[0]:<9} {totals[i]:>2} (dex {c[2]}, Side.{c[1]})")
heroes_first = party[order[0]][1] == "Hero"
print("the heroes act first" if heroes_first else "a monster acts first")
