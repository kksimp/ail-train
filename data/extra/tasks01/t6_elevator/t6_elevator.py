import sys
def main():
    lines = sys.stdin.read().split("\n")
    if lines and lines[-1] == "":
        lines.pop()
    lines = [l.rstrip("\r") for l in lines]
    def ints2(l):
        p = l.split()
        if len(p) != 2:
            return None
        try:
            return int(p[0]), int(p[1])
        except ValueError:
            return None
    h = ints2(lines[0]) if lines else None
    if h is None or not (1 <= h[1] <= h[0]):
        print("bad header")
        return
    F, pos = h
    reqs = []
    for l in lines[1:]:
        q = ints2(l)
        if q is None or q[0] < 0 or q[1] < 1 or q[1] > F:
            continue
        reqs.append(q)
    last = max([t for t, _ in reqs], default=0)
    pending = []
    d = 1
    t = 0
    moves = 0
    while True:
        for rt, rf in reqs:
            if rt == t and rf not in pending:
                pending.append(rf)
        if pos in pending:
            pending.remove(pos)
            print("t=%d floor=%d" % (t, pos))
        if not pending and t >= last:
            break
        if pending:
            if d == 1 and not any(p > pos for p in pending):
                d = -1
            elif d == -1 and not any(p < pos for p in pending):
                d = 1
            pos += d
            moves += 1
        t += 1
    print("moves=%d" % moves)
main()
