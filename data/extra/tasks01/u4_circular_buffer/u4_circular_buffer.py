import sys

lines = sys.stdin.read().splitlines()

def to_int(s):
    t = s[1:] if s.startswith("-") else s
    if t.isascii() and t.isdigit():
        return int(s)
    return None

cap = to_int(lines[0].strip()) if lines else None
if cap is None or cap < 1 or cap > 100:
    print("bad capacity")
    sys.exit(0)

buf = [0] * cap
head = 0
count = 0

for line in lines[1:]:
    w = line.split()
    if not w:
        continue
    c = w[0]
    if c == "push" and len(w) == 2 and to_int(w[1]) is not None:
        x = to_int(w[1])
        if count == cap:
            old = buf[head]
            buf[head] = x
            head = (head + 1) % cap
            print("overwrote", old)
        else:
            buf[(head + count) % cap] = x
            count += 1
            print("ok")
    elif c == "pop" and len(w) == 1:
        if count == 0:
            print("empty")
        else:
            print(buf[head])
            head = (head + 1) % cap
            count -= 1
    elif c == "peek" and len(w) == 1:
        print(buf[head] if count else "empty")
    elif c == "dump" and len(w) == 1:
        if count == 0:
            print("empty")
        else:
            print(" ".join(str(buf[(head + i) % cap]) for i in range(count)))
    elif c == "size" and len(w) == 1:
        print(count)
    elif c == "sum" and len(w) == 1:
        print(sum(buf[(head + i) % cap] for i in range(count)))
    else:
        print("error")
