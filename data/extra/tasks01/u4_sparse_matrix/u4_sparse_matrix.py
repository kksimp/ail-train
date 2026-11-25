import sys

def to_int(s):
    t = s[1:] if s.startswith("-") else s
    if t.isascii() and t.isdigit():
        return int(s)
    return None

def idx(s):
    v = to_int(s)
    if v is None or v < 0 or v > 999999:
        return None
    return v

cells = {}
for line in sys.stdin.read().splitlines():
    w = line.split()
    if not w:
        continue
    c = w[0]
    if c in ("set", "add") and len(w) == 4 and idx(w[1]) is not None and idx(w[2]) is not None and to_int(w[3]) is not None:
        key = (idx(w[1]), idx(w[2]))
        v = to_int(w[3])
        nv = v if c == "set" else cells.get(key, 0) + v
        if nv == 0:
            cells.pop(key, None)
        else:
            cells[key] = nv
        print("ok")
    elif c == "get" and len(w) == 3 and idx(w[1]) is not None and idx(w[2]) is not None:
        print(cells.get((idx(w[1]), idx(w[2])), 0))
    elif c == "rowsum" and len(w) == 2 and idx(w[1]) is not None:
        print(sum(v for (r, _), v in cells.items() if r == idx(w[1])))
    elif c == "colsum" and len(w) == 2 and idx(w[1]) is not None:
        print(sum(v for (_, cc), v in cells.items() if cc == idx(w[1])))
    elif c == "nnz" and len(w) == 1:
        print(len(cells))
    elif c == "rows" and len(w) == 1:
        rs = sorted({r for (r, _) in cells})
        print(" ".join(map(str, rs)) if rs else "none")
    else:
        print("error")
