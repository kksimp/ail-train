import sys


def digits(s):
    return s.isascii() and s.isdigit()


def main():
    lines = [l for l in sys.stdin.read().splitlines() if l != ""]
    h = lines[0].split(" ") if lines else []
    ok = len(h) == 4 and h[0] == "window" and h[2] == "threshold" and digits(h[1]) and digits(h[3])
    if ok and (int(h[1]) < 1 or int(h[3]) < 1):
        ok = False
    if not ok:
        print("error: bad header")
        return
    w, k = int(h[1]), int(h[3])
    errs = []
    bad = 0
    last = 0
    for line in lines[1:]:
        f = line.split(" ", 2)
        if len(f) < 2 or not digits(f[0]) or int(f[0]) < last:
            bad += 1
            continue
        last = int(f[0])
        if f[1] == "ERROR":
            errs.append(last)
    i = 0
    out = []
    while i < len(errs):
        t = errs[i]
        j = i
        while j < len(errs) and errs[j] <= t + w - 1:
            j += 1
        if j - i >= k:
            out.append(f"burst {t} {errs[j - 1]} {j - i}")
            i = j
        else:
            i += 1
    for o in out:
        print(o)
    print(f"bursts: {len(out)}")
    print(f"malformed: {bad}")


main()
