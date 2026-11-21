state = 66
def die():
    global state
    state = (state * 1103515245 + 12345) % 2147483648
    return 1 + (state // 65536) % 6
def tallest_rival(towers, me):
    best = -1
    for i in range(len(towers)):
        if i != me and (best < 0 or towers[i] > towers[best]): best = i
    return best
names = ["Iris", "Joss", "Kemi"]
towers = [0, 0, 0]
turn = 0; steals = 0
while max(towers) < 15:
    me = turn % 3
    roll = die()
    if roll <= 4: towers[me] += roll
    elif roll == 5:
        victim = tallest_rival(towers, me)
        taken = min(towers[victim], 2)
        towers[victim] -= taken; towers[me] += taken
        steals += 1
    else:
        towers[me] = max(towers[me] - 1, 0)
    if turn % 3 == 2:
        print(f"round {turn // 3 + 1:>2}: {towers}")
    turn += 1
winner = towers.index(max(towers))
print(f"{names[winner]} wins after {turn} turns with towers {towers}, {steals} steals")
