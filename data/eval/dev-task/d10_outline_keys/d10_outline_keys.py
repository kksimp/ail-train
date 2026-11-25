import sys

path = []
for n, line in enumerate(sys.stdin.read().splitlines(), 1):
    t = line.strip()
    if not t:
        continue
    sp = len(line) - len(line.lstrip())
    colon = t.find(":")
    if colon < 1 or sp % 2 != 0 or sp // 2 > len(path):
        print("bad line %d" % n)
        continue
    del path[sp // 2:]
    path.append(t[:colon].strip())
    val = t[colon + 1:].strip()
    if val:
        print(".".join(path) + "=" + val)
        path.pop()
