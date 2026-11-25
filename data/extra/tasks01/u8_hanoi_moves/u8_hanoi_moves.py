import sys

def hanoi(n, a, b, c, out):
    if n == 0:
        return
    hanoi(n - 1, a, c, b, out)
    out.append("move %d %s %s" % (n, a, c))
    hanoi(n - 1, b, a, c, out)

for raw in sys.stdin.read().split("\n"):
    line = raw.strip()
    if line == "":
        continue
    parts = line.split(" ")
    if len(parts) == 1:
        parts += ["A", "C"]
    ok = len(parts) == 3 and parts[0].isdigit() and 1 <= int(parts[0]) <= 5 \
        and parts[1] in ("A", "B", "C") and parts[2] in ("A", "B", "C")
    if not ok:
        print("invalid: " + line)
        continue
    n, f, t = int(parts[0]), parts[1], parts[2]
    out = []
    if f != t:
        spare = [p for p in "ABC" if p != f and p != t][0]
        hanoi(n, f, spare, t, out)
    print("%d %s %s: %d moves" % (n, f, t, len(out)))
    for m in out:
        print(m)
