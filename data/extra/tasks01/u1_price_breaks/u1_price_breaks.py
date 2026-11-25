import sys


def num(s, lo):
    if s and all(c in "0123456789" for c in s) and int(s) >= lo:
        return int(s)
    return None


def main():
    lines = sys.stdin.read().split("\n")
    if lines and lines[-1] == "":
        lines.pop()
    tiers = {}
    out = []
    total = 0
    for k, line in enumerate(lines, 1):
        if line == "":
            continue
        f = line.split(" ")
        if f[0] == "price" and len(f) == 4 and f[1] and num(f[2], 1) and num(f[3], 0) is not None:
            tiers.setdefault(f[1], {})[num(f[2], 1)] = num(f[3], 0)
        elif f[0] == "buy" and len(f) == 3 and f[1] and num(f[2], 1):
            q = num(f[2], 1)
            t = tiers.get(f[1], {})
            below = [m for m in t if m <= q]
            if not below:
                out.append("%s %d no price" % (f[1], q))
                continue
            u = t[max(below)]
            s = "%s %d @ %d = %d" % (f[1], q, u, q * u)
            total += q * u
            above = [m for m in t if m > q]
            if above:
                s += " next %d @ %d" % (min(above), t[min(above)])
            out.append(s)
        else:
            out.append("bad %d" % k)
    out.append("total %d" % total)
    print("\n".join(out))


main()
