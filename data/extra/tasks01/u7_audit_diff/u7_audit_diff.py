import sys


def main():
    snaps = {"@before": {}, "@after": {}}
    cur = None
    seen = set()
    bad = 0
    for line in sys.stdin.read().splitlines():
        if line == "":
            continue
        if line.startswith("@"):
            if line in snaps and line not in seen:
                seen.add(line)
                cur = line
            else:
                bad += 1
            continue
        f = line.split(" ", 2)
        if cur is None or len(f) < 3 or f[0] == "" or f[1] == "" or f[2] == "":
            bad += 1
            continue
        snaps[cur].setdefault(f[0], {})[f[1]] = f[2]
    a, b = snaps["@before"], snaps["@after"]
    unchanged = 0
    for u in sorted(set(a) | set(b)):
        if u not in a:
            print(f"{u}: added")
        elif u not in b:
            print(f"{u}: removed")
        else:
            changed = False
            for k in sorted(set(a[u]) | set(b[u])):
                if k not in a[u]:
                    print(f"{u}: +{k} {b[u][k]}")
                    changed = True
                elif k not in b[u]:
                    print(f"{u}: -{k} {a[u][k]}")
                    changed = True
                elif a[u][k] != b[u][k]:
                    print(f"{u}: {k} {a[u][k]} -> {b[u][k]}")
                    changed = True
            if not changed:
                unchanged += 1
    print(f"unchanged: {unchanged}")
    print(f"malformed: {bad}")


main()
