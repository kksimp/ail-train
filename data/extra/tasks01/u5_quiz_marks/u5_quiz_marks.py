import sys
lines = sys.stdin.read().split("\n")
key = lines[0].strip()
if not (1 <= len(key) <= 30) or any(c not in "ABCD" for c in key) or len(lines[0].split()) != 1:
    print("error: bad key"); sys.exit(0)
rows = []
seen = set()
bad = 0
for line in lines[1:]:
    f = line.split()
    if not f: continue
    if len(f) != 2 or len(f[1]) != len(key) or any(c not in "ABCD-" for c in f[1]) or f[0] in seen:
        bad += 1; continue
    seen.add(f[0])
    c = sum(1 for a, k in zip(f[1], key) if a == k)
    s = sum(1 for a in f[1] if a == "-")
    w = len(key) - c - s
    rows.append((-(4 * c - w), f[0], c, w, s, f[1]))
rows.sort()
if not rows:
    print("no submissions")
else:
    i = 0
    while i < len(rows):
        j = i
        while j < len(rows) and rows[j][0] == rows[i][0]: j += 1
        for k in range(i, j):
            r = rows[k]
            print("%d %s %d %d/%d/%d" % (i + 1, r[1], -r[0], r[2], r[3], r[4]))
        i = j
    cnt = [sum(1 for r in rows if r[5][q] == key[q]) for q in range(len(key))]
    print("correct per question: " + " ".join(str(x) for x in cnt))
    tot = -sum(r[0] for r in rows)
    n = len(rows)
    num = tot * 10
    v = (2 * abs(num) + n) // (2 * n)
    sign = "-" if num < 0 and v != 0 else ""
    print("mean: %s%d.%d" % (sign, v // 10, v % 10))
if bad:
    print("invalid: %d" % bad)
