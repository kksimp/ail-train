import sys
from bisect import bisect_left, bisect_right

def to_int(s):
    t = s[1:] if s.startswith("-") else s
    if t.isascii() and t.isdigit():
        return int(s)
    return None

xs = []
for line in sys.stdin.read().splitlines():
    w = line.split()
    if not w:
        continue
    c = w[0]
    if c in ("add", "remove", "count", "rank", "kth", "floor", "ceil") and len(w) == 2 and to_int(w[1]) is not None:
        x = to_int(w[1])
        if c == "add":
            xs.insert(bisect_left(xs, x), x)
            print("ok")
        elif c == "remove":
            i = bisect_left(xs, x)
            if i < len(xs) and xs[i] == x:
                xs.pop(i)
                print("ok")
            else:
                print("missing")
        elif c == "count":
            print(bisect_right(xs, x) - bisect_left(xs, x))
        elif c == "rank":
            print(bisect_left(xs, x))
        elif c == "kth":
            print(xs[x - 1] if 1 <= x <= len(xs) else "none")
        elif c == "floor":
            i = bisect_right(xs, x)
            print(xs[i - 1] if i > 0 else "none")
        else:
            i = bisect_left(xs, x)
            print(xs[i] if i < len(xs) else "none")
    elif c == "size" and len(w) == 1:
        print(len(xs))
    else:
        print("error")
