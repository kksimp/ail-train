import sys

lines = sys.stdin.read().split("\n")
board = []
ok = len(lines) >= 4
if ok:
    for l in lines[:4]:
        parts = l.strip().split(" ")
        if len(parts) != 4 or not all(p.isdigit() for p in parts):
            ok = False
            break
        board.extend(int(p) for p in parts)
if not ok or sorted(board) != list(range(16)):
    print("invalid board")
    sys.exit(0)
moves = lines[4].strip() if len(lines) > 4 else ""
pos = board.index(0)
DELTA = {"U": (-1, 0), "D": (1, 0), "L": (0, -1), "R": (0, 1)}
for k, ch in enumerate(moves, 1):
    if ch not in DELTA:
        print("bad move %d" % k)
        sys.exit(0)
    r, c = divmod(pos, 4)
    nr, nc = r + DELTA[ch][0], c + DELTA[ch][1]
    if not (0 <= nr < 4 and 0 <= nc < 4):
        print("illegal move %d" % k)
        sys.exit(0)
    np_ = nr * 4 + nc
    board[pos], board[np_] = board[np_], board[pos]
    pos = np_
for r in range(4):
    print(" ".join(str(x) for x in board[r * 4:r * 4 + 4]))
print("solved" if board == list(range(1, 16)) + [0] else "unsolved")
