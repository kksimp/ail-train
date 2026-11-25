import sys
L = [(0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6)]
def winner(b):
    for a, c, d in L:
        if b[a] != "." and b[a] == b[c] == b[d]:
            return b[a]
    return ""
def judge(line):
    b = ["."] * 9
    turn = 0
    done = False
    for tok in line.split():
        if done:
            return "invalid"
        try:
            n = int(tok)
        except ValueError:
            return "invalid"
        if n < 0 or n > 8 or b[n] != ".":
            return "invalid"
        b[n] = "X" if turn % 2 == 0 else "O"
        turn += 1
        if winner(b) != "":
            done = True
    if done:
        return winner(b) + " wins"
    if turn == 9:
        return "draw"
    return "in progress"
text = sys.stdin.read()
lines = text.split("\n")
if lines and lines[-1] == "":
    lines.pop()
for l in lines:
    print(judge(l.rstrip("\r")))
