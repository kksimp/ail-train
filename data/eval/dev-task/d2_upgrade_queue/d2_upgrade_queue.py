import sys

STATUS = {"PLAT": 0, "GOLD": 1, "SILVER": 2, "BASIC": 3}
FARE = {"Y": 0, "B": 1, "M": 2, "K": 3}


def num(s):
    if not s or len(s) > 7 or any(c not in "0123456789" for c in s):
        return -1
    return int(s)


class Err(Exception):
    pass


seats = runs = reqs = 0
pax = {}  # insertion ordered


def run():
    global seats, runs
    runs += 1
    queue = [p for p in pax.values() if p["seq"] > 0 and not p["up"]]
    queue.sort(key=lambda p: (p["st"], p["fr"], -p["miles"], p["seq"]))
    print("run %d: seats %d waiting %d" % (runs, seats, len(queue)))
    used = 0
    for i, p in enumerate(queue):
        if i < seats:
            print("U " + p["name"])
            p["up"] = True
            used += 1
        else:
            print("W %d %s" % (i - seats + 1, p["name"]))
    seats -= used


def apply(w):
    global seats, reqs
    cmd = w[0]
    if cmd == "SEATS":
        if len(w) != 2:
            raise Err("wrong number of arguments")
        n = num(w[1])
        if n < 0:
            raise Err("bad number")
        seats = n
    elif cmd == "PAX":
        if len(w) != 5:
            raise Err("wrong number of arguments")
        if w[2] not in STATUS:
            raise Err("bad status")
        if w[3] not in FARE:
            raise Err("bad fare")
        miles = num(w[4])
        if miles < 0:
            raise Err("bad number")
        if w[1] in pax:
            raise Err("duplicate passenger " + w[1])
        pax[w[1]] = {"name": w[1], "st": STATUS[w[2]], "fr": FARE[w[3]], "miles": miles, "seq": 0, "up": False}
    elif cmd == "REQ":
        if len(w) != 2:
            raise Err("wrong number of arguments")
        if w[1] not in pax:
            raise Err("unknown passenger " + w[1])
        if pax[w[1]]["seq"] > 0:
            raise Err("already requested " + w[1])
        reqs += 1
        pax[w[1]]["seq"] = reqs
    elif cmd == "RUN":
        if len(w) != 1:
            raise Err("wrong number of arguments")
        run()
    else:
        raise Err("unknown command")


for k, line in enumerate(sys.stdin.read().split("\n"), 1):
    w = line.split()
    if not w:
        continue
    try:
        apply(w)
    except Err as e:
        print("line %d: %s" % (k, e))

up = sum(1 for p in pax.values() if p["up"])
wait = sum(1 for p in pax.values() if not p["up"] and p["seq"] > 0)
print("summary: %d upgraded, %d waiting" % (up, wait))
