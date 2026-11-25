import re
import sys

projects = []  # [name, budget, spent]
months = 0


def amount(s):
    if not re.fullmatch(r"[0-9]+", s) or int(s) < 1:
        return None
    return int(s)


def find(name):
    for i, p in enumerate(projects):
        if p[0] == name:
            return i
    return -1


def run(line):
    global months
    w = line.split(" ")
    cmd = w[0]
    need = {"MONTH": 1, "BUDGET": 3, "SPEND": 3, "REFUND": 3, "REALLOC": 4}
    if cmd not in need:
        return "unknown command"
    if len(w) != need[cmd]:
        return "bad arguments"
    if cmd == "MONTH":
        months += 1
        return None
    cents = amount(w[-1])
    if cents is None:
        return "bad amount"
    if cmd == "BUDGET":
        if find(w[1]) >= 0:
            return "duplicate project " + w[1]
        projects.append([w[1], cents, 0])
    elif cmd == "SPEND":
        i = find(w[1])
        if i < 0:
            return "unknown project " + w[1]
        projects[i][2] += cents
    elif cmd == "REFUND":
        i = find(w[1])
        if i < 0:
            return "unknown project " + w[1]
        if cents > projects[i][2]:
            return "refund exceeds spend"
        projects[i][2] -= cents
    else:
        a = find(w[1])
        if a < 0:
            return "unknown project " + w[1]
        b = find(w[2])
        if b < 0:
            return "unknown project " + w[2]
        if a == b:
            return "same project"
        if projects[a][1] - cents < max(projects[a][2], 1):
            return "insufficient budget"
        projects[a][1] -= cents
        projects[b][1] += cents
    return None


for k, line in enumerate(sys.stdin.read().splitlines(), 1):
    if line == "":
        continue
    err = run(line)
    if err:
        print("line %d: %s" % (k, err))
print("months: %d" % months)
tb = ts = 0
for name, budget, spent in projects:
    pct = spent * 100 // budget
    status = "OVER" if spent > budget else ("WARN" if pct >= 80 else "OK")
    left = budget - spent
    avg = spent // max(months, 1)
    if avg == 0:
        rw = "inf"
    elif left <= 0:
        rw = "0"
    else:
        rw = str(left // avg)
    print("%s budget=%d spent=%d left=%d used=%d%% %s runway=%s" % (name, budget, spent, left, pct, status, rw))
    tb += budget
    ts += spent
print("projects: %d budget=%d spent=%d" % (len(projects), tb, ts))
