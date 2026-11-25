import sys

def place(cols, r, n):
    if r == n:
        return 1
    total = 0
    for c in range(n):
        ok = True
        for i in range(r):
            d = cols[i] - c
            if d == 0 or abs(d) == r - i:
                ok = False
                break
        if ok:
            cols.append(c)
            total += place(cols, r + 1, n)
            cols.pop()
    return total

for raw in sys.stdin.read().split("\n"):
    line = raw.strip()
    if line == "":
        continue
    try:
        n = int(line)
    except ValueError:
        print("invalid: " + line)
        continue
    if n < 1 or n > 9:
        print("invalid: " + line)
        continue
    print("%d: %d" % (n, place([], 0, n)))
