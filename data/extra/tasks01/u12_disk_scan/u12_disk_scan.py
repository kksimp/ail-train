import sys

lines = [l for l in sys.stdin.read().splitlines() if l.strip()]
c = h = -1
d = ""
if lines:
    f = lines[0].split()
    if len(f) == 6 and f[0] == "disk" and f[2] == "head" and f[4] == "dir" and f[5] in ("up", "down"):
        try:
            c, h, d = int(f[1]), int(f[3]), f[5]
        except ValueError:
            c = -1
if c < 1 or h < 0 or h >= c:
    print("bad header")
    sys.exit(0)
reqs = []
skipped = 0
for l in lines[1:]:
    for t in l.split():
        try:
            v = int(t)
        except ValueError:
            skipped += 1
            continue
        if 0 <= v < c:
            reqs.append(v)
        else:
            skipped += 1
if d == "up":
    first = sorted(r for r in reqs if r >= h)
    second = sorted((r for r in reqs if r < h), reverse=True)
    end = c - 1
else:
    first = sorted((r for r in reqs if r <= h), reverse=True)
    second = sorted(r for r in reqs if r > h)
    end = 0
order = first + second
path = [h] + first
if second:
    path.append(end)
    path += second
move = sum(abs(path[i + 1] - path[i]) for i in range(len(path) - 1))
print("order=" + " ".join(map(str, order)))
print("path=" + " ".join(map(str, path)))
print(f"movement={move} skipped={skipped}")
