def pips(board, white):
    total = 0
    for point, n in board.items():
        if white and n > 0:
            total += point * n
        if not white and n < 0:
            total += (25 - point) * -n
    return total

board = {24: -2, 13: 5, 8: 3, 6: 5, 1: 2, 12: -5, 17: -3, 19: -5}
board[1] = 0
board[19] = -3
board[20] = -2
board[6] = 7
print(f"start: White {pips(board, True)}, Black {pips(board, False)}")
moves = [[13, 5], [13, 3], [8, 6], [6, 4], [24, 6], [6, 6]]
for m in moves:
    frm = m[0]
    to = frm - m[1]
    if board.get(frm, 0) <= 0:
        print(f"no white checker on {frm}")
        continue
    board[frm] -= 1
    board[to] = board.get(to, 0) + 1
    w = pips(board, True)
    b = pips(board, False)
    leader = "White" if w < b else "Black"
    print(f"{frm}/{to}: White {w}, Black {b}, {leader} leads by {abs(b - w)}")
