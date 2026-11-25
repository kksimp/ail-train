import sys


def parse(line):
    f = line.split(" ")
    if len(f) != 3:
        return None
    t = f[1]
    if not (t.isascii() and t.isdigit()):
        if not (t.startswith("-") and t[1:].isascii() and t[1:].isdigit()):
            return None
    d = int(t)
    if d < 0:
        return None
    deps = [] if f[2] == "-" else f[2].split(",")
    return (f[0], d, deps)


items = {}
names = []
for n, line in enumerate(sys.stdin.read().splitlines(), 1):
    if line.strip() == "":
        continue
    it = parse(line)
    if it is None or it[0] in items:
        print(f"bad line {n}")
        continue
    items[it[0]] = it
    names.append(it[0])
for name in names:
    for d in items[name][2]:
        if d not in items:
            print(f"error: unknown dependency {d} in {name}")
            sys.exit(0)
left = {n: len(items[n][2]) for n in names}
users = {}
for n in names:
    for d in items[n][2]:
        users.setdefault(d, []).append(n)
ready = [n for n in names if left[n] == 0]
start, finish, done = {}, {}, []
while ready:
    cur = min(ready, key=lambda s: s.encode())
    ready.remove(cur)
    deps = items[cur][2]
    s = max((finish[d] for d in deps), default=0)
    start[cur] = s
    finish[cur] = s + items[cur][1]
    done.append(cur)
    for u in users.get(cur, []):
        left[u] -= 1
        if left[u] == 0:
            ready.append(u)
if len(done) < len(names):
    print("error: cycle")
    sys.exit(0)
for n in done:
    print(f"{n} {start[n]} {finish[n]}")


def pick(cands):
    best = None
    for c in cands:
        if best is None or finish[c] > finish[best] or (finish[c] == finish[best] and c.encode() < best.encode()):
            best = c
    return best


last = pick(names)
print(f"length {finish[last] if last else 0}")
chain = []
cur = last
while cur is not None:
    chain.append(cur)
    cur = pick(items[cur][2])
print("critical: " + " -> ".join(reversed(chain)) if chain else "critical: none")
