MILLS = [[0, 1, 2], [2, 3, 4], [4, 5, 6], [6, 7, 0], [8, 9, 10], [10, 11, 12], [12, 13, 14], [14, 15, 8], [16, 17, 18], [18, 19, 20], [20, 21, 22], [22, 23, 16], [1, 9, 17], [3, 11, 19], [5, 13, 21], [7, 15, 23]]

def in_mill(board, p):
    for m in MILLS:
        if p in m and board[m[0]] == board[p] and board[m[1]] == board[p] and board[m[2]] == board[p]:
            return True
    return False

board = ['.'] * 24
moves = [0, 8, 1, 9, 2, 10, 16, 11, 17, 12, 18, 3, 4, 19]
for i, p in enumerate(moves):
    me = 'W' if i % 2 == 0 else 'B'
    foe = 'B' if me == 'W' else 'W'
    if board[p] != '.':
        print(f"{me} cannot place on {p}")
        continue
    board[p] = me
    if in_mill(board, p):
        taken = -1
        for q in range(24):
            if taken < 0 and board[q] == foe and not in_mill(board, q):
                taken = q
        if taken >= 0:
            board[taken] = '.'
            print(f"{me} places {p}, makes a mill and removes {foe} from {taken}")
        else:
            print(f"{me} places {p}, makes a mill but every {foe} piece is protected")
whites = board.count('W')
blacks = board.count('B')
print(f"pieces left: W {whites}, B {blacks}")
print("".join(board))
