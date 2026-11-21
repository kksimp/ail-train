state = 12
def roll_die():
    global state
    state = (state * 1103515245 + 12345) % 2147483648
    return 1 + (state // 65536) % 4
starts = [0, 8]; names = ["Red", "Blue"]
tokens = [[0, 0, 0], [0, 0, 0], [1, 8, 0], [1, 8, 0]]
laps = [0, 0]; turn = 0
while laps[0] < 3 and laps[1] < 3:
    p = turn % 2
    roll = roll_die()
    mine = [i for i in range(4) if tokens[i][0] == p]
    pick = mine[0]
    if tokens[mine[1]][2] < tokens[pick][2]: pick = mine[1]
    for i in mine:
        land = (tokens[i][1] + roll) % 16
        if any(t[0] != p and t[1] == land for t in tokens): pick = i
    tokens[pick][1] = (tokens[pick][1] + roll) % 16
    tokens[pick][2] += roll
    for t in tokens:
        if t[0] != p and t[1] == tokens[pick][1]:
            t[1] = starts[t[0]]; t[2] = 0
            print(f"turn {turn + 1:>2}: {names[p]} rolls {roll} and sends a {names[1 - p]} token home from {tokens[pick][1]}")
    if tokens[pick][2] >= 16:
        laps[p] += 1
        tokens[pick][1] = starts[p]; tokens[pick][2] = 0
        print(f"turn {turn + 1:>2}: {names[p]} completes lap {laps[p]}")
    turn += 1
winner = names[0] if laps[0] == 3 else names[1]
print(f"{winner} wins after {turn} turns, laps {laps}")
