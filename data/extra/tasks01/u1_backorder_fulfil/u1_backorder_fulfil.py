import sys


def num(s):
    if s and all(c in "0123456789" for c in s):
        n = int(s)
        if n >= 1:
            return n
    return None


def main():
    lines = sys.stdin.read().split("\n")
    if lines and lines[-1] == "":
        lines.pop()
    onhand = {}
    backs = []
    out = []
    for k, line in enumerate(lines, 1):
        if line == "":
            continue
        f = line.split(" ")
        if f[0] == "stock" and len(f) == 3 and f[1] and num(f[2]):
            onhand[f[1]] = onhand.get(f[1], 0) + num(f[2])
        elif f[0] == "order" and len(f) == 4 and f[1] and f[2] and num(f[3]):
            q = num(f[3])
            have = onhand.get(f[2], 0)
            ship = min(have, q)
            onhand[f[2]] = have - ship
            if q > ship:
                backs.append([f[1], f[2], q - ship])
            out.append("%s shipped %d backorder %d" % (f[1], ship, q - ship))
        elif f[0] == "restock" and len(f) == 3 and f[1] and num(f[2]):
            onhand[f[1]] = onhand.get(f[1], 0) + num(f[2])
            for b in backs:
                if b[1] == f[1] and b[2] > 0 and onhand[f[1]] > 0:
                    n = min(b[2], onhand[f[1]])
                    b[2] -= n
                    onhand[f[1]] -= n
                    out.append("fill %s %d" % (b[0], n))
        else:
            out.append("bad %d" % k)
    for s in sorted(onhand):
        out.append("on-hand %s %d" % (s, onhand[s]))
    for b in backs:
        if b[2] > 0:
            out.append("open %s %s %d" % (b[0], b[1], b[2]))
    if out:
        print("\n".join(out))


main()
