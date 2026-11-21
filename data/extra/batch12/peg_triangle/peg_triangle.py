def hole(r, c):
    return r * (r + 1) // 2 + c

def jumps():
    dirs = [[0, 1], [1, 0], [1, 1], [0, -1], [-1, 0], [-1, -1]]
    out = []
    for r in range(5):
        for c in range(r + 1):
            for d in dirs:
                r2 = r + 2 * d[0]
                c2 = c + 2 * d[1]
                if r2 >= 0 and r2 < 5 and c2 >= 0 and c2 <= r2:
                    out.append([hole(r, c), hole(r + d[0], c + d[1]), hole(r2, c2)])
    return out

def search(board, moves, dead, path):
    pegs = len([i for i in range(15) if ((board >> i) & 1) == 1])
    if pegs == 1:
        return True
    if board in dead:
        return False
    for m in moves:
        if ((board >> m[0]) & 1) == 1 and ((board >> m[1]) & 1) == 1 and ((board >> m[2]) & 1) == 0:
            after = (board ^ (1 << m[0])) ^ ((1 << m[1]) | (1 << m[2]))
            path.append(m)
            if search(after, moves, dead, path):
                return True
            path.pop()
    dead.add(board)
    return False

moves = jumps()
start = 32767 - 1
dead = set()
path = []
print(f"{len(moves)} possible jumps on the board")
if search(start, moves, dead, path):
    for i, m in enumerate(path):
        print(f"{i + 1:>2}: peg {m[0]} jumps {m[1]} into {m[2]}")
    print(f"one peg left after {len(path)} jumps")
else:
    print("no solution")
