import sys


def num(s, lo):
    if s and all(c in "0123456789" for c in s) and int(s) >= lo:
        return int(s)
    return None


def main():
    lines = sys.stdin.read().split("\n")
    if lines and lines[-1] == "":
        lines.pop()
    out = []
    rates = {}
    items = []
    for k, line in enumerate(lines, 1):
        if line == "":
            continue
        f = line.split(" ")
        if f[0] == "tax" and len(f) == 3 and f[1] and num(f[2], 0) is not None and num(f[2], 0) <= 10000:
            rates[f[1]] = num(f[2], 0)
        elif f[0] == "item" and len(f) == 5 and f[1] and f[2] and num(f[3], 0) is not None and num(f[4], 1):
            items.append((f[1], f[2], num(f[3], 0) * num(f[4], 1)))
        else:
            out.append("bad %d" % k)
    cats = {}
    tn = tt = 0
    for name, cat, net in items:
        t = (net * rates.get(cat, 0) + 5000) // 10000
        out.append("%s net %d tax %d%s" % (name, net, t, "" if cat in rates else " no rate"))
        c = cats.setdefault(cat, [0, 0])
        c[0] += net
        c[1] += t
        tn += net
        tt += t
    for cat in sorted(cats):
        out.append("cat %s net %d tax %d" % (cat, cats[cat][0], cats[cat][1]))
    out += ["net %d" % tn, "tax %d" % tt, "total %d" % (tn + tt)]
    print("\n".join(out))


main()
