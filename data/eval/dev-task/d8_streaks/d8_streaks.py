import sys

lines = sys.stdin.read().splitlines()
s = lines[0].strip(" ") if lines else ""
if s == "":
    print("no games")
    sys.exit(0)
for c in s:
    if c not in "WL":
        print("bad result: " + c)
        sys.exit(0)
best = {"W": 0, "L": 0}
run = 0
prev = ""
for c in s:
    run = run + 1 if c == prev else 1
    prev = c
    best[c] = max(best[c], run)
print("games: %d" % len(s))
print("longest W: %d" % best["W"])
print("longest L: %d" % best["L"])
print("current: %s %d" % (prev, run))
