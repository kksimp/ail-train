import sys
def ints(s, n):
    p = s.split()
    if len(p) != n:
        return None
    try:
        return [int(x) for x in p]
    except ValueError:
        return None
def main():
    lines = sys.stdin.read().split("\n")
    if lines and lines[-1] == "":
        lines.pop()
    lines = [l.rstrip("\r") for l in lines]
    def bad():
        print("bad input")
    if len(lines) < 3:
        return bad()
    wh = ints(lines[0], 2)
    st = lines[1].split()
    if wh is None or wh[0] < 1 or wh[1] < 1 or len(st) != 3 or st[2] not in "NESW" or len(st[2]) != 1:
        return bad()
    try:
        x, y = int(st[0]), int(st[1])
        k = int(lines[2].strip())
    except ValueError:
        return bad()
    W, H = wh
    if k < 0 or len(lines) < 3 + k:
        return bad()
    obs = set()
    for i in range(k):
        o = ints(lines[3 + i], 2)
        if o is None:
            return bad()
        obs.add((o[0], o[1]))
    if not (0 <= x < W and 0 <= y < H) or (x, y) in obs:
        return bad()
    d = "NESW".index(st[2])
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    for cmd in lines[3 + k:]:
        if any(c not in "FBLR" for c in cmd):
            print("bad command")
            continue
        bumps = 0
        for c in cmd:
            if c == "L":
                d = (d + 3) % 4
            elif c == "R":
                d = (d + 1) % 4
            else:
                s = 1 if c == "F" else -1
                nx, ny = x + s * dx[d], y + s * dy[d]
                if 0 <= nx < W and 0 <= ny < H and (nx, ny) not in obs:
                    x, y = nx, ny
                else:
                    bumps += 1
        print("%d %d %s bumps=%d" % (x, y, "NESW"[d], bumps))
    print("final %d %d %s" % (x, y, "NESW"[d]))
main()
