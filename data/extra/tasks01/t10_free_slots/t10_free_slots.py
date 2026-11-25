import sys


def ints(line):
    out = []
    for w in line.split(" "):
        t = w[1:] if w.startswith("-") else w
        if not t.isdigit() or not t.isascii():
            return None
        out.append(int(w))
    return out


lines = sys.stdin.read().splitlines()
hdr = ints(lines[0]) if lines else None
if hdr is None or len(hdr) != 3 or hdr[0] >= hdr[1] or hdr[2] < 1:
    print("bad header")
    sys.exit(0)
op, cl, minlen = hdr
busy = []
skipped = 0
for line in lines[1:]:
    if line.strip() == "":
        continue
    v = ints(line)
    if v is None or len(v) != 2 or v[0] >= v[1]:
        skipped += 1
        continue
    busy.append((v[0], v[1]))
busy.sort()
cursor = op
total = 0
for a, e in busy:
    if a > cursor:
        hi = min(a, cl)
        if hi - cursor >= minlen:
            print(f"{cursor}-{hi}")
            total += hi - cursor
    if e > cursor:
        cursor = e
if cl - cursor >= minlen:
    print(f"{cursor}-{cl}")
    total += cl - cursor
print(f"free total {total}")
print(f"skipped {skipped}")
