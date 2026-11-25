import sys


def num(s):
    if s and all(c in "0123456789" for c in s) and int(s) >= 1:
        return int(s)
    return None


def main():
    lines = sys.stdin.read().split("\n")
    if lines and lines[-1] == "":
        lines.pop()
    out = []
    shelf = {}
    ships = {}
    order = []
    for k, line in enumerate(lines, 1):
        if line == "":
            continue
        f = line.split(" ")
        if f[0] == "stock" and len(f) == 4 and f[1] and f[2] and num(f[3]):
            shelf[(f[1], f[2])] = shelf.get((f[1], f[2]), 0) + num(f[3])
        elif f[0] == "transfer" and len(f) == 6 and all(f[1:5]) and num(f[5]) and f[1] not in ships:
            id_, a, b, sku, q = f[1], f[2], f[3], f[4], num(f[5])
            if a == b:
                out.append("reject %s same" % id_)
            elif shelf.get((a, sku), 0) < q:
                out.append("reject %s short" % id_)
            else:
                shelf[(a, sku)] -= q
                ships[id_] = [a, b, sku, q, False]
                order.append(id_)
                out.append("ship " + id_)
        elif f[0] == "receive" and len(f) == 2 and f[1]:
            s = ships.get(f[1])
            if s is None:
                out.append("reject %s unknown" % f[1])
            elif s[4]:
                out.append("reject %s done" % f[1])
            else:
                s[4] = True
                shelf[(s[1], s[2])] = shelf.get((s[1], s[2]), 0) + s[3]
                out.append("arrived " + f[1])
        else:
            out.append("bad %d" % k)
    for (st, sku) in sorted(shelf):
        if shelf[(st, sku)] > 0:
            out.append("shelf %s %s %d" % (st, sku, shelf[(st, sku)]))
    for i in order:
        s = ships[i]
        if not s[4]:
            out.append("transit %s %s %s %s %d" % (i, s[0], s[1], s[2], s[3]))
    if out:
        print("\n".join(out))


main()
