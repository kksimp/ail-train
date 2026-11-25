import sys


def digits(s):
    return s.isascii() and s.isdigit()


def main():
    lines = [l for l in sys.stdin.read().splitlines() if l != ""]
    h = lines[0].split(" ") if lines else []
    if len(h) != 4 or h[0] != "policy" or not all(digits(x) and int(x) >= 1 for x in h[1:]):
        print("error: bad header")
        return
    F, W, L = int(h[1]), int(h[2]), int(h[3])
    fails = {}
    until = {}
    last = 0
    bad = 0
    locks = 0
    for line in lines[1:]:
        f = line.split(" ")
        if len(f) != 3 or not digits(f[0]) or f[1] == "" or f[2] not in ("ok", "fail") or int(f[0]) < last:
            bad += 1
            continue
        t = int(f[0])
        last = t
        u = f[1]
        if until.get(u, 0) > t:
            print(f"{t} {u} denied")
        elif f[2] == "ok":
            fails[u] = []
            print(f"{t} {u} ok")
        else:
            lst = [x for x in fails.get(u, []) if t - x < W]
            lst.append(t)
            if len(lst) >= F:
                until[u] = t + L
                fails[u] = []
                locks += 1
                print(f"{t} {u} locked")
            else:
                fails[u] = lst
                print(f"{t} {u} fail")
    print(f"lockouts: {locks}")
    print(f"malformed: {bad}")


main()
