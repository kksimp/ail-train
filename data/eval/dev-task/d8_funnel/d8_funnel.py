import sys

LOW = "abcdefghijklmnopqrstuvwxyz"
DIG = "0123456789"


def ok(s, alphabet, lo, hi):
    return lo <= len(s) <= hi and all(c in alphabet for c in s)


def pct(a, b):
    return 0 if b == 0 else (a * 200 + b) // (2 * b)


lines = sys.stdin.read().split("\n")
if lines and lines[-1] == "":
    lines.pop()
steps = None
if lines and lines[0].startswith("funnel: "):
    cand = lines[0][len("funnel: "):].split(",")
    if 2 <= len(cand) <= 5 and all(ok(s, LOW, 1, 10) for s in cand) and len(set(cand)) == len(cand):
        steps = cand
if steps is None:
    print("bad funnel")
    sys.exit(0)
events = []
for i, line in enumerate(lines[1:], 2):
    if line == "":
        continue
    f = line.split(" ")
    if len(f) != 3:
        print("line %d: bad format" % i)
    elif not ok(f[0], DIG, 1, 6):
        print("line %d: bad time" % i)
    elif not ok(f[1], LOW + DIG, 1, 8):
        print("line %d: bad user" % i)
    elif not ok(f[2], LOW, 1, 10):
        print("line %d: bad step" % i)
    else:
        events.append((int(f[0]), f[1], f[2]))
events.sort(key=lambda e: e[0])
prog = {}
for ts, u, st in events:
    p = prog.get(u, 0)
    if p < len(steps) and st == steps[p]:
        p += 1
    prog[u] = p
counts = [sum(1 for p in prog.values() if p > k) for k in range(len(steps))]
print("step\tusers\tof_first\tof_prev")
for k, name in enumerate(steps):
    prev = "-" if k == 0 else "%d%%" % pct(counts[k], counts[k - 1])
    print("%s\t%d\t%d%%\t%s" % (name, counts[k], pct(counts[k], counts[0]), prev))
print("users: %d" % len(prog))
print("completed: %d" % counts[-1])
