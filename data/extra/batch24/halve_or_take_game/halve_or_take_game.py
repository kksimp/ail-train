def table(limit):
    win = [False]
    for n in range(1, limit + 1):
        w = not win[n - 1]
        if n >= 4 and not win[n - 4]: w = True
        if n % 2 == 0 and not win[n // 2]: w = True
        win.append(w)
    return win
def best_move(win, n):
    if not win[n - 1]: return n - 1
    if n >= 4 and not win[n - 4]: return n - 4
    if n % 2 == 0 and not win[n // 2]: return n // 2
    return n - 1
win = table(40)
lost = [n for n in range(41) if not win[n]]
print(f"losing piles for the player to move: {lost}")
for start in [22, 26]:
    pile = start; moves = [pile]
    while pile > 0:
        pile = best_move(win, pile); moves.append(pile)
    first = "first" if len(moves) % 2 == 0 else "second"
    print(f"from {start}: {' > '.join(map(str, moves))}, the {first} player wins")
