import sys

lines = sys.stdin.read().splitlines()

def to_int(s):
    t = s[1:] if s.startswith("-") else s
    if t.isascii() and t.isdigit():
        return int(s)
    return None

q = to_int(lines[0].strip()) if lines else None
if q is None or q < 1 or q > 100:
    print("bad quantum")
    sys.exit(0)

from collections import deque
queue = deque()  # [name, remaining]
clock = 0
for line in lines[1:]:
    w = line.split()
    if not w:
        continue
    c = w[0]
    if c == "add" and len(w) == 3 and to_int(w[2]) is not None and 1 <= to_int(w[2]) <= 1000:
        if any(p[0] == w[1] for p in queue):
            print("dup")
        else:
            queue.append([w[1], to_int(w[2])])
            print("ok")
    elif c == "run" and len(w) == 2 and to_int(w[1]) is not None and to_int(w[1]) >= 0:
        for _ in range(to_int(w[1])):
            if not queue:
                print("idle")
                break
            p = queue.popleft()
            t = min(q, p[1])
            p[1] -= t
            clock += t
            print(f"{p[0]} ran {t}")
            if p[1] == 0:
                print(f"{p[0]} done")
            else:
                queue.append(p)
    elif c == "status" and len(w) == 1:
        print(" ".join(f"{p[0]}:{p[1]}" for p in queue) if queue else "empty")
    elif c == "clock" and len(w) == 1:
        print(clock)
    else:
        print("error")
