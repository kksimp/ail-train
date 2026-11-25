import sys


def number(s):
    if s == "" or len(s) > 6 or not all(c in "0123456789" for c in s):
        return None
    return int(s)


tables = []  # [id, seats, party]
waiting = []  # [name, size]


def seat_waiting(t):
    for i, (name, size) in enumerate(waiting):
        if size <= tables[t][1]:
            tables[t][2] = name
            print(f"{name} seated at {tables[t][0]}")
            del waiting[i]
            return


def seated_at(name):
    for i, t in enumerate(tables):
        if t[2] == name:
            return i
    return -1


def waiting_at(name):
    for i, p in enumerate(waiting):
        if p[0] == name:
            return i
    return -1


def show(items):
    return "none" if not items else ", ".join(items)


for k, line in enumerate(sys.stdin.read().splitlines(), 1):
    w = line.split()
    if not w:
        continue
    s = 0
    if len(w) == 3:
        v = number(w[2])
        s = v if v is not None else 0
    name = w[1] if len(w) >= 2 else ""
    at = seated_at(name)
    wi = waiting_at(name)
    if w[0] == "table" and len(w) == 3 and s > 0 and all(t[0] != name for t in tables):
        tables.append([name, s, ""])
        print(f"table {name} added")
        seat_waiting(len(tables) - 1)
    elif w[0] == "arrive" and len(w) == 3 and s > 0:
        biggest = max((t[1] for t in tables), default=0)
        if at >= 0 or wi >= 0:
            print(f"{name} already here")
        elif s > biggest:
            print(f"{name} too large")
        else:
            best = -1
            for i, t in enumerate(tables):
                if t[2] == "" and t[1] >= s and (best < 0 or t[1] < tables[best][1]):
                    best = i
            if best >= 0:
                tables[best][2] = name
                print(f"{name} seated at {tables[best][0]}")
            else:
                waiting.append([name, s])
                print(f"{name} waits (position {len(waiting)})")
    elif w[0] == "leave" and len(w) == 2:
        if at >= 0:
            tables[at][2] = ""
            print(f"{name} left")
            seat_waiting(at)
        elif wi >= 0:
            del waiting[wi]
            print(f"{name} removed from waitlist")
        else:
            print(f"{name} not found")
    else:
        print(f"line {k}: bad line")
print("waiting: " + show([f"{n}({sz})" for n, sz in waiting]))
print("free tables: " + show([t[0] for t in tables if t[2] == ""]))
