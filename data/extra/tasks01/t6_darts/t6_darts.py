import sys
def value(t):
    if t == "B":
        return 50, True
    if t == "M":
        return 0, False
    if t == "25":
        return 25, False
    if len(t) >= 2 and t[0] in "SDT" and t[1:].isdigit() and t[1:].isascii():
        n = int(t[1:])
        if 1 <= n <= 20 and t[1] != "0" or False:
            return n * {"S": 1, "D": 2, "T": 3}[t[0]], t[0] == "D"
    return None
def game(line):
    toks = line.split()
    rem = 301
    start = 301
    inturn = 0
    bust = False
    finished_at = 0
    for i, t in enumerate(toks, 1):
        if finished_at:
            return "invalid"
        v = value(t)
        if v is None:
            return "invalid"
        pts, dbl = v
        if not bust:
            left = rem - pts
            if left < 0 or left == 1 or (left == 0 and not dbl):
                bust = True
                rem = start
            elif left == 0:
                rem = 0
                finished_at = i
            else:
                rem = left
        inturn += 1
        if inturn == 3:
            inturn = 0
            bust = False
            start = rem
    if finished_at:
        return "finished in %d darts" % finished_at
    return "remaining %d after %d darts" % (rem, len(toks))
lines = sys.stdin.read().split("\n")
if lines and lines[-1] == "":
    lines.pop()
for l in lines:
    print(game(l.rstrip("\r")))
