import sys

def runs(row):
    out = []
    n = 0
    for ch in row:
        if ch == "#":
            n += 1
        else:
            if n:
                out.append(n)
            n = 0
    if n:
        out.append(n)
    return out

def show(xs):
    return " ".join(str(x) for x in xs) if xs else "none"

for raw in sys.stdin.read().split("\n"):
    line = raw.strip()
    if line == "":
        continue
    parts = line.split(" ")
    if len(parts) != 2:
        print("invalid")
        continue
    clues_s, row = parts
    if row == "" or any(c not in "#." for c in row):
        print("invalid")
        continue
    if clues_s == "0":
        clues = []
    else:
        items = clues_s.split(",")
        if not all(i.isascii() and i.isdigit() and int(i) > 0 for i in items):
            print("invalid")
            continue
        clues = [int(i) for i in items]
    got = runs(row)
    if got == clues:
        print("ok")
    else:
        print("bad: got %s want %s" % (show(got), show(clues)))
