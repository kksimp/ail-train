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
    po = {}
    total = held = 0
    for k, line in enumerate(lines, 1):
        if line == "":
            continue
        f = line.split(" ")
        if f[0] == "po" and len(f) == 5 and f[1] and f[2] and num(f[3], 1) and num(f[4], 0) is not None and (f[1], f[2]) not in po:
            po[(f[1], f[2])] = {"price": num(f[4], 0), "recv": 0, "matched": 0}
        elif f[0] == "recv" and len(f) == 4 and f[1] and f[2] and num(f[3], 1) and (f[1], f[2]) in po:
            po[(f[1], f[2])]["recv"] += num(f[3], 1)
        elif f[0] == "inv" and len(f) == 6 and all(f[1:4]) and num(f[4], 1) and num(f[5], 0) is not None:
            q, p = num(f[4], 1), num(f[5], 0)
            line_ = po.get((f[2], f[3]))
            if line_ is None:
                out.append("%s reject nopo" % f[1])
            elif q > line_["recv"] - line_["matched"]:
                out.append("%s hold qty" % f[1])
                held += 1
            elif abs(p - line_["price"]) * 100 > line_["price"] * 2:
                out.append("%s hold price" % f[1])
                held += 1
            else:
                line_["matched"] += q
                total += q * p
                out.append("%s match %d" % (f[1], q * p))
        else:
            out.append("bad %d" % k)
    out.append("matched %d" % total)
    out.append("held %d" % held)
    print("\n".join(out))


main()
