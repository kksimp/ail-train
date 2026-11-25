import sys


def num(s):
    if s and all(c in "0123456789" for c in s):
        return int(s)
    return None


def main():
    lines = sys.stdin.read().split("\n")
    if lines and lines[-1] == "":
        lines.pop()
    out = []
    pos = {}
    for k, line in enumerate(lines, 1):
        if line == "":
            continue
        f = line.split(" ")
        if f[0] == "po" and len(f) == 4 and f[1] and f[2] and num(f[3]) is not None and f[2] not in pos:
            pos[f[2]] = [f[1], num(f[3]), None]
        elif f[0] == "recv" and len(f) == 3 and num(f[2]) is not None and f[1] in pos \
                and pos[f[1]][2] is None and num(f[2]) >= pos[f[1]][1]:
            pos[f[1]][2] = num(f[2])
        else:
            out.append("bad %d" % k)
    sup = {}
    for s, d, r in pos.values():
        sup.setdefault(s, []).append(None if r is None else r - d)
    for s in sorted(sup):
        got = [x for x in sup[s] if x is not None]
        op = len(sup[s]) - len(got)
        if got:
            t = (20 * sum(got) + len(got)) // (2 * len(got))
            out.append("%s received %d open %d avg %d.%d min %d max %d" % (s, len(got), op, t // 10, t % 10, min(got), max(got)))
        else:
            out.append("%s received 0 open %d avg - min - max -" % (s, op))
    if out:
        print("\n".join(out))


main()
