import sys
from collections import deque

def to_int(s):
    t = s[1:] if s.startswith("-") else s
    if t.isascii() and t.isdigit():
        return int(s)
    return None

d = deque()
for line in sys.stdin.read().splitlines():
    w = line.split()
    if not w:
        continue
    c = w[0]
    if c in ("push_front", "push_back", "rotate") and len(w) == 2 and to_int(w[1]) is not None:
        x = to_int(w[1])
        if c == "push_front":
            d.appendleft(x)
        elif c == "push_back":
            d.append(x)
        elif d:
            d.rotate(-(x % len(d)))
        print("ok")
    elif c in ("pop_front", "pop_back", "front", "back", "reverse", "show") and len(w) == 1:
        if c == "reverse":
            d.reverse()
            print("ok")
        elif c == "show":
            print(" ".join(map(str, d)) if d else "empty")
        elif not d:
            print("empty")
        elif c == "pop_front":
            print(d.popleft())
        elif c == "pop_back":
            print(d.pop())
        elif c == "front":
            print(d[0])
        else:
            print(d[-1])
    else:
        print("error")
