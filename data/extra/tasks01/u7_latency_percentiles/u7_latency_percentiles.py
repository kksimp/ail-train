import sys


def rank(xs, p):
    n = len(xs)
    r = (p * n + 99) // 100
    return xs[r - 1]


def line(name, xs):
    xs = sorted(xs)
    return f"{name} {len(xs)} {rank(xs, 50)} {rank(xs, 90)} {rank(xs, 99)} {xs[-1]}"


def main():
    groups = {}
    allv = []
    bad = 0
    for ln in sys.stdin.read().splitlines():
        if ln == "":
            continue
        f = ln.split(" ")
        if len(f) != 2 or f[0] == "" or not (f[1].isascii() and f[1].isdigit()):
            bad += 1
            continue
        v = int(f[1])
        groups.setdefault(f[0], []).append(v)
        allv.append(v)
    for k in sorted(groups):
        print(line(k, groups[k]))
    if allv:
        print(line("ALL", allv))
    print(f"malformed: {bad}")


main()
