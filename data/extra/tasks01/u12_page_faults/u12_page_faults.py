import sys

lines = [l for l in sys.stdin.read().splitlines() if l.strip()]
n = 0
if lines:
    f = lines[0].split()
    if len(f) == 2 and f[0] == "frames":
        try:
            n = int(f[1])
        except ValueError:
            n = 0
if n < 1:
    print("bad frames")
    sys.exit(0)
refs = []
skipped = 0
for l in lines[1:]:
    for tok in l.split():
        try:
            refs.append(int(tok))
        except ValueError:
            skipped += 1


def sim(lru):
    mem = []
    trace = []
    faults = 0
    for r in refs:
        if r in mem:
            trace.append("H")
            if lru:
                mem.remove(r)
                mem.append(r)
        else:
            trace.append("F")
            faults += 1
            if len(mem) == n:
                mem.pop(0)
            mem.append(r)
    return faults, "".join(trace), mem


for name, lru in (("FIFO", False), ("LRU", True)):
    faults, trace, mem = sim(lru)
    print(f"{name} faults={faults} hits={len(refs) - faults}")
    print(f"{name} trace={trace}")
    print(f"{name} frames=[{' '.join(map(str, mem))}]")
print(f"skipped {skipped}")
