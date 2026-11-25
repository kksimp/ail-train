import sys


def fmt(s):
    return "{" + " ".join(sorted(s)) + "}"


def main():
    sets = {}
    arity = {"union": 4, "inter": 4, "diff": 4, "show": 2, "size": 2, "subset": 3, "del": 2, "names": 1}
    for line in sys.stdin.read().split("\n"):
        w = line.split()
        if not w:
            continue
        c = w[0]
        if c == "set" and len(w) >= 2:
            sets[w[1]] = set(w[2:])
            print(f"{w[1]} = {fmt(sets[w[1]])}")
            continue
        if c not in arity or len(w) != arity[c]:
            print("error: bad command")
            continue
        if c == "names":
            print(" ".join(sorted(sets)) if sets else "(none)")
            continue
        operands = w[2:] if c in ("union", "inter", "diff") else w[1:]
        bad = next((n for n in operands if n not in sets), None)
        if bad is not None:
            print(f"error: unknown set {bad}")
            continue
        if c in ("union", "inter", "diff"):
            a, b = sets[w[2]], sets[w[3]]
            sets[w[1]] = a | b if c == "union" else a & b if c == "inter" else a - b
            print(f"{w[1]} = {fmt(sets[w[1]])}")
        elif c == "show":
            print(fmt(sets[w[1]]))
        elif c == "size":
            print(len(sets[w[1]]))
        elif c == "subset":
            print("yes" if sets[w[1]] <= sets[w[2]] else "no")
        else:
            del sets[w[1]]
            print(f"deleted {w[1]}")


main()
