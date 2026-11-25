import sys


def num(s, lo=0):
    if s and all(c in "0123456789" for c in s) and int(s) >= lo:
        return int(s)
    return None


def main():
    lines = sys.stdin.read().split("\n")
    if lines and lines[-1] == "":
        lines.pop()
    out = []
    lots = {}
    today = 0
    for k, line in enumerate(lines, 1):
        if line == "":
            continue
        f = line.split(" ")
        if f[0] == "lot" and len(f) == 5 and f[1] and f[2] and num(f[3], 1) and num(f[4]) is not None and (f[1], f[2]) not in lots:
            lots[(f[1], f[2])] = [num(f[3], 1), num(f[4])]
        elif f[0] == "asof" and len(f) == 2 and num(f[1]) is not None:
            today = num(f[1])
        elif f[0] == "sell" and len(f) == 3 and f[1] and num(f[2], 1):
            q = num(f[2], 1)
            live = sorted((v[1], key[1], key) for key, v in lots.items() if key[0] == f[1] and v[1] >= today and v[0] > 0)
            if sum(lots[x[2]][0] for x in live) < q:
                out.append("short " + f[1])
                continue
            for _, _, key in live:
                t = min(q, lots[key][0])
                lots[key][0] -= t
                q -= t
            out.append("sold %s %s" % (f[1], f[2]))
        else:
            out.append("bad %d" % k)
    rows = sorted((v[1], key[0], key[1], v[0]) for key, v in lots.items() if v[0] > 0)
    for e, s, l, q in rows:
        if e < today:
            out.append("expired %s %s %d %d" % (s, l, q, e))
    for e, s, l, q in rows:
        if today <= e <= today + 7:
            out.append("soon %s %s %d %d" % (s, l, q, e))
    out.append("expired units %d" % sum(r[3] for r in rows if r[0] < today))
    print("\n".join(out))


main()
