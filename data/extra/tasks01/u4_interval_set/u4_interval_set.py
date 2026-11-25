import sys

def to_int(s):
    t = s[1:] if s.startswith("-") else s
    if t.isascii() and t.isdigit():
        return int(s)
    return None

iv = []  # sorted disjoint, non-touching

def add(l, r):
    out = []
    for a, b in iv:
        if b < l or a > r:
            out.append((a, b))
        else:
            l = min(l, a)
            r = max(r, b)
    out.append((l, r))
    out.sort()
    return out

def remove(l, r):
    out = []
    for a, b in iv:
        if b <= l or a >= r:
            out.append((a, b))
            continue
        if a < l:
            out.append((a, l))
        if b > r:
            out.append((r, b))
    return out

for line in sys.stdin.read().splitlines():
    w = line.split()
    if not w:
        continue
    c = w[0]
    if c in ("add", "remove") and len(w) == 3 and to_int(w[1]) is not None and to_int(w[2]) is not None:
        l, r = to_int(w[1]), to_int(w[2])
        if l >= r:
            print("bad")
        else:
            iv = add(l, r) if c == "add" else remove(l, r)
            print("ok")
    elif c == "query" and len(w) == 2 and to_int(w[1]) is not None:
        x = to_int(w[1])
        print("yes" if any(a <= x < b for a, b in iv) else "no")
    elif c == "total" and len(w) == 1:
        print(sum(b - a for a, b in iv))
    elif c == "show" and len(w) == 1:
        print(" ".join(f"[{a},{b})" for a, b in iv) if iv else "empty")
    else:
        print("error")
