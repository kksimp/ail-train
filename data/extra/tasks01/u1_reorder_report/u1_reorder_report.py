import sys


def num(s):
    if s and all(c in "0123456789" for c in s):
        return int(s)
    return None


def main():
    lines = sys.stdin.read().split("\n")
    if lines and lines[-1] == "":
        lines.pop()
    items = {}
    out = []
    for k, line in enumerate(lines, 1):
        if line == "":
            continue
        f = line.split(" ")
        if f[0] == "item" and len(f) == 7 and f[1] and all(num(x) is not None for x in f[2:]):
            items[f[1]] = [num(x) for x in f[2:]]
        else:
            out.append("bad %d" % k)
    rows = []
    for name, (onhand, daily, lead, safety, target) in items.items():
        point = daily * lead + safety
        if onhand <= point:
            rows.append((-(point - onhand), name, onhand, point, max(target - onhand, 0)))
    rows.sort()
    for neg, name, onhand, point, q in rows:
        out.append("%s onhand %d point %d short %d order %d" % (name, onhand, point, -neg, q))
    out.append("reorder %d of %d" % (len(rows), len(items)))
    print("\n".join(out))


main()
