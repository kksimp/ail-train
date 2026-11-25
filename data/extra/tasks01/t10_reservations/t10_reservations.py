import sys

lines = sys.stdin.read().splitlines()
head = (lines[0] if lines else "").split(" ")
size = None
if len(head) == 2 and head[0] == "seats":
    t = head[1][1:] if head[1].startswith("-") else head[1]
    if t.isascii() and t.isdigit():
        size = int(head[1])
if size is None or size < 1 or size > 50:
    print("bad header")
    sys.exit(0)
holder = {}
waits = {}


def known(name):
    return name in holder.values() or any(name in q for q in waits.values())


def toint(s):
    t = s[1:] if s.startswith("-") else s
    return int(s) if t.isascii() and t.isdigit() else 0


for i in range(1, len(lines)):
    line = lines[i]
    if line.strip() == "":
        continue
    f = line.split(" ")
    if len(f) == 3 and f[0] == "book":
        name, seat = f[1], toint(f[2])
        if seat < 1 or seat > size:
            print(f"{name}: invalid seat")
        elif known(name):
            print(f"{name}: already booked")
        elif seat in holder:
            waits.setdefault(seat, []).append(name)
            print(f"{name}: waitlisted for {seat}")
        else:
            holder[seat] = name
            print(f"{name}: booked {seat}")
    elif len(f) == 2 and f[0] == "cancel":
        name = f[1]
        for seat in range(1, size + 1):
            if holder.get(seat) == name:
                print(f"{name}: cancelled {seat}")
                q = waits.get(seat, [])
                if not q:
                    del holder[seat]
                else:
                    holder[seat] = q[0]
                    waits[seat] = q[1:]
                    print(f"{q[0]}: promoted to {seat}")
                break
            q = waits.get(seat, [])
            if name in q:
                waits[seat] = [w for w in q if w != name]
                print(f"{name}: left waitlist")
                break
        else:
            print(f"{name}: no reservation")
    elif len(f) == 1 and f[0] == "show":
        print("seats: " + " ".join(f"{s}={holder.get(s, '-')}" for s in range(1, size + 1)))
    else:
        print(f"bad line {i + 1}")
