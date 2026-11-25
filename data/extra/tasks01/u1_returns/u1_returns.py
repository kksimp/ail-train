import sys


def num(s, lo):
    if s and all(c in "0123456789" for c in s) and int(s) >= lo:
        return int(s)
    return None


def main():
    lines = sys.stdin.read().split("\n")
    if lines and lines[-1] == "":
        lines.pop()
    sales = {}
    back = {}
    stock = {}
    total = 0
    out = []
    for k, line in enumerate(lines, 1):
        if line == "":
            continue
        f = line.split(" ")
        if f[0] == "sale" and len(f) == 5 and f[1] and f[2] and num(f[3], 1) and num(f[4], 0) is not None and (f[1], f[2]) not in sales:
            sales[(f[1], f[2])] = (num(f[3], 1), num(f[4], 0))
        elif f[0] == "return" and len(f) in (4, 5) and f[1] and f[2] and num(f[3], 1) and (len(f) == 4 or f[4] == "damaged"):
            key = (f[1], f[2])
            q = num(f[3], 1)
            if key not in sales:
                out.append("reject %s %s none" % key)
            elif q > sales[key][0] - back.get(key, 0):
                out.append("reject %s %s excess" % key)
            else:
                back[key] = back.get(key, 0) + q
                c = q * sales[key][1]
                total += c
                if len(f) == 4:
                    stock[f[2]] = stock.get(f[2], 0) + q
                out.append("refund %s %s %d %d" % (f[1], f[2], q, c))
        else:
            out.append("bad %d" % k)
    for s in sorted(stock):
        out.append("restocked %s %d" % (s, stock[s]))
    out.append("refunds %d" % total)
    print("\n".join(out))


main()
