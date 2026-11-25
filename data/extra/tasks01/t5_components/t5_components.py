import re
import sys


def to_int(s):
    return int(s) if re.fullmatch(r"-?[0-9]+", s) else None


lines = [l.strip() for l in sys.stdin.read().splitlines() if l.strip()]
n = to_int(lines[0]) if lines else None
if n is None or n < 0:
    print("bad header")
else:
    parent = list(range(n))

    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    for l in lines[1:]:
        w = l.split()
        if len(w) != 2:
            continue
        u, v = to_int(w[0]), to_int(w[1])
        if u is None or v is None or not (0 <= u < n) or not (0 <= v < n):
            continue
        ru, rv = find(u), find(v)
        if ru != rv:
            parent[ru] = rv
    groups = {}
    for i in range(n):
        groups.setdefault(find(i), []).append(i)
    print("components:", len(groups))
    for members in groups.values():
        print(" ".join(map(str, members)))
