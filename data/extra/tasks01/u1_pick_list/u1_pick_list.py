import sys


def num(s):
    if s and all(c in "0123456789" for c in s) and int(s) >= 1:
        return int(s)
    return None


def main():
    lines = sys.stdin.read().split("\n")
    if lines and lines[-1] == "":
        lines.pop()
    loc = {}
    need = {}
    out = []
    for k, line in enumerate(lines, 1):
        if line == "":
            continue
        f = line.split(" ")
        if f[0] == "loc" and len(f) == 3 and f[1] and f[2]:
            loc[f[1]] = f[2]
        elif f[0] == "pick" and len(f) == 4 and f[1] and f[2] and num(f[3]):
            need[f[2]] = need.get(f[2], 0) + num(f[3])
        else:
            out.append("bad %d" % k)
    rows = sorted((loc.get(s, "~"), s, q) for s, q in need.items())
    last = None
    units = 0
    for b, s, q in rows:
        if b != last:
            out.append("bin " + ("NOBIN" if b == "~" else b))
            last = b
        out.append("  %s %d" % (s, q))
        units += q
    out.append("lines %d units %d" % (len(rows), units))
    print("\n".join(out))


main()
