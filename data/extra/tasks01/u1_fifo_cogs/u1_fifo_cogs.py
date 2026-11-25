import sys


def num(s):
    if s and all(c in "0123456789" for c in s):
        return int(s)
    return None


def main():
    lines = sys.stdin.read().split("\n")
    if lines and lines[-1] == "":
        lines.pop()
    lots = {}
    out = []
    total = 0
    for k, line in enumerate(lines, 1):
        if line == "":
            continue
        f = line.split(" ")
        if f[0] == "buy" and len(f) == 4 and f[1] and num(f[2]) and num(f[3]) is not None:
            lots.setdefault(f[1], []).append([num(f[2]), num(f[3])])
        elif f[0] == "sell" and len(f) == 3 and f[1] and num(f[2]):
            q = num(f[2])
            L = lots.get(f[1], [])
            if sum(x[0] for x in L) < q:
                out.append("short " + f[1])
                continue
            cogs = 0
            need = q
            while need > 0:
                take = min(need, L[0][0])
                cogs += take * L[0][1]
                L[0][0] -= take
                need -= take
                if L[0][0] == 0:
                    L.pop(0)
            total += cogs
            out.append("sold %s %d cogs %d" % (f[1], q, cogs))
        else:
            out.append("bad %d" % k)
    for s in sorted(lots):
        q = sum(x[0] for x in lots[s])
        if q > 0:
            out.append("stock %s %d %d" % (s, q, sum(x[0] * x[1] for x in lots[s])))
    out.append("cogs %d" % total)
    print("\n".join(out))


main()
