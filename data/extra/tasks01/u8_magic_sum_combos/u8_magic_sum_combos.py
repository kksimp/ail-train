import sys

def gen(k, n, start, cur, out):
    if k == 0:
        if n == 0:
            out.append(list(cur))
        return
    for d in range(start, 10):
        if d > n:
            break
        cur.append(d)
        gen(k - 1, n - d, d + 1, cur, out)
        cur.pop()

for raw in sys.stdin.read().split("\n"):
    line = raw.strip()
    if line == "":
        continue
    parts = line.split(" ")
    if len(parts) != 2 or not all(p.isdigit() and p.isascii() for p in parts):
        print("invalid: " + line)
        continue
    k, n = int(parts[0]), int(parts[1])
    out = []
    gen(k, n, 1, [], out)
    print("%d %d: %d" % (k, n, len(out)))
    for s in out:
        print(" ".join(str(x) for x in s))
