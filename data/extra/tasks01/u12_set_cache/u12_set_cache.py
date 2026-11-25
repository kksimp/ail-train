import sys

lines = [l for l in sys.stdin.read().splitlines() if l.strip()]
sets = ways = blk = -1
pol = ""
if lines:
    f = lines[0].split()
    if len(f) == 6 and f[0] == "cache" and f[4] == "policy" and f[5] in ("lru", "fifo"):
        try:
            sets, ways, blk, pol = int(f[1]), int(f[2]), int(f[3]), f[5]
        except ValueError:
            sets = -1
if sets < 1 or ways < 1 or blk < 1:
    print("bad header")
    sys.exit(0)
cache = [[] for _ in range(sets)]
hits = misses = skipped = 0
out = []
for l in lines[1:]:
    for tok in l.split():
        if not tok.isdigit() or not tok.isascii():
            skipped += 1
            continue
        a = int(tok)
        b = a // blk
        s = b % sets
        tag = b // sets
        c = cache[s]
        if tag in c:
            hits += 1
            if pol == "lru":
                c.remove(tag)
                c.append(tag)
            out.append(f"{a} set={s} hit")
        else:
            misses += 1
            if len(c) == ways:
                c.pop(0)
            c.append(tag)
            out.append(f"{a} set={s} miss")
total = hits + misses
v = hits * 10000 // total if total else 0
out.append(f"hits={hits} misses={misses} ratio={v // 100}.{v % 100:02d} skipped={skipped}")
print("\n".join(out))
